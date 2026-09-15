def get_all_students():
    data = load_data(STUDENTS_FILE)

    return [
        Student.from_dict(student)
        for student in data
    ]
    
def add_student(name, age, email, phone):

    validate_name(name)
    validate_age(age)
    validate_email(email)
    validate_phone(phone)

    students = get_all_students()

    new_id = max(
        [student.id for student in students],
        default=0
    ) + 1

    student = Student(
        new_id,
        name,
        age,
        email,
        phone
    )

    students.append(student)

    save_data(
        STUDENTS_FILE,
        [student.to_dict() for student in students]
    )

    return student


def get_student_by_id(student_id):
    students = get_all_students()

    for student in students:
        if student.id == student_id:
            return student

    return None


def update_student(student_id, name, age, email, phone):
    students = get_all_students()

    for student in students:
        if student.id == student_id:
            student.name = name
            student.age = age
            student.email = email
            student.phone = phone

            save_data(
                STUDENTS_FILE,
                [student.to_dict() for student in students]
            )

            return student

    return None