# 🎓 TutorHub - HCMUT Tutor Management System

A modern web application for managing tutors, students, and tutoring sessions at Ho Chi Minh City University of Technology.

## ✨ Features

- 🏠 **Landing Page** - Browse available tutors with ratings
- 🔐 **Dual Login System** - HCMUT & Admin authentication
- 📊 **Admin Dashboard** - Statistics, charts, and activity monitoring
- 👨‍🏫 **Tutor Management** - Add, remove, and manage tutor profiles
- 📈 **Reports & Analytics** - Traffic and enrollment visualization
- ⚙️ **Configuration** - System settings management
- 🤖 **AI Chat Assistant** - AI-powered tutor inquiry system (BONUS)

## 🚀 Quick Setup

### Windows (Easy Mode)

```bash
setup.bat
run.bat
```

### Mac/Linux

```bash
chmod +x setup.sh
./setup.sh
python app.py
```

### Manual Setup

## 1. Thiết lập môi trường ảo

```bash
# Tạo venv
python -m venv venv

# Kích hoạt
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

## 2. Cài đặt phụ thuộc & chạy ứng dụng

```bash
pip install -r requirements.txt
python app.py
```

## 🌐 Access the Application

Open browser: **http://127.0.0.1:5000**

### Demo Accounts

- **Admin**: `admin` / `admin123` (Full access)
- **User**: `hcmut_user` / `user123` (Limited access)

## 🤖 AI Chat Setup (Optional)

1. Get free API key: https://makersuite.google.com/app/apikey
2. Copy `.env.example` to `.env`
3. Add your API key to `.env`
4. Restart app

See `AI_CHAT_SETUP.md` for details.

## 📁 Project Structure

Ứng dụng mặc định chạy ở `http://localhost:5000`. Khi thay đổi mã nguồn, chỉ cần lưu file và Flask sẽ tự reload (ở chế độ `debug=True`).

## 3. Quy tắc code (từ `guide.md`)

- Backend sử dụng Flask, frontend dùng Bootstrap
- Layer Architecture: routes (presentation) → services (logic) → data (hardcode)
- MVP approach: Ưu tiên chạy được toàn bộ flow, không cần DB
- Data hardcoded trong `data/constants.py`

## 📚 Documentation

- **SETUP.md** - Chi tiết setup cho máy khác
- **AI_CHAT_SETUP.md** - Hướng dẫn AI Chat
- **guide.md** - Quy tắc development

## 🐛 Troubleshooting

**Port 5000 bị chiếm:**

```bash
# Windows
netstat -ano | findstr :5000
taskkill /PID <id> /F
```

**AI Chat không hoạt động:**

- Check file `.env` có API key đúng
- Cần internet để gọi Gemini API

---

📝 **Note**: Dự án có thể chạy trên bất kỳ máy nào có Python 3.8+  
🚀 **Demo Ready**: Setup chỉ mất 3-5 phút

## 4. Cấu trúc thư mục chính

```
Assignment/
├── app.py                # Ứng dụng Flask và định nghĩa route
├── data/                 # Tập tin dữ liệu hardcode dùng chung
│   ├── __init__.py
│   └── constants.py
├── requirements.txt      # Danh sách phụ thuộc Python
├── static/               # Tài nguyên tĩnh (css, js, hình ảnh)
│   ├── css/
│   ├── js/
│   └── img/
├── templates/            # Giao diện Jinja2 (index, login, home, ...)
├── guide.md              # Tài liệu hướng dẫn quy tắc code
└── README.md             # Tài liệu này
```
