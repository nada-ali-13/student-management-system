from config.settings import ENROLLMENTS_FILE
from storage.json_storage import load_data , save_data
from enrollments.models import Enrollment
from students.service import get_student_by_id
from courses.service import get_course_by_id


def get_all_enrollments():
    data = load_data(ENROLLMENTS_FILE)

    return [
        Enrollment.from_dict(enrollment)
        for enrollment in data
    ]
def get_enrollment_by_id(enrollment_id):
    enrollments = get_all_enrollments()

    for enrollment in enrollments:
        if enrollment.id == enrollment_id:
            return enrollment

    return None
def add_enrollment(
    student_id,
    course_id,
    paid=False
):
    student = get_student_by_id(student_id)

    if student is None:
        raise ValueError("Student not found")

    course = get_course_by_id(course_id)

    if course is None:
        raise ValueError("Course not found")

    if not course.active:
        raise ValueError("Course is not active")

    enrollments = get_all_enrollments()

    for enrollment in enrollments:
        if (
            enrollment.student_id == student_id
            and enrollment.course_id == course_id
        ):
            raise ValueError(
                "Student is already enrolled in this course"
            )

    new_id = max(
        [enrollment.id for enrollment in enrollments],
        default=0
    ) + 1

    enrollment = Enrollment(
        new_id,
        student_id,
        course_id,
        paid
    )

    enrollments.append(enrollment)

    save_data(
        ENROLLMENTS_FILE,
        [enrollment.to_dict() for enrollment in enrollments]
    )

    return enrollment
def get_student_enrollments(student_id):
    enrollments = get_all_enrollments()

    return [
        enrollment
        for enrollment in enrollments
        if enrollment.student_id == student_id
    ]

def get_course_enrollments(course_id):
    enrollments = get_all_enrollments()

    return [
        enrollment
        for enrollment in enrollments
        if enrollment.course_id == course_id
    ]


def update_payment_status(enrollment_id, paid):
    enrollments = get_all_enrollments()

    for enrollment in enrollments:
        if enrollment.id == enrollment_id:
            enrollment.paid = paid

            save_data(
                ENROLLMENTS_FILE,
                [enrollment.to_dict() for enrollment in enrollments]
            )


def delete_enrollment(enrollment_id):
    enrollments = get_all_enrollments()

    for enrollment in enrollments:
        if enrollment.id == enrollment_id:
            enrollments.remove(enrollment)

            save_data(
                ENROLLMENTS_FILE,
                [enrollment.to_dict() for enrollment in enrollments]
            )

            return True
