"""
TutorHub Application - Flask Backend
Layer Architecture:
- Presentation Layer: Routes (Flask routes)
- Business Logic Layer: Service functions
- Data Layer: Hardcoded data
"""

from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'tutorhub_secret_key_2025'  # For session management

# ==================== DATA LAYER ====================
# Hardcoded data - No database needed

TUTORS = [
    {
        'id': 1,
        'name': 'Nguyễn Văn A',
        'title': 'Assoc. Prof',
        'subject': 'Data Structures and Algorithms',
        'rating': 4.5,
        'image': 'https://via.placeholder.com/150?text=NAK'
    },
    {
        'id': 2,
        'name': 'Nguyễn Văn B',
        'title': None,
        'subject': 'Calculus 1',
        'rating': 3,
        'image': 'https://via.placeholder.com/150?text=NHN'
    },
    {
        'id': 3,
        'name': 'Nguyễn Văn C',
        'title': None,
        'subject': 'Linear Algebra',
        'rating': 4,
        'image': 'https://via.placeholder.com/150?text=TLA'
    }
]

USERS = {
    'hoainam123': {
        'username': 'hoainam123',
        'password': 'password123',
        'email': 'hoainam@hcmut.edu.vn',
        'role': 'student',
        'name': 'Nguyễn Hoài Nam'
    },
    'admin': {
        'username': 'admin',
        'password': 'admin123',
        'email': 'admin@hcmut.edu.vn',
        'role': 'admin',
        'name': 'Administrator'
    }
}

PROGRAM_FEATURES = [
    {
        'icon': 'bi-person-badge',
        'title': 'Comprehensive Profiles',
        'description': 'Maintain detailed tutor and student records for quick reference.'
    },
    {
        'icon': 'bi-cpu',
        'title': 'Efficient Matching',
        'description': 'Match students with the best tutors based on needs and availability.'
    },
    {
        'icon': 'bi-calendar-week',
        'title': 'Session Management',
        'description': 'Schedule, monitor, and review every learning session in one place.'
    },
    {
        'icon': 'bi-clock-history',
        'title': 'Smart Scheduling',
        'description': 'Automated reminders help minimize conflicts and missed appointments.'
    },
    {
        'icon': 'bi-chat-dots',
        'title': 'Feedback & Improvement',
        'description': 'Collect feedback to continuously improve tutor quality and student outcomes.'
    },
    {
        'icon': 'bi-graph-up-arrow',
        'title': 'Performance Analytics',
        'description': 'Track program KPIs to support data-driven decisions.'
    }
]

PROGRAM_BENEFITS = [
    'Enhanced support system for students navigating coursework.',
    'Empowered faculty and senior students to contribute meaningfully.',
    'Streamlined administrative tasks for program organizers.',
    'Better resource allocation through data insights.',
    'Increased engagement and satisfaction across the community.'
]

PROGRAM_GALLERY = [
    {
        'caption': 'Campus Welcome',
        'image': 'img/hcmut/campus.png'
    },
    {
        'caption': 'Tutor & Student Dialogue',
        'image': 'img/hcmut/campus.png'
    },
    {
        'caption': 'Graduation Moments',
        'image': 'img/hcmut/campus.png'
    },
    {
        'caption': 'Outdoor Study',
        'image': 'img/hcmut/campus.png'
    },
    {
        'caption': 'Hands-on Workshop',
        'image': 'img/hcmut/campus.png'
    },
    {
        'caption': 'Community Events',
        'image': 'img/hcmut/campus.png'
    }
]

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

if __name__ == '__main__':
    app.run(debug=True, port=5000)

