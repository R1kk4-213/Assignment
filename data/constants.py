"""
Static datasets used across the TutorHub application.
Separating these structures keeps `app.py` focused on routing and logic.
"""

TUTORS = [
    {'id': 1, 'name': 'Kim Ri Cha', 'title': 'Assoc. Prof', 'subject': 'Data Structures and Algorithms', 'rating': 4.5, 'image': 'https://via.placeholder.com/150?text=NAK', 'active': True, 'added_date': '2025-01-15'},
    {'id': 2, 'name': 'Park ky Chou', 'title': None, 'subject': 'Calculus 1', 'rating': 3, 'image': 'https://via.placeholder.com/150?text=NHN', 'active': True, 'added_date': '2025-01-20'},
    {'id': 3, 'name': 'Nguyễn Văn C', 'title': None, 'subject': 'Linear Algebra', 'rating': 4, 'image': 'https://via.placeholder.com/150?text=TLA', 'active': True, 'added_date': '2025-02-05'},
    {'id': 4, 'name': 'Trần Thị D', 'title': 'Dr.', 'subject': 'Physics 1', 'rating': 4.8, 'image': 'https://via.placeholder.com/150?text=TTD', 'active': True, 'added_date': '2025-02-10'},
    {'id': 5, 'name': 'Lê Văn E', 'title': None, 'subject': 'Chemistry', 'rating': 4.2, 'image': 'https://via.placeholder.com/150?text=LVE', 'active': True, 'added_date': '2025-02-18'},
    {'id': 6, 'name': 'Phạm Thị F', 'title': 'Prof.', 'subject': 'Programming Fundamentals', 'rating': 4.9, 'image': 'https://via.placeholder.com/150?text=PTF', 'active': True, 'added_date': '2025-02-25'},
    {'id': 7, 'name': 'Hoàng Văn G', 'title': None, 'subject': 'Discrete Mathematics', 'rating': 3.8, 'image': 'https://via.placeholder.com/150?text=HVG', 'active': True, 'added_date': '2025-03-01'},
    {'id': 8, 'name': 'Đặng Thị H', 'title': 'Assoc. Prof', 'subject': 'Database Systems', 'rating': 4.6, 'image': 'https://via.placeholder.com/150?text=DTH', 'active': True, 'added_date': '2025-03-05'},
    {'id': 9, 'name': 'Vũ Văn I', 'title': None, 'subject': 'Computer Networks', 'rating': 4.1, 'image': 'https://via.placeholder.com/150?text=VVI', 'active': True, 'added_date': '2025-03-12'},
    {'id': 10, 'name': 'Bùi Thị K', 'title': 'Dr.', 'subject': 'Operating Systems', 'rating': 4.7, 'image': 'https://via.placeholder.com/150?text=BTK', 'active': True, 'added_date': '2025-03-18'},
    {'id': 11, 'name': 'Ngô Văn L', 'title': None, 'subject': 'Software Engineering', 'rating': 4.0, 'image': 'https://via.placeholder.com/150?text=NVL', 'active': True, 'added_date': '2025-03-25'},
    {'id': 12, 'name': 'Đinh Thị M', 'title': None, 'subject': 'Web Development', 'rating': 4.4, 'image': 'https://via.placeholder.com/150?text=DTM', 'active': True, 'added_date': '2025-04-02'},
    {'id': 13, 'name': 'Dương Văn N', 'title': 'Prof.', 'subject': 'Machine Learning', 'rating': 4.9, 'image': 'https://via.placeholder.com/150?text=DVN', 'active': True, 'added_date': '2025-04-08'},
    {'id': 14, 'name': 'Mai Thị O', 'title': None, 'subject': 'Artificial Intelligence', 'rating': 4.5, 'image': 'https://via.placeholder.com/150?text=MTO', 'active': True, 'added_date': '2025-04-15'},
    {'id': 15, 'name': 'Tô Văn P', 'title': 'Assoc. Prof', 'subject': 'Data Mining', 'rating': 4.3, 'image': 'https://via.placeholder.com/150?text=TVP', 'active': True, 'added_date': '2025-04-20'},
    {'id': 16, 'name': 'Lý Thị Q', 'title': None, 'subject': 'Computer Graphics', 'rating': 3.9, 'image': 'https://via.placeholder.com/150?text=LTQ', 'active': True, 'added_date': '2025-04-25'},
    {'id': 17, 'name': 'Võ Văn R', 'title': 'Dr.', 'subject': 'Information Security', 'rating': 4.8, 'image': 'https://via.placeholder.com/150?text=VVR', 'active': True, 'added_date': '2025-05-01'},
    {'id': 18, 'name': 'Hồ Thị S', 'title': None, 'subject': 'Mobile App Development', 'rating': 4.2, 'image': 'https://via.placeholder.com/150?text=HTS', 'active': True, 'added_date': '2025-05-05'},
    {'id': 19, 'name': 'Trịnh Văn T', 'title': None, 'subject': 'Cloud Computing', 'rating': 4.6, 'image': 'https://via.placeholder.com/150?text=TVT', 'active': True, 'added_date': '2025-05-10'},
    {'id': 20, 'name': 'Phan Thị U', 'title': 'Prof.', 'subject': 'Big Data Analytics', 'rating': 4.7, 'image': 'https://via.placeholder.com/150?text=PTU', 'active': True, 'added_date': '2025-05-15'},
    {'id': 21, 'name': 'Cao Văn V', 'title': None, 'subject': 'IoT Systems', 'rating': 4.0, 'image': 'https://via.placeholder.com/150?text=CVV', 'active': True, 'added_date': '2025-05-20'},
    {'id': 22, 'name': 'La Thị W', 'title': 'Assoc. Prof', 'subject': 'Robotics', 'rating': 4.4, 'image': 'https://via.placeholder.com/150?text=LTW', 'active': True, 'added_date': '2025-05-22'},
    {'id': 23, 'name': 'Ông Văn X', 'title': None, 'subject': 'Embedded Systems', 'rating': 4.1, 'image': 'https://via.placeholder.com/150?text=OVX', 'active': True, 'added_date': '2025-05-25'},
    {'id': 24, 'name': 'Từ Thị Y', 'title': 'Dr.', 'subject': 'Natural Language Processing', 'rating': 4.8, 'image': 'https://via.placeholder.com/150?text=TTY', 'active': True, 'added_date': '2024-10-15'},
    {'id': 25, 'name': 'Vu Duc Viet Anh', 'title': None, 'subject': 'Calculus', 'rating': 4.5, 'image': 'https://via.placeholder.com/150?text=VDVA', 'active': True, 'added_date': '2025-11-27'},
    {'id': 26, 'name': 'Lê Văn C', 'title': None, 'subject': 'Statistics', 'rating': 3.0, 'image': 'https://via.placeholder.com/150?text=LVC', 'active': True, 'added_date': '2025-04-10'},
    {'id': 27, 'name': 'Trần D', 'title': None, 'subject': 'English', 'rating': 3.5, 'image': 'https://via.placeholder.com/150?text=TD', 'active': False, 'added_date': '2025-03-15'},
    {'id': 28, 'name': 'Nguyễn E', 'title': None, 'subject': 'Biology', 'rating': 4.3, 'image': 'https://via.placeholder.com/150?text=NE', 'active': True, 'added_date': '2024-12-20'},
    {'id': 29, 'name': 'Phạm F', 'title': 'Dr.', 'subject': 'Economics', 'rating': 4.6, 'image': 'https://via.placeholder.com/150?text=PF', 'active': True, 'added_date': '2025-01-25'},
    {'id': 30, 'name': 'Hoàng G', 'title': None, 'subject': 'Business Management', 'rating': 4.2, 'image': 'https://via.placeholder.com/150?text=HG', 'active': True, 'added_date': '2025-02-28'},
    {'id': 31, 'name': 'Đặng H', 'title': 'Prof.', 'subject': 'Marketing', 'rating': 4.7, 'image': 'https://via.placeholder.com/150?text=DH', 'active': True, 'added_date': '2024-11-10'},
    {'id': 32, 'name': 'Vũ I', 'title': None, 'subject': 'Accounting', 'rating': 4.1, 'image': 'https://via.placeholder.com/150?text=VI', 'active': True, 'added_date': '2025-03-20'},
    {'id': 33, 'name': 'Bùi K', 'title': 'Assoc. Prof', 'subject': 'Finance', 'rating': 4.5, 'image': 'https://via.placeholder.com/150?text=BK', 'active': True, 'added_date': '2024-10-05'},
    {'id': 34, 'name': 'Ngô L', 'title': None, 'subject': 'Psychology', 'rating': 4.0, 'image': 'https://via.placeholder.com/150?text=NL', 'active': True, 'added_date': '2025-04-18'},
    {'id': 35, 'name': 'Đinh M', 'title': 'Dr.', 'subject': 'Sociology', 'rating': 4.4, 'image': 'https://via.placeholder.com/150?text=DM', 'active': True, 'added_date': '2024-09-25'},
    {'id': 36, 'name': 'Dương N', 'title': None, 'subject': 'Philosophy', 'rating': 3.8, 'image': 'https://via.placeholder.com/150?text=DN', 'active': True, 'added_date': '2025-05-08'},
    {'id': 37, 'name': 'Vũ Đức Việt Anh', 'title': None, 'subject': 'Advanced Calculus', 'rating': 4.9, 'image': 'https://via.placeholder.com/150?text=VDVA', 'active': True, 'added_date': '2025-11-27'},
    {'id': 38, 'name': 'Nguyễn Hoài Nam', 'title': 'Prof.', 'subject': 'Computer Science', 'rating': 5.0, 'image': 'https://via.placeholder.com/150?text=NHN', 'active': True, 'added_date': '2025-11-27'}
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
    'nguyenB234':{
        'username': 'nguyenB234',
        'password': 'tutor123',
        'email': 'nguyenB@hcmut.edu.vn',
        'role': 'tutor',
        'name': 'Nguyễn Văn B'
    },
    'tuannguyen': {
        'username': 'tuannguyen',
        'password': 'student123',
        'email': 'tuan.nguyen@hcmut.edu.vn',
        'role': 'student',
        'name': 'Nguyễn Văn Tuấn'
    },
    'linhtran': {
        'username': 'linhtran',
        'password': 'student123',
        'email': 'linh.tran@hcmut.edu.vn',
        'role': 'student',
        'name': 'Trần Thị Linh'
    },
    'ducle': {
        'username': 'ducle',
        'password': 'student123',
        'email': 'duc.le@hcmut.edu.vn',
        'role': 'student',
        'name': 'Lê Minh Đức'
    },
    'huongpham': {
        'username': 'huongpham',
        'password': 'student123',
        'email': 'huong.pham@hcmut.edu.vn',
        'role': 'student',
        'name': 'Phạm Thị Hương'
    },
    'quangvo': {
        'username': 'quangvo',
        'password': 'student123',
        'email': 'quang.vo@hcmut.edu.vn',
        'role': 'student',
        'name': 'Võ Đức Quang'
    },
    'thanhhoang': {
        'username': 'thanhhoang',
        'password': 'student123',
        'email': 'thanh.hoang@hcmut.edu.vn',
        'role': 'student',
        'name': 'Hoàng Văn Thành'
    },
    'anhdang': {
        'username': 'anhdang',
        'password': 'student123',
        'email': 'anh.dang@hcmut.edu.vn',
        'role': 'student',
        'name': 'Đặng Tuấn Anh'
    },
    'mynguyen': {
        'username': 'mynguyen',
        'password': 'student123',
        'email': 'my.nguyen@hcmut.edu.vn',
        'role': 'student',
        'name': 'Nguyễn Thị Mỹ'
    },
    'messilun': {
        'username': 'messilun',
        'password': 'goat123',
        'email': 'messi.lun@hcmut.edu.vn',
        'role': 'student',
        'name': 'Messi Lùn'
    },
    'ronaldo': {
        'username': 'ronaldo',
        'password': 'cr7siuu',
        'email': 'ronaldo@hcmut.edu.vn',
        'role': 'student',
        'name': 'Cristiano Ronaldo'
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

RECENT_ACTIVITIES = [
    {'text': 'Tutor added: Vu Duc Viet Anh (Calculus)', 'time': '2 minutes ago', 'timestamp': '2025-11-27 14:30'},
    {'text': 'System config updated: Email notifications', 'time': '1 hour ago', 'timestamp': '2025-11-27 13:30'},
    {'text': 'Tutor review: Le Van C received 3 stars', 'time': '2 hours ago', 'timestamp': '2025-11-27 10:15'},
    {'text': 'Tutor removed: Tran D has been suspended', 'time': '5 hours ago', 'timestamp': '2025-11-27 09:00'}
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

