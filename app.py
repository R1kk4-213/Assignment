"""
TutorHub Application - Flask Backend
Layer Architecture:
- Presentation Layer: Routes (Flask routes)
- Business Logic Layer: Service functions
- Data Layer: Hardcoded data
"""

from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from datetime import datetime
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

from data import (
    TUTORS,
    USERS,
    PROGRAM_FEATURES,
    PROGRAM_BENEFITS,
    PROGRAM_GALLERY,
    RECENT_ACTIVITIES,
)

app = Flask(__name__)
app.secret_key = 'tutorhub_secret_key_2025'  # For session management

# Configure Gemini API
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY', 'YOUR_API_KEY_HERE')
genai.configure(api_key=GEMINI_API_KEY)

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
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password!', 'error')
    
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
            flash('Invalid username or password!', 'error')
    
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

@app.route('/api/chat', methods=['POST'])
def chat():
    """AI Chat endpoint using Gemini"""
    try:
        data = request.get_json()
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({'success': False, 'error': 'No message provided'}), 400
        
        # Create context about tutors
        tutors_info = []
        for tutor in TUTORS:
            status = "active" if tutor.get('active', True) else "inactive"
            tutors_info.append(
                f"- {tutor['name']}: {tutor['title']}, teaches {tutor['subject']}, "
                f"rating {tutor['rating']}/5.0, status: {status}"
            )
        
        context = f"""You are an AI assistant for TutorHub, a tutor management system at HCMUT.

Available tutors:
{chr(10).join(tutors_info)}

System configuration:
- Max students per session: {CONFIG['max_students']}
- Session duration: {CONFIG['session_duration']} minutes

Answer user questions about tutors, subjects, ratings, and system information. 
Be helpful, friendly, and concise. If asked about specific tutors, provide their details.
Use emojis occasionally to be friendly. Keep responses under 100 words."""

        # Call Gemini API - using gemini-2.0-flash (latest fast model)
        model = genai.GenerativeModel('gemini-2.0-flash')
        response = model.generate_content(f"{context}\n\nUser question: {user_message}")
        
        ai_response = response.text
        
        return jsonify({
            'success': True,
            'response': ai_response
        })
        
    except Exception as e:
        print(f"Chat error: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Failed to get AI response. Please check API key configuration.'
        }), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)

