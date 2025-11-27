"""
TutorHub Application - Flask Backend
Layer Architecture:
- Presentation Layer: Routes (Flask routes)
- Business Logic Layer: Service functions
- Data Layer: Hardcoded data
"""

from flask import Flask, render_template, request, redirect, url_for, session, flash, abort

from data import (
    TUTORS,
    USERS,
    PROGRAM_FEATURES,
    PROGRAM_BENEFITS,
    PROGRAM_GALLERY,
    RESOURCES,
    KEYWORDS,
    FILE_TYPES,
)

app = Flask(__name__)
app.secret_key = 'tutorhub_secret_key_2025'  # For session management


# ==================== BUSINESS LOGIC LAYER ====================

def get_all_tutors():
    """Get all tutors"""
    return TUTORS

def authenticate_user(username, password):
    """Authenticate user credentials"""
    if username in USERS and USERS[username]['password'] == password:
        return USERS[username]
    return None


def get_resource_by_id(resource_id: int):
    for r in RESOURCES:
        if r.get('id') == resource_id:
            return r
    return None


# ==================== PRESENTATION LAYER ====================
# Routes - Handle HTTP requests and responses

@app.route('/')
def index():
    """Landing page"""
    tutors = get_all_tutors()
    return render_template('index.html', tutors=tutors)

@app.route('/login')
def login():
    """Login page - Choose login method"""
    return render_template('login.html')

@app.route('/login/hcmut', methods=['GET', 'POST'])
def login_hcmut():
    """HCMUT Login form"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = authenticate_user(username, password)
        if user:
            session['user'] = user
            flash('Đăng nhập thành công!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Tên đăng nhập hoặc mật khẩu không đúng!', 'error')
    
    return render_template('login_form.html', login_type='HCMUT Login')

@app.route('/login/admin', methods=['GET', 'POST'])
def login_admin():
    """Administrator Login form"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = authenticate_user(username, password)
        if user and user['role'] == 'admin':
            session['user'] = user
            flash('Đăng nhập quản trị viên thành công!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Tên đăng nhập hoặc mật khẩu không đúng!', 'error')
    
    return render_template('login_form.html', login_type='Administrator Login')

@app.route('/home')
def home():
    """Authenticated landing page"""
    user = session.get('user')
    if not user:
        flash('Vui lòng đăng nhập để tiếp tục.', 'error')
        return redirect(url_for('login'))
    
    return render_template(
        'home.html',
        user=user,
        features=PROGRAM_FEATURES,
        benefits=PROGRAM_BENEFITS,
        gallery=PROGRAM_GALLERY
    )


@app.route('/materials')
def materials():
    """Materials / Resources browsing page"""
    user = session.get('user')
    if not user:
        flash('Vui lòng đăng nhập để tiếp tục.', 'error')
        return redirect(url_for('login'))
    # Read filters from query string
    q = request.args.get('q', '').strip().lower()
    selected_keywords = request.args.getlist('keywords')
    raw_selected_files = request.args.getlist('file_types')
    sort = request.args.get('sort', 'newest')

    # If there are no query params at all (initial page load), default to
    # selecting all file types and no keywords. If the user submitted the form
    # (request.args present) and didn't select any file types, honor that as
    # an explicit "none selected" state.
    request_has_args = bool(request.args)
    if not request_has_args:
        selected_files = list(FILE_TYPES)
    else:
        selected_files = raw_selected_files

    # Start with the full list
    filtered = list(RESOURCES)

    # If the user did not select any keywords and did not select any file types,
    # return an empty result set (explicitly cleared filters).
    if not selected_keywords and not selected_files:
        filtered = []
    else:
        # Text search (title or tutor)
        if q:
            filtered = [r for r in filtered if q in r.get('title', '').lower() or q in r.get('tutor', '').lower()]

        # Keyword filtering (match any selected keyword)
        if selected_keywords:
            filtered = [r for r in filtered if any(kw in r.get('keywords', []) for kw in selected_keywords)]

        # File type filtering
        if selected_files:
            lower_selected = [s.lower() for s in selected_files]
            def file_match(r):
                ft = r.get('file_type', '') or ''
                ft_l = ft.lower()
                return any(s in ft_l for s in lower_selected)
            filtered = [r for r in filtered if file_match(r)]

    # Sorting
    if sort == 'most_views':
        filtered.sort(key=lambda r: r.get('viewed', 0), reverse=True)
    elif sort == 'az':
        filtered.sort(key=lambda r: r.get('title', '').lower())

    return render_template(
        'materials.html',
        resources=filtered,
        keywords=KEYWORDS,
        file_types=FILE_TYPES,
        current_q=request.args.get('q', ''),
        selected_keywords=selected_keywords,
        selected_files=selected_files,
        current_sort=sort
    )


@app.route('/preview/<int:resource_id>')
def preview(resource_id: int):
    resource = get_resource_by_id(resource_id)
    if not resource:
        abort(404)
    # Derive course name from the title if not explicitly provided.
    title = resource.get('title', '')
    course_name = resource.get('course')
    if not course_name and title:
        # Attempt to split by dash/ hyphen " - " first (common pattern: "Course - Chapter X")
        if ' - ' in title:
            course_name = title.split(' - ')[0].strip()
        else:
            # Fallback: remove the word 'Chapter' and everything after it
            parts = title.split('Chapter')
            if parts and parts[0].strip():
                course_name = parts[0].strip().rstrip('-').strip()
    return render_template('preview.html', resource=resource, resource_course=course_name)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

