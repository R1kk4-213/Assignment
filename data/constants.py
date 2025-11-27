"""
Static datasets used across the TutorHub application.
Separating these structures keeps `app.py` focused on routing and logic.
"""

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
    },
    'quan': {
        'username': 'quan',
        'password': 'quan123',
        'email': 'tutor01@hcmut.edu.vn',
        'role': 'tutor',
        'name': 'Nguyễn Văn A'
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

# Students data
STUDENTS = [
    {
        'id': 1,
        'name': 'Nguyễn Hoài Nam',
        'student_id': '2211234',
        'email': 'hoainam@hcmut.edu.vn',
        'phone': '0901234567',
        'major': 'Computer Science'
    },
    {
        'id': 2,
        'name': 'Trần Thị Mai',
        'student_id': '2211235',
        'email': 'mai.tran@hcmut.edu.vn',
        'phone': '0901234568',
        'major': 'Software Engineering'
    },
    {
        'id': 3,
        'name': 'Lê Văn Bình',
        'student_id': '2211236',
        'email': 'binh.le@hcmut.edu.vn',
        'phone': '0901234569',
        'major': 'Computer Science'
    },
    {
        'id': 4,
        'name': 'Phạm Thị Hương',
        'student_id': '2211237',
        'email': 'huong.pham@hcmut.edu.vn',
        'phone': '0901234570',
        'major': 'Data Science'
    },
    {
        'id': 5,
        'name': 'Hoàng Minh Tuấn',
        'student_id': '2211238',
        'email': 'tuan.hoang@hcmut.edu.vn',
        'phone': '0901234571',
        'major': 'Computer Engineering'
    }
]

# Sessions data (this will be modified in-memory during runtime)
SESSIONS = [
    {
        'id': 1,
        'student_id': 1,
        'student_name': 'Nguyễn Hoài Nam',
        'subject': 'Data Structures and Algorithms',
        'date': '2025-11-28',
        'time': '09:00',
        'duration': '2 hours',
        'status': 'Scheduled',
        'tutor_name': 'Nguyễn Văn A',
        'location': 'Room B4-301'
    },
    {
        'id': 2,
        'student_id': 2,
        'student_name': 'Trần Thị Mai',
        'subject': 'Linear Algebra',
        'date': '2025-11-29',
        'time': '14:00',
        'duration': '1.5 hours',
        'status': 'Scheduled',
        'tutor_name': 'Nguyễn Văn A',
        'location': 'Room B4-302'
    },
    {
        'id': 3,
        'student_id': 3,
        'student_name': 'Lê Văn Bình',
        'subject': 'Calculus 1',
        'date': '2025-11-30',
        'time': '10:00',
        'duration': '2 hours',
        'status': 'Scheduled',
        'tutor_name': 'Nguyễn Văn A',
        'location': 'Room B4-303'
    }
]

