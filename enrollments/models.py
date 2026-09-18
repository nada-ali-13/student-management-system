class Enrollment:
    def __init__(
        self,
        enrollment_id,
        student_id,
        course_id,
        paid
    ):
        self.id = enrollment_id
        self.student_id = student_id
        self.course_id = course_id
        self.paid = paid

    def to_dict(self):
        return {
            "id": self.id,
            "student_id": self.student_id,
            "course_id": self.course_id,
            "paid": self.paid
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id"],
            data["student_id"],
            data["course_id"],
            data["paid"],)