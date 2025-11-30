

"""
TutorHub Application - Flask Backend
Layer Architecture:
- Presentation Layer: Routes (Flask routes)
- Business Logic Layer: Service functions
- Data Layer: Hardcoded data
"""

import os
import threading
from flask import Flask, render_template, request, redirect, url_for, session, flash, abort, jsonify
from datetime import datetime
from data import (
    TUTORS,
    USERS,
    STUDENTS,
    SESSIONS,
    PROGRAM_FEATURES,
    PROGRAM_BENEFITS,
    PROGRAM_GALLERY,
    TUTOR_PROFILE,
    RECENT_ACTIVITIES,
    RESOURCES,
    KEYWORDS,
    FILE_TYPES,
)

app = Flask(__name__)
app.secret_key = 'tutorhub_secret_key_2025'  # For session management

# Simple hardcoded configuration
CONFIG = {
    'max_students': 10,
    'session_duration': 90
}

# Simple helper function for activities
def add_activity(action, description):
    """Add new activity to hardcoded list"""
    new_activity = {
        'action': action,
        'description': description,
        'time': datetime.now().strftime('%H:%M'),
        'date': datetime.now().strftime('%Y-%m-%d')
    }
    RECENT_ACTIVITIES.insert(0, new_activity)
    # Keep only last 20 activities
    if len(RECENT_ACTIVITIES) > 20:
        RECENT_ACTIVITIES.pop()


# ==================== BUSINESS LOGIC LAYER ====================
def get_all_tutors():
    """Get all tutors"""
    return TUTORS

def authenticate_user(username, password):
    """Authenticate user credentials"""
    if username in USERS and USERS[username]['password'] == password:
        return USERS[username]
    return None

<<<<<<< HEAD
def get_tutor_profile():
    """Return the active tutor profile."""
    return TUTOR_PROFILE

def update_tutor_profile(bio, phone, areas):
    """Persist editable fields from the profile form."""
    TUTOR_PROFILE['biography'] = bio
    TUTOR_PROFILE['phone_number'] = phone
    TUTOR_PROFILE['areas_of_expertise'] = areas
    return TUTOR_PROFILE

def get_dashboard_stats():
    """Calculate dashboard statistics from actual data"""
    from datetime import datetime, timedelta
    
    total_tutors = len(TUTORS)
    active_tutors = len([t for t in TUTORS if t.get('active', True)])
    
    # Calculate percentage change vs last month
    current_date = datetime.now()
    last_month = current_date - timedelta(days=30)
    
    # Count tutors added in last month
    tutors_last_month = len([
        t for t in TUTORS 
        if datetime.strptime(t.get('added_date', '2025-01-01'), '%Y-%m-%d') >= last_month
    ])
    
    # Calculate percentage
    if total_tutors > 0:
        total_change_pct = round((tutors_last_month / total_tutors) * 100)
        active_change_pct = round((tutors_last_month / active_tutors) * 100) if active_tutors > 0 else 0
    else:
        total_change_pct = 0
        active_change_pct = 0
    
    return {
        'total_tutors': total_tutors,
        'active_tutors': active_tutors,
        'total_change_pct': total_change_pct,
        'active_change_pct': active_change_pct
    }

def get_monthly_trends():
    """Calculate monthly tutor adding trends from actual data"""
    from datetime import datetime
    from collections import defaultdict
    
    added_by_month = defaultdict(int)
    removed_by_month = defaultdict(int)
    
    # Count tutors added by month
    for tutor in TUTORS:
        date_str = tutor.get('added_date', '2025-01-01')
        date = datetime.strptime(date_str, '%Y-%m-%d')
        month_key = date.strftime('%B')
        
        if tutor.get('active', True):
            added_by_month[month_key] += 1
        else:
            # Suspended tutors count as removed
            removed_by_month[month_key] += 1
    
    # Get last 5 months
    months = ['January', 'February', 'March', 'April', 'May']
    
    return {
        'labels': months,
        'added': [added_by_month.get(m, 0) for m in months],
        'removed': [removed_by_month.get(m, 0) for m in months]
    }

def get_reports_data(period='monthly'):
    """Generate simple hardcoded reports data"""
    import random
    
    # Simple hardcoded data based on period
    if period == 'yearly':
        labels = ['2020', '2021', '2022', '2023', '2024', '2025']
        page_views = [1200, 1500, 1800, 2100, 2400, 2700]
        clicks = [800, 1000, 1200, 1400, 1600, 1800]
        inquiries = [1800, 2000, 2200, 2400, 2600, 2800]
        enrollments = [1200, 1400, 1600, 1800, 2000, 2200]
    elif period == 'quarterly':
        labels = ['Q1 2024', 'Q2 2024', 'Q3 2024', 'Q4 2024', 'Q1 2025', 'Q2 2025']
        page_views = [360, 450, 540, 630, 720, 810]
        clicks = [240, 300, 360, 420, 480, 540]
        inquiries = [540, 600, 660, 720, 780, 840]
        enrollments = [360, 420, 480, 540, 600, 660]
    else:  # monthly
        labels = ['January', 'February', 'March', 'April', 'May', 'June']
        page_views = [120, 320, 240, 180, 210, 280]
        clicks = [80, 180, 110, 120, 150, 190]
        inquiries = [180, 220, 190, 200, 210, 240]
        enrollments = [120, 150, 130, 140, 150, 170]
    
    return {
        'traffic': {
            'labels': labels,
            'page_views': page_views,
            'clicks': clicks
        },
        'enrollment': {
            'labels': labels,
            'inquiries': inquiries,
            'enrollments': enrollments
        }
    }


def get_resource_by_id(resource_id: int):
    for r in RESOURCES:
        if r.get('id') == resource_id:
            return r
    return None


=======
>>>>>>> origin/create_session
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
<<<<<<< HEAD

        # Use your authenticate_user directly
=======
>>>>>>> origin/create_session
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

        else:
<<<<<<< HEAD
            flash('Incorrect username or password!', 'error')

=======
            flash('Tên đăng nhập hoặc mật khẩu không đúng!', 'error')
>>>>>>> origin/create_session
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
            flash('Admin login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
<<<<<<< HEAD
            flash('Invalid username or password!', 'error')
    
=======
            flash('Tên đăng nhập hoặc mật khẩu không đúng!', 'error')
>>>>>>> origin/create_session
    return render_template('login_form.html', login_type='Administrator Login')

@app.route('/home')
def home():
    """Authenticated landing page"""
    user = session.get('user')
    if not user:
        flash('Please login to continue.', 'error')
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

@app.route('/dashboard')
def dashboard():
    """Admin Dashboard"""
    user = session.get('user')
    if not user:
        flash('Please login to continue.', 'error')
        return redirect(url_for('login'))
    
    if user['role'] != 'admin':
        flash('You do not have permission to access this page.', 'error')
        return redirect(url_for('home'))
    
    # Get real statistics from data
    stats = get_dashboard_stats()
    monthly_trends = get_monthly_trends()
    
    return render_template(
        'dashboard.html',
        user=user,
        stats=stats,
        recent_activities=RECENT_ACTIVITIES,
        monthly_trends=monthly_trends
    )

@app.route('/tutor-management')
def tutor_management():
    """Tutor Management Page"""
    user = session.get('user')
    if not user:
        flash('Please login to continue.', 'error')
        return redirect(url_for('login'))
    
    if user['role'] != 'admin':
        flash('You do not have permission to access this page.', 'error')
        return redirect(url_for('home'))
    
    # Get tutors with email
    tutors_with_email = []
    for tutor in TUTORS:
        tutor_copy = tutor.copy()
        # Generate email from name
        name_parts = tutor['name'].lower().replace('ă', 'a').replace('â', 'a').replace('đ', 'd')
        name_parts = name_parts.replace('ê', 'e').replace('ô', 'o').replace('ơ', 'o').replace('ư', 'u')
        name_parts = name_parts.split()
        if len(name_parts) >= 2:
            email = f"{name_parts[-1]}.{name_parts[0][0]}@example.com"
        else:
            email = f"{name_parts[0]}@example.com"
        tutor_copy['email'] = email
        tutors_with_email.append(tutor_copy)
    
    return render_template(
        'tutor_management.html',
        user=user,
        tutors=tutors_with_email
    )

@app.route('/tutor/toggle-status/<int:tutor_id>', methods=['POST'])
def toggle_tutor_status(tutor_id):
    """Toggle tutor active status"""
    user = session.get('user')
    if not user or user['role'] != 'admin':
        return {'success': False, 'message': 'Unauthorized'}, 403
    
    # Find tutor in TUTORS list
    for tutor in TUTORS:
        if tutor['id'] == tutor_id:
            tutor['active'] = not tutor['active']
            status = 'activated' if tutor['active'] else 'removed'
            
            # Add activity
            action = 'activate' if tutor['active'] else 'remove'
            add_activity(action, f'{status.capitalize()} tutor: {tutor["name"]}')
            
            return {
                'success': True, 
                'message': f'Tutor {status} successfully',
                'new_status': tutor['active']
            }
    
    return {'success': False, 'message': 'Tutor not found'}, 404

@app.route('/search-users')
def search_users():
    """Search users in database for promotion to tutor"""
    user = session.get('user')
    if not user or user['role'] != 'admin':
        return {'success': False, 'message': 'Unauthorized'}, 403
    
    query = request.args.get('q', '').lower()
    
    # Get list of existing tutor names to exclude them
    existing_tutor_usernames = set()
    for tutor in TUTORS:
        # Generate username from tutor name
        name_parts = tutor['name'].lower().replace(' ', '').replace('ă', 'a').replace('â', 'a').replace('đ', 'd')
        name_parts = name_parts.replace('ê', 'e').replace('ô', 'o').replace('ơ', 'o').replace('ư', 'u')
        existing_tutor_usernames.add(name_parts)
    
    # Search through USERS
    results = []
    for username, user_data in USERS.items():
        # Skip if already a tutor
        if username in existing_tutor_usernames:
            continue
        
        # Skip admin accounts
        if user_data.get('role') == 'admin':
            continue
        
        # Search by username, name, or email
        if query == '' or \
           query in username.lower() or \
           query in user_data.get('name', '').lower() or \
           query in user_data.get('email', '').lower():
            results.append({
                'username': username,
                'name': user_data.get('name', username),
                'email': user_data.get('email', '')
            })
    
    return {'success': True, 'users': results}

@app.route('/promote-to-tutor', methods=['POST'])
def promote_to_tutor():
    """Promote a user to tutor"""
    user = session.get('user')
    if not user or user['role'] != 'admin':
        return {'success': False, 'message': 'Unauthorized'}, 403
    
    data = request.json
    username = data.get('username')
    
    if not username or username not in USERS:
        return {'success': False, 'message': 'User not found'}, 404
    
    user_data = USERS[username]
    
    # Create new tutor entry
    new_tutor_id = max([t['id'] for t in TUTORS]) + 1 if TUTORS else 1
    
    new_tutor = {
        'id': new_tutor_id,
        'name': user_data.get('name', username),
        'title': 'Instructor',  # Default title
        'subject': 'General',   # Default subject
        'rating': 0.0,
        'image': 'default-avatar.jpg',
        'active': True,
        'added_date': datetime.now().strftime('%Y-%m-%d')
    }
    
    TUTORS.append(new_tutor)
    
    # Add activity
    add_activity('add', f'Added new tutor: {user_data.get("name", username)}')
    
    return {
        'success': True, 
        'message': f'{user_data.get("name", username)} has been promoted to tutor',
        'tutor': new_tutor
    }

@app.route('/configuration', methods=['GET'])
def configuration():
    """Configuration page"""
    user = session.get('user')
    if not user:
        flash('Please login to continue.', 'error')
        return redirect(url_for('login'))
    
    if user['role'] != 'admin':
        flash('You do not have permission to access this page.', 'error')
        return redirect(url_for('home'))
    
    return render_template('configuration.html', user=user, config=CONFIG)

@app.route('/save-configuration', methods=['POST'])
def save_configuration():
    """Save configuration settings"""
    user = session.get('user')
    if not user or user['role'] != 'admin':
        return {'success': False, 'message': 'Unauthorized'}, 403
    
    try:
        max_students = int(request.form.get('maxStudents', 10))
        session_duration = int(request.form.get('sessionDuration', 90))
        
        # Update hardcoded config
        CONFIG['max_students'] = max_students
        CONFIG['session_duration'] = session_duration
        
        # Add activity
        add_activity('update', f'Updated configuration: Max students={max_students}, Session duration={session_duration}min')
        
        flash('Configuration saved successfully!', 'success')
        return redirect(url_for('configuration'))
    except Exception as e:
        flash(f'Error saving configuration: {str(e)}', 'error')
        return redirect(url_for('configuration'))

@app.route('/reports')
def reports():
    """Reports page"""
    user = session.get('user')
    if not user:
        flash('Please login to continue.', 'error')
        return redirect(url_for('login'))
    
    if user['role'] != 'admin':
        flash('You do not have permission to access this page.', 'error')
        return redirect(url_for('home'))
    
    period = request.args.get('period', 'monthly')
    reports_data = get_reports_data(period)
    return render_template('reports.html', user=user, reports_data=reports_data, current_period=period)


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

@app.route('/edit_session')
def edit_session():
    """Edit session page - Only for tutors"""
    user = session.get('user')
    if not user:
        flash('Vui lòng đăng nhập để tiếp tục.', 'error')
        return redirect(url_for('login'))
    if user.get('role') != 'tutor':
        flash('Chỉ giáo viên mới có thể truy cập trang này.', 'error')
        return redirect(url_for('home'))
    return render_template('edit_session.html', user=user, students=STUDENTS, sessions=SESSIONS)

# API Routes for Session Management
@app.route('/api/sessions', methods=['GET'])
def get_sessions():
    """Get all sessions"""
    user = session.get('user')
    if not user or user.get('role') != 'tutor':
        return jsonify({'error': 'Unauthorized'}), 403
    return jsonify(SESSIONS)

@app.route('/api/sessions/create', methods=['POST'])
def create_session():
    """Create a new session"""
    user = session.get('user')
    if not user or user.get('role') != 'tutor':
        return jsonify({'error': 'Unauthorized'}), 403
    
    data = request.get_json()
    new_session = {
        'id': max([s['id'] for s in SESSIONS]) + 1 if SESSIONS else 1,
        'student_id': int(data['student_id']),
        'student_name': data['student_name'],
        'subject': data['subject'],
        'date': data['date'],
        'time': data['time'],
        'duration': data['duration'],
        'status': 'Scheduled',
        'tutor_name': user['name'],
        'location': data['location']
    }
    SESSIONS.append(new_session)
    return jsonify({'success': True, 'session': new_session})

@app.route('/api/sessions/<int:session_id>/reschedule', methods=['PUT'])
def reschedule_session(session_id):
    """Reschedule an existing session"""
    user = session.get('user')
    if not user or user.get('role') != 'tutor':
        return jsonify({'error': 'Unauthorized'}), 403
    
    data = request.get_json()
    for s in SESSIONS:
        if s['id'] == session_id:
            s['date'] = data['date']
            s['time'] = data['time']
            s['location'] = data.get('location', s['location'])
            return jsonify({'success': True, 'session': s})
    return jsonify({'error': 'Session not found'}), 404

@app.route('/api/sessions/<int:session_id>/cancel', methods=['DELETE'])
def cancel_session(session_id):
    """Cancel a session"""
    user = session.get('user')
    if not user or user.get('role') != 'tutor':
        return jsonify({'error': 'Unauthorized'}), 403
    
    for i, s in enumerate(SESSIONS):
        if s['id'] == session_id:
            s['status'] = 'Cancelled'
            return jsonify({'success': True, 'session': s})
    return jsonify({'error': 'Session not found'}), 404

@app.route('/logout')
def logout():
    """Logout user"""
    session.pop('user', None)
    flash('Đăng xuất thành công!', 'success')
    return redirect(url_for('login'))

# ========== Chrome Incognito Launch Logic ========== #
def open_chrome_incognito(url):
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    if not os.path.exists(chrome_path):
        chrome_path = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    if os.path.exists(chrome_path):
        os.system(f'"{chrome_path}" --incognito {url}')
    else:
        print("Google Chrome not found. Please install Chrome or open the app manually in incognito mode.")

def run_app():
    app.run(debug=True, port=5000)

if __name__ == '__main__':
    threading.Timer(1.5, lambda: open_chrome_incognito("http://127.0.0.1:5000")).start()
    run_app()
