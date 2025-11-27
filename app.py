"""
TutorHub Application - Flask Backend
Layer Architecture:
- Presentation Layer: Routes (Flask routes)
- Business Logic Layer: Service functions
- Data Layer: Hardcoded data
"""

from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import datetime
from collections import defaultdict
import json
import os

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

# Data persistence files
ACTIVITIES_FILE = 'data/activities.json'
TUTORS_FILE = 'data/tutors.json'
CONFIG_FILE = 'data/config.json'

# Default configuration
DEFAULT_CONFIG = {
    'max_students': 10,
    'session_duration': 90
}

# Helper functions for data persistence
def load_activities():
    """Load activities from JSON file"""
    if os.path.exists(ACTIVITIES_FILE):
        try:
            with open(ACTIVITIES_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return list(RECENT_ACTIVITIES)
    return list(RECENT_ACTIVITIES)

def save_activities(activities):
    """Save activities to JSON file"""
    try:
        os.makedirs('data', exist_ok=True)
        with open(ACTIVITIES_FILE, 'w', encoding='utf-8') as f:
            json.dump(activities, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Error saving activities: {e}")

def load_tutors():
    """Load tutors from JSON file"""
    if os.path.exists(TUTORS_FILE):
        try:
            with open(TUTORS_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return list(TUTORS)
    return list(TUTORS)

def save_tutors(tutors):
    """Save tutors to JSON file"""
    try:
        os.makedirs('data', exist_ok=True)
        with open(TUTORS_FILE, 'w', encoding='utf-8') as f:
            json.dump(tutors, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Error saving tutors: {e}")

def add_activity(action, description):
    """Add new activity and persist to file"""
    activities = load_activities()
    new_activity = {
        'action': action,
        'description': description,
        'time': datetime.now().strftime('%H:%M'),
        'date': datetime.now().strftime('%Y-%m-%d')
    }
    activities.insert(0, new_activity)
    # Keep only last 20 activities
    if len(activities) > 20:
        activities = activities[:20]
    save_activities(activities)
    return activities

def load_config():
    """Load configuration from JSON file"""
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return DEFAULT_CONFIG.copy()
    return DEFAULT_CONFIG.copy()

def save_config(config):
    """Save configuration to JSON file"""
    try:
        os.makedirs('data', exist_ok=True)
        with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
            json.dump(config, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Error saving config: {e}")

# Initialize data from files on startup
try:
    TUTORS.clear()
    TUTORS.extend(load_tutors())
    RECENT_ACTIVITIES.clear()
    RECENT_ACTIVITIES.extend(load_activities())
except Exception as e:
    print(f"Error initializing data: {e}")


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
    """Generate reports data from activities and tutors
    Args:
        period: 'monthly', 'quarterly', or 'yearly'
    """
    import random
    from collections import defaultdict
    
    activities = load_activities()
    
    # Define time periods
    if period == 'yearly':
        labels = ['2020', '2021', '2022', '2023', '2024', '2025']
        # Map month to year range
        def get_period_key(date_obj):
            return str(date_obj.year)
    elif period == 'quarterly':
        labels = ['Q1 2024', 'Q2 2024', 'Q3 2024', 'Q4 2024', 'Q1 2025', 'Q2 2025']
        # Map month to quarter
        def get_period_key(date_obj):
            quarter = (date_obj.month - 1) // 3 + 1
            return f'Q{quarter} {date_obj.year}'
    else:  # monthly
        labels = ['January', 'February', 'March', 'April', 'May', 'June']
        month_map = {
            1: 'January', 2: 'February', 3: 'March', 
            4: 'April', 5: 'May', 6: 'June',
            7: 'January', 8: 'February', 9: 'March',
            10: 'April', 11: 'May', 12: 'June'
        }
        def get_period_key(date_obj):
            return month_map.get(date_obj.month)
    
    # Initialize data arrays
    page_views = [120, 320, 240, 80, 210, 230][:len(labels)]
    clicks = [80, 180, 110, 60, 150, 160][:len(labels)]
    
    # Extend arrays if needed
    while len(page_views) < len(labels):
        page_views.append(random.randint(100, 300))
        clicks.append(random.randint(50, 200))
    
    # Count activities per period
    period_activity_count = defaultdict(int)
    for activity in activities:
        if 'date' in activity:
            try:
                date_obj = datetime.strptime(activity['date'], '%Y-%m-%d')
                period_name = get_period_key(date_obj)
                if period_name and period_name in labels:
                    period_idx = labels.index(period_name)
                    period_activity_count[period_idx] += 1
            except:
                pass
    
    # Adjust traffic based on activities
    for period_idx, activity_count in period_activity_count.items():
        multiplier = 1 if period == 'monthly' else (3 if period == 'quarterly' else 12)
        page_views[period_idx] += activity_count * (15 * multiplier)
        clicks[period_idx] += activity_count * (8 * multiplier)
    
    # Enrollment Trends - based on tutor additions
    inquiries = []
    enrollments = []
    
    for label in labels:
        # Count tutors added in this period
        tutors_in_period = 0
        for tutor in TUTORS:
            if 'added_date' in tutor:
                try:
                    date_obj = datetime.strptime(tutor['added_date'], '%Y-%m-%d')
                    if get_period_key(date_obj) == label:
                        tutors_in_period += 1
                except:
                    pass
        
        # Generate inquiries and enrollments based on tutor count
        multiplier = 1 if period == 'monthly' else (3 if period == 'quarterly' else 12)
        base_inquiries = (150 + (tutors_in_period * 8)) * multiplier
        base_enrollments = (100 + (tutors_in_period * 5)) * multiplier
        
        # Add some variation
        variation = 10 * multiplier
        inquiries.append(base_inquiries + random.randint(-variation, variation * 2))
        enrollments.append(base_enrollments + random.randint(-variation, variation))
    
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
            
            # Save tutors to file
            save_tutors(TUTORS)
            
            # Add activity and save to file
            action = 'activate' if tutor['active'] else 'remove'
            add_activity(action, f'{status.capitalize()} tutor: {tutor["name"]}')
            RECENT_ACTIVITIES.clear()
            RECENT_ACTIVITIES.extend(load_activities())
            
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
    
    # Save tutors to file
    save_tutors(TUTORS)
    
    # Add activity and save to file
    add_activity('add', f'Added new tutor: {user_data.get("name", username)}')
    RECENT_ACTIVITIES.clear()
    RECENT_ACTIVITIES.extend(load_activities())
    
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
    
    config = load_config()
    return render_template('configuration.html', user=user, config=config)

@app.route('/save-configuration', methods=['POST'])
def save_configuration():
    """Save configuration settings"""
    user = session.get('user')
    if not user or user['role'] != 'admin':
        return {'success': False, 'message': 'Unauthorized'}, 403
    
    try:
        max_students = int(request.form.get('maxStudents', 10))
        session_duration = int(request.form.get('sessionDuration', 90))
        
        config = {
            'max_students': max_students,
            'session_duration': session_duration
        }
        
        save_config(config)
        
        # Add activity
        add_activity('update', f'Updated configuration: Max students={max_students}, Session duration={session_duration}min')
        RECENT_ACTIVITIES.clear()
        RECENT_ACTIVITIES.extend(load_activities())
        
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

if __name__ == '__main__':
    app.run(debug=True, port=5000)

