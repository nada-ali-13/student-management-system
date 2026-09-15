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