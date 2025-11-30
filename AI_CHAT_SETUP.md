# 🤖 AI Chat Assistant Setup Guide

## Tính năng

- Chat với AI để hỏi về tutors, subjects, ratings
- Giao diện đẹp với floating chat button
- Typing animation và smooth transitions
- Sử dụng Google Gemini AI (FREE & Unlimited)

## Setup trong 2 phút:

### 1. Lấy API Key (1 phút)

1. Truy cập: https://makersuite.google.com/app/apikey
2. Đăng nhập Google account
3. Click "Create API Key"
4. Copy API key

### 2. Cấu hình (30 giây)

1. Mở file `.env` trong project
2. Thay `your_api_key_here` bằng API key vừa lấy:
   ```
   GEMINI_API_KEY=AIzaSy...your_actual_key
   ```

### 3. Chạy app (30 giây)

```bash
python app.py
```

## Demo

1. Mở http://127.0.0.1:5000
2. Click vào icon robot góc dưới phải
3. Hỏi thử:
   - "How many tutors are available?"
   - "Who teaches Math?"
   - "Show me tutors with highest rating"
   - "What is the session duration?"

## Tính năng AI:

✅ Trả lời câu hỏi về tutors
✅ Thống kê số lượng tutors
✅ Tìm tutor theo subject
✅ So sánh rating
✅ Thông tin cấu hình hệ thống

## Demo Tips:

- Hỏi bằng tiếng Anh hoặc tiếng Việt đều được
- AI sẽ trả lời dựa trên data thực của project
- Có typing animation rất smooth
- Response time < 2 giây

## Troubleshooting:

- Nếu lỗi API key: Kiểm tra file `.env`
- Nếu không có response: Check console log
- API free & unlimited, không lo hết quota

## Tech Stack:

- Google Gemini Pro (AI model)
- Flask backend
- Vanilla JavaScript frontend
- Bootstrap styling
