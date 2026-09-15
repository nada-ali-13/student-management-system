from students.service import (
    add_student,
    get_all_students,
    get_student_by_id,
    update_student,
    delete_student
)
from courses.service import (
    add_course,
    get_all_courses,
    get_course_by_id,
    update_course,
    delete_course
)
from enrollments.service import (
    add_enrollment,
    get_all_enrollments,
    update_payment_status,
    delete_enrollment
)
from reports.generator import (
    generate_student_report,
    generate_course_report
)

def main_menu():
    while True:
        print("\n================================")
        print("       STUDENT MANAGEMENT")
        print("================================")
        print("1. Student Management")
        print("2. Course Management")
        print("3. Enrollment Management")
        print("4. Reports")
        print("0. Exit")
        print("================================")

        choice = input("Choose an option: ")

        if choice == "1":
            student_menu()

        elif choice == "2":
            course_menu()

        elif choice == "3":
            enrollment_menu()

        elif choice == "4":
            reports_menu()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
#______________________________________________________________
#                  STUDENT MANAGEMENT
#______________________________________________________________

def student_menu():
    while True:
        print("\n================================")
        print("       STUDENT MANAGEMENT")
        print("================================")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Search Student")
        print("5. Show All Students")
        print("0. Back")
        print("================================")

        choice = input("Choose an option: ")

        if choice == "1":
            add_student_menu()

        elif choice == "2":
            update_student_menu()

        elif choice == "3":
            delete_student_menu()

        elif choice == "4":
            search_student_menu()

        elif choice == "5":
            show_all_students()

        elif choice == "0":
            break

        else:
            print("Invalid choice.")

def add_student_menu():
    print("\n--- Add Student ---")

    name = input("Name: ")

    age = int(input("Age: "))

    email = input("Email: ")

    phone = input("Phone: ")

    student = add_student(
        name,
        age,
        email,
        phone
    )

    print(f"\nStudent added successfully!")
    print(f"Student ID: {student.id}")

def show_all_students():
    students = get_all_students()

    print("\n--- All Students ---")

    if not students:
        print("No students found.")
        return

    for student in students:
        print(
            f"ID: {student.id} | "
            f"Name: {student.name} | "
            f"Age: {student.age} | "
            f"Email: {student.email}"
        )

def search_student_menu():
    print("\n--- Search Student ---")

    student_id = int(input("Enter student ID: "))

    student = get_student_by_id(student_id)

    if student:
        print(f"\nID: {student.id}")
        print(f"Name: {student.name}")
        print(f"Age: {student.age}")
        print(f"Email: {student.email}")
        print(f"Phone: {student.phone}")

    else:
        print("Student not found.")

def update_student_menu():
    print("\n--- Update Student ---")

    student_id = int(input("Enter student ID: "))

    student = get_student_by_id(student_id)

    if student is None:
        print("Student not found.")
        return

    print("Enter the new data:")

    name = input("Name: ")
    age = int(input("Age: "))
    email = input("Email: ")
    phone = input("Phone: ")

    updated_student = update_student(
        student_id,
        name,
        age,
        email,
        phone
    )

    print(
        f"\nStudent {updated_student.id} "
        f"updated successfully."
    )

def delete_student_menu():
    print("\n--- Delete Student ---")

    student_id = int(input("Enter student ID: "))

    student = get_student_by_id(student_id)

    if student is None:
        print("Student not found.")
        return

    print(f"Student: {student.name}")

    confirmation = input(
        "Are you sure you want to delete this student? (y/n): "
    )

    if confirmation.lower() == "y":

        deleted = delete_student(student_id)

        if deleted:
            print("Student deleted successfully.")

    else:
        print("Deletion cancelled.")


#__________________________________________________________
#                  COURSE MANAGEMENT
#__________________________________________________________

def course_menu():
    while True:
        print("\n================================")
        print("        COURSE MANAGEMENT")
        print("================================")
        print("1. Add Course")
        print("2. Update Course")
        print("3. Delete Course")
        print("4. Search Course")
        print("5. Show All Courses")
        print("0. Back")
        print("================================")

        choice = input("Choose an option: ")

        if choice == "1":
            add_course_menu()

        elif choice == "2":
            update_course_menu()

        elif choice == "3":
            delete_course_menu()

        elif choice == "4":
            search_course_menu()

        elif choice == "5":
            show_all_courses()

        elif choice == "0":
            break

        else:
            print("Invalid choice.")


def add_course_menu():
    print("\n--- Add Course ---")

    name = input("Course name: ")

    description = input("Description: ")

    fees = float(input("Fees: "))

    start_date = input(
        "Start date (YYYY-MM-DD): "
    )

    end_date = input(
        "End date (YYYY-MM-DD): "
    )

    active_input = input(
        "Is the course active? (y/n): "
    )

    active = active_input.lower() == "y"

    course = add_course(
        name,
        description,
        fees,
        start_date,
        end_date,
        active
    )

    print("\nCourse added successfully!")
    print(f"Course ID: {course.id}")

def show_all_courses():
    courses = get_all_courses()

    print("\n--- All Courses ---")

    if not courses:
        print("No courses found.")
        return

    for course in courses:

        status = "Active" if course.active else "Inactive"

        print(
            f"ID: {course.id} | "
            f"Name: {course.name} | "
            f"Fees: {course.fees} | "
            f"Status: {status}"
        )

def search_course_menu():
    print("\n--- Search Course ---")

    course_id = int(input("Enter course ID: "))

    course = get_course_by_id(course_id)

    if course:
        status = "Active" if course.active else "Inactive"

        print(f"\nID: {course.id}")
        print(f"Name: {course.name}")
        print(f"Description: {course.description}")
        print(f"Fees: {course.fees}")
        print(f"Start: {course.start_date}")
        print(f"End: {course.end_date}")
        print(f"Status: {status}")

    else:
        print("Course not found.")

def update_course_menu():
    print("\n--- Update Course ---")

    course_id = int(input("Enter course ID: "))

    course = get_course_by_id(course_id)

    if course is None:
        print("Course not found.")
        return

    name = input("Course name: ")
    description = input("Description: ")
    fees = float(input("Fees: "))

    start_date = input(
        "Start date (YYYY-MM-DD): "
    )

    end_date = input(
        "End date (YYYY-MM-DD): "
    )

    active_input = input(
        "Is the course active? (y/n): "
    )

    active = active_input.lower() == "y"

    update_course(
        course_id,
        name,
        description,
        fees,
        start_date,
        end_date,
        active
    )

    print("Course updated successfully.")


def delete_course_menu():
    print("\n--- Delete Course ---")

    course_id = int(input("Enter course ID: "))

    course = get_course_by_id(course_id)

    if course is None:
        print("Course not found.")
        return

    print(f"Course: {course.name}")

    confirmation = input(
        "Are you sure you want to delete this course? (y/n): "
    )

    if confirmation.lower() == "y":

        deleted = delete_course(course_id)

        if deleted:
            print("Course deleted successfully.")

    else:
        print("Deletion cancelled.")


#___________________________________________________________
#                   ENROLLMENT MANAGEMENT
#___________________________________________________________

def enrollment_menu():
    while True:
        print("\n================================")
        print("     ENROLLMENT MANAGEMENT")
        print("================================")
        print("1. Enroll Student")
        print("2. Update Payment")
        print("3. Cancel Enrollment")
        print("4. Show All Enrollments")
        print("0. Back")
        print("================================")

        choice = input("Choose an option: ")

        if choice == "1":
            add_enrollment_menu()

        elif choice == "2":
            update_payment_menu()

        elif choice == "3":
            delete_enrollment_menu()

        elif choice == "4":
            show_all_enrollments()

        elif choice == "0":
            break

        else:
            print("Invalid choice.")


def add_enrollment_menu():
    print("\n--- Enroll Student ---")

    student_id = int(input("Student ID: "))
    course_id = int(input("Course ID: "))

    paid_input = input(
        "Has the student paid? (y/n): "
    )

    paid = paid_input.lower() == "y"

    enrollment = add_enrollment(
        student_id,
        course_id,
        paid
    )

    print("\nStudent enrolled successfully!")
    print(f"Enrollment ID: {enrollment.id}")


def update_payment_menu():
    print("\n--- Update Payment ---")

    enrollment_id = int(
        input("Enrollment ID: ")
    )

    paid_input = input(
        "Has the student paid? (y/n): "
    )

    paid = paid_input.lower() == "y"

    enrollment = update_payment_status(
        enrollment_id,
        paid
    )

    if enrollment:
        status = "Paid" if enrollment.paid else "Unpaid"

        print(
            f"Payment status updated: {status}"
        )
    else:
        print("Enrollment not found.")

def delete_enrollment_menu():
    print("\n--- Cancel Enrollment ---")

    enrollment_id = int(
        input("Enrollment ID: ")
    )

    enrollment = get_all_enrollments()

    selected = None

    for item in enrollment:
        if item.id == enrollment_id:
            selected = item
            break

    if selected is None:
        print("Enrollment not found.")
        return

    confirmation = input(
        "Are you sure you want to cancel this enrollment? (y/n): "
    )

    if confirmation.lower() == "y":

        deleted = delete_enrollment(
            enrollment_id
        )

        if deleted:
            print(
                "Enrollment cancelled successfully."
            )

    else:
        print("Cancellation cancelled.")


def show_all_enrollments():
    enrollments = get_all_enrollments()

    print("\n--- All Enrollments ---")

    if not enrollments:
        print("No enrollments found.")
        return

    for enrollment in enrollments:

        payment = (
            "Paid"
            if enrollment.paid
            else "Unpaid"
        )

        course = get_course_by_id(
            enrollment.course_id
        )

        student = get_student_by_id(
            enrollment.student_id
        )

        student_name = (
            student.name
            if student
            else "Unknown"
        )

        course_name = (
            course.name
            if course
            else "Unknown"
        )

        print(
            f"ID: {enrollment.id} | "
            f"Student: {student_name} | "
            f"Course: {course_name} | "
            f"Payment: {payment}"
        )



#________________________________________________________
#                      REPORTS
#________________________________________________________

def reports_menu():
    while True:
        print("\n================================")
        print("            REPORTS")
        print("================================")
        print("1. Student Report")
        print("2. Course Report")
        print("0. Back")
        print("================================")

        choice = input("Choose an option: ")

        if choice == "1":
            student_report_menu()

        elif choice == "2":
            course_report_menu()

        elif choice == "0":
            break

        else:
            print("Invalid choice.")

def student_report_menu():
    student_id = int(
        input("Enter student ID: ")
    )

    print()

    print(
        generate_student_report(student_id)
    )

def course_report_menu():
    course_id = int(
        input("Enter course ID: ")
    )

    print()

    print(
        generate_course_report(course_id)
    )



if __name__ == "__main__":
    main_menu()

