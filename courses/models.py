class Course:
    def __init__(
        self,
        course_id,
        name,
        description,
        fees,
        start_date,
        end_date,
        active
    ):
        self.id = course_id
        self.name = name
        self.description = description
        self.fees = fees
        self.start_date = start_date
        self.end_date = end_date
        self.active = active

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "fees": self.fees,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "active": self.active
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id"],
            data["name"],
            data["description"],
            data["fees"],
            data["start_date"],
            data["end_date"],
            data["active"]
        )
