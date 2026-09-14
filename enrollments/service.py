from config.settings import ENROLLMENTS_FILE
from storage.json_storage import load_data
from enrollments.models import Enrollment

def get_all_enrollments():
    data = load_data(ENROLLMENTS_FILE)

    return [
        Enrollment.from_dict(enrollment)
        for enrollment in data
    ]
