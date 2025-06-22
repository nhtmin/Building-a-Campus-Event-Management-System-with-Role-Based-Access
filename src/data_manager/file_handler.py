# src/data_manager/file_handler.py
import json
import os

# Đường dẫn tới thư mục 'data' của bạn (điều chỉnh nếu cấu trúc khác)
# os.path.dirname(os.path.abspath(__file__)) là đường dẫn đến thư mục hiện tại (data_manager)
# ../../data nghĩa là lùi 2 cấp thư mục để đến thư mục gốc của dự án, rồi vào thư mục data
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../data')

def load_data(file_name):
    filepath = os.path.join(DATA_DIR, file_name)
    if not os.path.exists(filepath):
        # Nếu file không tồn tại, trả về danh sách rỗng
        return []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        # Nếu file rỗng hoặc lỗi JSON, trả về danh sách rỗng
        return []
    except FileNotFoundError:
        return [] # Đảm bảo xử lý cả trường hợp file không tìm thấy

def save_data(data, file_name):
    filepath = os.path.join(DATA_DIR, file_name)
    # Tạo thư mục data nếu nó chưa tồn tại (đảm bảo an toàn)
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)