

"""
TutorHub Application - Flask Backend
Layer Architecture:
- Presentation Layer: Routes (Flask routes)
- Business Logic Layer: Service functions
- Data Layer: Hardcoded data
"""

import os
import threading
from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from data import (
    TUTORS,
    USERS,
    STUDENTS,
    SESSIONS,
    PROGRAM_FEATURES,
    PROGRAM_BENEFITS,
    PROGRAM_GALLERY,
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
