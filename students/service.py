def get_all_students():
    data = load_data(STUDENTS_FILE)

    return [
        Student.from_dict(student)
        for student in data
    ]