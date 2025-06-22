# src/models/user.py
class User:
    def __init__(self, user_id, username, password, role):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.role = role # Ví dụ: 'admin', 'organizer', 'student_visitor'

    def to_dict(self):
        # Hàm này giúp chuyển đổi đối tượng User thành dictionary để lưu vào file
        return {
            "user_id": self.user_id,
            "username": self.username,
            "password": self.password,
            "role": self.role
        }

    @classmethod
    def from_dict(cls, data):
        # Hàm này giúp tạo lại đối tượng User từ dictionary đọc từ file
        return cls(data['user_id'], data['username'], data['password'], data['role'])