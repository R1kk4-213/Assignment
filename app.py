"""
TutorHub Application - Flask Backend
Layer Architecture:
- Presentation Layer: Routes (Flask routes)
- Business Logic Layer: Service functions
- Data Layer: Hardcoded data
"""

from flask import Flask, render_template, request, redirect, url_for, session, flash

from data import (
    TUTORS,
    USERS,
    PROGRAM_FEATURES,
    PROGRAM_BENEFITS,
    PROGRAM_GALLERY,
    TUTOR_PROFILE,
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

def get_tutor_profile():
    """Return the active tutor profile."""
    return TUTOR_PROFILE

def update_tutor_profile(bio, phone, areas):
    """Persist editable fields from the profile form."""
    TUTOR_PROFILE['biography'] = bio
    TUTOR_PROFILE['phone_number'] = phone
    TUTOR_PROFILE['areas_of_expertise'] = areas
    return TUTOR_PROFILE


# ==================== PRESENTATION LAYER ====================
# Routes - Handle HTTP requests and responses

@app.route('/')
def index():
    """Landing page"""
    tutors = get_all_tutors()
    return render_template('index.html', tutors=tutors)

#Huy work

@app.route('/track_progress')
def track_progress():
    """Track Student Progress"""
    tutors = get_all_tutors()
    return render_template('track_progress.html', tutors=tutors)

@app.route('/feedback_list')
def feedback_list():
    """Get all the feedback"""
    tutors = get_all_tutors()
    return render_template('feedback_list.html', tutors=tutors)

@app.route('/tutor_home')
def tutor_home():
    """Get the dashboard of tutors"""
    tutors = get_all_tutors()
    return render_template('tutor_home.html', tutors=tutors)

@app.route('/submit_feedback')
def submit_feedback():
    """Submit feedback for tutors"""
    tutors = get_all_tutors()
    return render_template('submit_feedback.html', tutors=tutors)

#End of Huy work

@app.route('/login')
def login():
    """Login page - Choose login method"""
    return render_template('login.html')

# @app.route('/login/hcmut', methods=['GET', 'POST'])
# def login_hcmut():
#     """HCMUT Login form"""
#     if request.method == 'POST':
#         username = request.form.get('username')
#         password = request.form.get('password')
        
#         user = authenticate_user(username, password)
#         if user:
#             session['user'] = user
#             flash('Đăng nhập thành công!', 'success')
#             return redirect(url_for('home'))
#         else:
#             flash('Tên đăng nhập hoặc mật khẩu không đúng!', 'error')
    
#     return render_template('login_form.html', login_type='HCMUT Login')

@app.route('/login/hcmut', methods=['GET', 'POST'])
def login_hcmut():
    """HCMUT Login for only student + tutor"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Use your authenticate_user directly
        user = authenticate_user(username, password)

        if user:
            # Save session without password
            session['user'] = {
                'username': user['username'],
                'email': user['email'],
                'role': user['role'],
                'name': user['name'],
                # optional fields; safe to include
                'student_id': user.get('student_id'),
                'class': user.get('class'),
                'department': user.get('department')
            }

            # Redirect depending on role
            if user['role'] == 'student':
                flash(f'Welcome student {user["name"]}!', 'success')
                return redirect(url_for('home'))

            else:
                flash(f'Welcome tutor {user["name"]}!', 'success')
                return redirect(url_for('tutor_dashboard'))

            # fallback
            return redirect(url_for('home'))

        else:
            flash('Incorrect username or password!', 'error')

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
@app.route('/tutor-dashboard')
def tutor_dashboard():
    """Tutor dashboard page"""
    user = session.get('user')
    if not user:
        flash('Vui lòng đăng nhập để tiếp tục.', 'error')
        return redirect(url_for('login'))

    # If later you distinguish roles, you can also check user['role'] == 'tutor' here

    return render_template(
        'tutor_dashboard.html',
        user=user
    )

@app.route('/find-tutor')
def find_tutor():
    return render_template("request.html")

# @app.route('/')
# def reloadpage():
#     return render_template("index.html")  # trang landing này
@app.route('/my-tutors')
def my_tutors():
    return render_template("mytutor.html")
@app.route('/response_page')
def response_page():
    return render_template("response.html")
@app.route('/resources')
def resources():
    pass

@app.route('/view-profile')
def view_profile():
    """Display tutor profile information."""
    user = session.get('user')
    if not user:
        flash('Vui lòng đăng nhập để tiếp tục.', 'error')
        return redirect(url_for('login'))
    
    profile = get_tutor_profile()
    return render_template(
        'view_profile.html',
        user=user,
        profile=profile
    )

@app.route('/edit-profile', methods=['GET', 'POST'])
def edit_profile():
    """Allow editing of the expertise area only."""
    user = session.get('user')
    if not user:
        flash('Vui lòng đăng nhập để tiếp tục.', 'error')
        return redirect(url_for('login'))
    
    profile = get_tutor_profile()
    if request.method == 'POST':
        raw_expertise = request.form.get('areas_of_expertise', '')
        biography = request.form.get('biography', '').strip()
        phone_number = request.form.get('phone_number', '').strip()
        
        parsed = [tag.strip() for tag in raw_expertise.split(',') if tag.strip()]
        if not parsed:
            flash('Vui lòng nhập ít nhất một lĩnh vực chuyên môn.', 'error')
            return redirect(url_for('edit_profile'))
        if not biography:
            flash('Vui lòng nhập Biography.', 'error')
            return redirect(url_for('edit_profile'))
        if not phone_number:
            flash('Vui lòng nhập Phone Number.', 'error')
            return redirect(url_for('edit_profile'))
        
        update_tutor_profile(biography, phone_number, parsed)
        flash('Cập nhật hồ sơ thành công!', 'success')
        return redirect(url_for('view_profile'))
    
    return render_template(
        'edit_profile.html',
        user=user,
        profile=profile
    )

if __name__ == '__main__':
    app.run(debug=True, port=5000)

