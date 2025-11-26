# TutorHub - HCMUT

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

Ứng dụng mặc định chạy ở `http://localhost:5000`. Khi thay đổi mã nguồn, chỉ cần lưu file và Flask sẽ tự reload (ở chế độ `debug=True`).

## 3. Quy tắc code (từ `guide.md`)

- Backend sử dụng Flask, frontend dùng Bootstrap.
- Áp dụng Layer Architecture: routes (presentation) -> services (logic) -> data (hardcode).
- Mục tiêu là MVP: ưu tiên chạy được toàn bộ flow, không cần DB.
- CRUD/logic đơn giản, dữ liệu cần thiết được hardcode.
- Toàn bộ xử lý backend đặt trong `app.py`, mỗi route tự xử lý logic nhỏ gọn.
- Tài nguyên tĩnh (`static/`) chứa ảnh, CSS, JS.

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


