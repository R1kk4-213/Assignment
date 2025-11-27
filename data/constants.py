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

TUTOR_PROFILE = {
    'id': '2352778',
    'name': 'Nguyen Hoai Nam',
    'email': 'nam.strong@hcmut.edu.vn',
    'faculty': 'Faculty of Computer Science and Engineering',
    'role': 'Tutor',
    'status': 'Active',
    'faculty_department': 'Computer Science and Engineering',
    'profile_picture': 'img/asset/avatar.png',
    'biography': (
        'As a dedicated software engineering student and a peer tutor at HCMUT, '
        'I am deeply passionate about fostering a collaborative learning environment. '
        'My academic journey has equipped me with strong problem-solving skills and a solid '
        'foundation in computer science principles. I specialize in machine learning, computer '
        'vision and data algorithms. Through the Tutor/Mentor program, I aim to share my knowledge, '
        'assist fellow students in overcoming academic challenges, and inspire a greater interest in '
        'technology. I believe in a patient and engaging approach to teaching, tailoring my methods to '
        'suit individual learning styles. Beyond academics, I enjoy coding personal projects, exploring '
        'new technologies, and participating in university hackathons. I am committed to continuous '
        'improvement and making a positive impact within the HCMUT community.'
    ),
    'phone_number': '+84901234567',
    'areas_of_expertise': [
        'Artificial Intelligence',
        'Machine Learning',
        'Natural Language Processing',
        'Computer Vision',
        'Data Structures'
    ]
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

