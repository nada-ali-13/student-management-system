from enrollments.service import get_student_enrollments
from courses.service import get_course_by_id
from enrollments.service import get_course_enrollments
from students.service import get_student_by_id


def generate_student_report(student_id):
    student = get_student_by_id(student_id)

    if student is None:
        return "Student not found"

    enrollments = get_student_enrollments(student_id)

    report = []

    report.append("================================")
    report.append("        STUDENT REPORT")
    report.append("================================")
    report.append(f"ID: {student.id}")
    report.append(f"Name: {student.name}")
    report.append(f"Age: {student.age}")
    report.append(f"Email: {student.email}")
    report.append(f"Phone: {student.phone}")
    report.append(f"Number of courses: {len(enrollments)}")
    report.append("")

    if not enrollments:
        report.append("No courses enrolled.")
    else:
        report.append("Courses:")

        for enrollment in enrollments:
            course = get_course_by_id(enrollment.course_id)

            if course:
                payment = "Paid" if enrollment.paid else "Unpaid"

                report.append(
                    f"- {course.name}"
                )
                report.append(
                    f"  Start: {course.start_date}"
                )
                report.append(
                    f"  End: {course.end_date}"
                )
                report.append(
                    f"  Payment: {payment}"
                )
                report.append("")

    return "\n".join(report)


def generate_course_report(course_id):
    course = get_course_by_id(course_id)

    if course is None:
        return "Course not found"

    enrollments = get_course_enrollments(course_id)

    status = "Active" if course.active else "Inactive"

    report = []

    report.append("================================")
    report.append("         COURSE REPORT")
    report.append("================================")
    report.append(f"ID: {course.id}")
    report.append(f"Name: {course.name}")
    report.append(f"Description: {course.description}")
    report.append(f"Fees: {course.fees}")
    report.append(f"Start Date: {course.start_date}")
    report.append(f"End Date: {course.end_date}")
    report.append(f"Status: {status}")
    report.append(f"Students enrolled: {len(enrollments)}")
    report.append("")

    if not enrollments:
        report.append("No students enrolled.")
    else:
        report.append("Students:")

        for enrollment in enrollments:
            student = get_student_by_id(enrollment.student_id)

            if student:
                payment = "Paid" if enrollment.paid else "Unpaid"

                report.append(
                    f"- {student.name} ({payment})"
                )

    return "\n".join(report)