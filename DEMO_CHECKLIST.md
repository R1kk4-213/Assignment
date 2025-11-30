# ✅ Demo Checklist - TutorHub

## 📋 Trước khi demo

### Chuẩn bị môi trường

- [ ] Python 3.8+ đã cài đặt
- [ ] Clone/Copy project về máy demo
- [ ] Chạy `setup.bat` (Windows) hoặc `setup.sh` (Mac/Linux)
- [ ] Verify app chạy được: `python app.py`
- [ ] Test truy cập: http://127.0.0.1:5000

### Cấu hình AI (Optional nhưng nên có)

- [ ] Lấy Gemini API key: https://makersuite.google.com/app/apikey
- [ ] Copy `.env.example` thành `.env`
- [ ] Paste API key vào file `.env`
- [ ] Restart app và test AI chat

### Test các tính năng

- [ ] Landing page load đúng (tutors hiển thị)
- [ ] Login admin hoạt động (admin/admin123)
- [ ] Dashboard hiển thị charts
- [ ] Tutor Management: Add/Remove tutors
- [ ] Reports: Charts load và filter works
- [ ] Configuration: Save settings
- [ ] AI Chat: Click robot icon, gửi message test

---

## 🎬 Demo Script (Gợi ý 5-7 phút)

### 1. Landing Page (30s)

"Đây là trang chủ TutorHub - hệ thống quản lý gia sư của HCMUT"

- Scroll xem danh sách tutors
- Highlight rating system
- Show smooth animations

### 2. Login System (30s)

"Hệ thống có 2 loại login: HCMUT user và Admin"

- Click Login
- Chọn Admin Login
- Login: admin/admin123

### 3. Admin Dashboard (1 min)

"Dashboard tổng quan với real-time statistics"

- Point out:
  - Total tutors, Active tutors cards
  - Monthly trends chart
  - Recent activities log
- Explain: "Data được tính toán từ danh sách tutors thực tế"

### 4. Tutor Management (1.5 min)

"Quản lý tutors - add, remove, activate/deactivate"

- Search tutor by name
- Click "Add New Tutor" button
  - Search for user in database
  - Promote to tutor
- Show newly added tutor in list
- Toggle status (Activate/Deactivate)
- Explain: "Changes update real-time và ghi vào activity log"

### 5. Reports (1 min)

"Báo cáo thống kê với data visualization"

- Show Traffic chart (Page views, Clicks)
- Show Enrollment chart
- Change period: Monthly → Quarterly → Yearly
- Charts update smoothly

### 6. Configuration (30s)

"Cấu hình system settings"

- Change max students per session
- Change session duration
- Save settings
- Show flash notification

### 7. 🤖 AI Chat Assistant (1-2 min) - WOW MOMENT!

"Tính năng bonus: AI Chat Assistant với Gemini AI"

- Click robot icon (bottom-right)
- Show chat interface
- Ask questions:
  - "How many tutors are available?"
  - "Who teaches Mathematics?"
  - "Show me tutors with highest rating"
  - "What's the session duration?"
- Highlight:
  - Real-time response
  - Context-aware (biết data trong system)
  - Smooth typing animation
  - Professional UI

### 8. Wrap Up (30s)

"Tổng kết technical highlights:"

- ✅ Layer Architecture (Presentation → Business → Data)
- ✅ Session management with Flask
- ✅ Bootstrap responsive design
- ✅ AI integration với Google Gemini
- ✅ Real-time updates
- ✅ Hardcoded data (no database) - MVP approach

---

## 💡 Demo Tips

### Nếu gặp vấn đề:

1. **App không start**:

   - Check port 5000 có bị chiếm không
   - Đổi port: `app.run(port=5001)` trong app.py

2. **AI Chat lỗi**:

   - Say: "AI feature cần API key, demo các features khác trước"
   - Skip AI chat, showcase các features còn lại
   - Backup: Có screenshot AI chat works

3. **Import error**:
   - Quick fix: `pip install Flask Werkzeug`
   - Continue demo với basic features

### Highlight khi demo:

- ✨ Smooth animations và transitions
- ✨ Professional UI/UX design
- ✨ Real-time updates (activities log)
- ✨ Interactive charts
- ✨ AI integration (wow factor)
- ✨ Clean architecture

### Câu hỏi thường gặp:

**Q: Tại sao không dùng database?**
A: "MVP approach - focus vào complete flow và features. Data hardcoded để dễ demo và deploy. Production sẽ integrate database."

**Q: AI Chat hoạt động thế nào?**
A: "Sử dụng Google Gemini Pro API. App gửi context về tutors và user question, AI generate response based on real data trong system."

**Q: Responsive không?**
A: "Có! Dùng Bootstrap 5 responsive grid. Demo trên mobile view." (Press F12 → Toggle device toolbar)

**Q: Deploy thế nào?**
A: "Rất đơn giản - chỉ cần Python và pip install. Có sẵn setup script cho Windows/Mac/Linux. Setup mất 3-5 phút."

---

## 🎯 Điểm cộng khi demo

1. **Show code structure** (briefly)

   - Layer architecture trong app.py
   - Data constants
   - Template inheritance

2. **Explain technical decisions**

   - Tại sao chọn Flask (lightweight, flexible)
   - Tại sao hardcode data (MVP, easy demo)
   - Tại sao Gemini (free, powerful, easy integrate)

3. **Show responsive design**

   - F12 → Device toolbar
   - Test mobile view
   - Show chat widget mobile responsive

4. **Backup materials**
   - Screenshots của features
   - Video recording (nếu có)
   - Code snippets

---

## 📞 Emergency Contacts

- Setup guide: SETUP.md
- AI guide: AI_CHAT_SETUP.md
- Code guide: guide.md
- Main docs: README.md

---

## ⏱️ Time Breakdown

- Landing page: 30s
- Login: 30s
- Dashboard: 1 min
- Tutor Management: 1.5 min
- Reports: 1 min
- Configuration: 30s
- AI Chat: 1-2 min
- Q&A: 1-2 min

**Total: ~7-10 minutes**

---

Good luck! 🍀 You got this! 💪
