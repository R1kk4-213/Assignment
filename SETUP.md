# 🚀 TutorHub - Quick Setup Guide

## Setup trên máy khác (3-5 phút)

### Prerequisites

- Python 3.8+ đã cài đặt
- Git (để clone project)

### Bước 1: Clone project

```bash
git clone <repository-url>
cd Assignment
```

### Bước 2: Tạo virtual environment (Optional nhưng nên làm)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### Bước 3: Cài dependencies

```bash
pip install -r requirements.txt
```

### Bước 4: Cấu hình API Key (cho AI Chat)

1. Lấy free API key: https://makersuite.google.com/app/apikey
2. Tạo file `.env` (hoặc rename `.env.example`):

```
GEMINI_API_KEY=your_api_key_here
```

**LƯU Ý:** Nếu không có API key, app vẫn chạy được nhưng AI Chat sẽ không hoạt động!

### Bước 5: Chạy app

```bash
python app.py
```

### Bước 6: Mở browser

Truy cập: http://127.0.0.1:5000

---

## 🎯 Demo Accounts

### Admin Account

- Username: `admin`
- Password: `admin123`
- Access: Dashboard, Tutor Management, Reports, Configuration

### HCMUT User Account

- Username: `hcmut_user`
- Password: `user123`
- Access: Home page, Program features

---

## ✨ Features để demo

### 1. Landing Page (/)

- Danh sách tutors với avatar, rating
- Smooth animations
- Responsive design

### 2. Login System

- 2 loại login: HCMUT & Admin
- Session management
- Flash messages

### 3. Admin Dashboard (/dashboard)

- Statistics cards với real data
- Monthly trends chart
- Recent activities log
- **Login as admin để xem**

### 4. Tutor Management (/tutor-management)

- Danh sách tutors với search
- Add new tutor (promote từ users)
- Activate/Deactivate tutors
- **Login as admin để xem**

### 5. Configuration (/configuration)

- Cấu hình max students
- Session duration settings
- **Login as admin để xem**

### 6. Reports (/reports)

- Traffic & Enrollment charts
- Filter by period (monthly/quarterly/yearly)
- **Login as admin để xem**

### 7. 🤖 AI Chat Assistant (BONUS FEATURE)

- Click icon robot góc dưới phải
- Hỏi về tutors, ratings, subjects
- Real-time response từ Gemini AI
- **Cần API key để hoạt động**

---

## 🎬 Demo Flow gợi ý

1. **Landing page** → Show tutor cards, smooth scroll
2. **Login as Admin** → Vào dashboard
3. **Dashboard** → Show statistics, charts, activities
4. **Tutor Management** → Add/remove tutors, search
5. **Reports** → Show charts, change periods
6. **AI Chat** → Demo chat với AI assistant
7. **Logout** → Back to landing page

---

## ⚡ Quick Demo (Không setup AI)

Nếu demo gấp và không có thời gian lấy API key:

```bash
# 1. Clone & install
git clone <repo-url>
cd Assignment
pip install Flask Werkzeug

# 2. Comment out AI code trong app.py (hoặc bỏ qua lỗi)
# 3. Chạy
python app.py
```

**Tất cả features khác vẫn hoạt động bình thường!**

---

## 🐛 Troubleshooting

### Port 5000 đã được sử dụng

```bash
# Windows - Tìm process
netstat -ano | findstr :5000
taskkill /PID <process_id> /F

# Hoặc đổi port trong app.py:
app.run(debug=True, port=5001)
```

### Import error

```bash
pip install -r requirements.txt --force-reinstall
```

### AI Chat không hoạt động

- Check file `.env` có đúng format không
- Verify API key tại: https://makersuite.google.com/app/apikey
- Xem console log để debug

---

## 📦 Portable Demo (Không cần cài Python)

### Option 1: Tạo executable với PyInstaller

```bash
pip install pyinstaller
pyinstaller --onefile --add-data "templates;templates" --add-data "static;static" app.py
```

### Option 2: Đóng gói cả venv

1. Zip toàn bộ folder (bao gồm venv)
2. Copy sang máy khác
3. Activate venv và chạy

### Option 3: Docker (Advanced)

```bash
docker build -t tutorhub .
docker run -p 5000:5000 tutorhub
```

---

## 💡 Tips cho điểm 10

1. **Chuẩn bị trước:**

   - Test trên máy demo trước
   - Có sẵn API key trong `.env`
   - Mở sẵn browser tab

2. **Demo flow mượt mà:**

   - Start từ landing page
   - Show từng feature có logic
   - Highlight AI chat ở cuối (wow factor!)

3. **Backup plan:**

   - Screenshot các features (nếu demo fail)
   - Record video demo trước
   - Có API key dự phòng

4. **Giải thích kỹ thuật:**
   - Layer architecture (Presentation → Business → Data)
   - Session management
   - AI integration với Gemini
   - Responsive design

---

## 🎓 Câu hỏi thường gặp

**Q: Có cần database không?**
A: Không! Data được hardcode trong `data/constants.py`. Phù hợp cho demo và assignment.

**Q: AI Chat có cần internet không?**
A: Có, cần internet để gọi Gemini API.

**Q: Có thể demo offline không?**
A: Được! Tất cả features trừ AI Chat hoạt động offline.

**Q: Cần bao nhiêu thời gian setup?**
A: 3-5 phút nếu có Python. 10-15 phút nếu cài từ đầu.

---

## 📞 Contact

Nếu có vấn đề khi setup, check:

- Console log trong browser (F12)
- Terminal output
- File `guide.md` trong project

Good luck! 🍀
