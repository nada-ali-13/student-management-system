class Student:
    def __init__(self, student_id, name, age, email, phone):
        self.id = student_id
        self.name = name
        self.age = age
        self.email = email
        self.phone = phone
        
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "email": self.email,
            "phone": self.phone
        }
    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id"],
            data["name"],
            data["age"],
            data["email"],
            data["phone"]
        )