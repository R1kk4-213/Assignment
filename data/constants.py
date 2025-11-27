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


RESOURCES = [
    {
        'id': 1,
        'title': 'Advanced Programming - Chapter 1',
        'tutor': 'Quan Thanh Tho',
        'file_type': 'Powerpoint',
        'size': '3.6 MB',
        'viewed': 20,
        'thumbnail': 'img/materials/advprog.png',
        'keywords': ['Advanced Programming']
    },
    {
        'id': 2,
        'title': 'Probability & Statistics - Chapter 4',
        'tutor': 'Phan Thi Huong',
        'file_type': 'PDF',
        'size': '2.8 MB',
        'viewed': 42,
        'thumbnail': 'img/materials/prob_stats.png',
        'keywords': ['Probability & Statistics']
    },
    {
        'id': 3,
        'title': 'Database Systems - Chapter 3',
        'tutor': 'Vo Thi Ngoc Chau',
        'file_type': 'PDF',
        'size': '5.1 MB',
        'viewed': 34,
        'thumbnail': 'img/materials/database.png',
        'keywords': ['Database Systems']
    },
    {
        'id': 4,
        'title': 'Data Structures and Algorithms - Chapter 1',
        'tutor': 'Nguyen Hua Phung',
        'file_type': 'PDF',
        'size': '1.2 MB',
        'viewed': 10,
        'thumbnail': 'img/materials/dsa.png',
        'keywords': ['Data Structures and Algorithms'],
        'course': 'Data Structure and Algorithms',
        'released_date': '02/10/2025'
    },
    {
        'id': 5,
        'title': 'Computer Networks - Chapter 1',
        'tutor': 'Nguyen Le Duy Lai',
        'file_type': 'PDF',
        'size': '2.0 MB',
        'viewed': 15,
        'thumbnail': 'img/materials/com_network.png',
        'keywords': ['Computer Networks']
    }
]

KEYWORDS = [
    'Probability & Statistics',
    'Advanced Programming',
    'Database Systems',
    'DSA',
    'Computer Networks'
]

FILE_TYPES = [
    'PDF',
    'Word',
    'Powerpoint'
]

