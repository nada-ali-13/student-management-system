from config.settings import COURSES_FILE
from storage.json_storage import load_data, save_data
from courses.models import Course


def get_all_courses():
    data = load_data(COURSES_FILE)

    return [
        Course.from_dict(course)
        for course in data
    ]


def get_course_by_id(course_id):
    courses = get_all_courses()

    for course in courses:
        if course.id == course_id:
            return course

    return None

def add_course(
    name,
    description,
    fees,
    start_date,
    end_date,
    active=True
):
    courses = get_all_courses()

    new_id = max(
        [course.id for course in courses],
        default=0
    ) + 1

    course = Course(
        new_id,
        name,
        description,
        fees,
        start_date,
        end_date,
        active
    )

    courses.append(course)

    save_data(
        COURSES_FILE,
        [course.to_dict() for course in courses]
    )

    return course

def update_course(
    course_id,
    name,
    description,
    fees,
    start_date,
    end_date,
    active
):
    courses = get_all_courses()
from config.settings import COURSES_FILE
from storage.json_storage import load_data, save_data
from courses.models import Course


def get_all_courses():
    data = load_data(COURSES_FILE)

    return [
        Course.from_dict(course)
        for course in data
    ]


def get_course_by_id(course_id):
    courses = get_all_courses()

    for course in courses:
        if course.id == course_id:
            return course

    return None

def add_course(
    name,
    description,
    fees,
    start_date,
    end_date,
    active=True
):
    courses = get_all_courses()

    new_id = max(
        [course.id for course in courses],
        default=0
    ) + 1

    course = Course(
        new_id,
        name,
        description,
        fees,
        start_date,
        end_date,
        active
    )

    courses.append(course)

    save_data(
        COURSES_FILE,
        [course.to_dict() for course in courses]
    )

    return course

def update_course(
    course_id,
    name,
    description,
    fees,
    start_date,
    end_date,
    active
):
    courses = get_all_courses()

    for course in courses:
        if course.id == course_id:
            course.name = name
            course.description = description
            course.fees = fees
            course.start_date = start_date
            course.end_date = end_date
            course.active = active

            save_data(
                COURSES_FILE,
                [course.to_dict() for course in courses]
            )

            return course

    return None

def delete_course(course_id):
    courses = get_all_courses()

    for course in courses:
        if course.id == course_id:
            courses.remove(course)

            save_data(
                COURSES_FILE,
                [course.to_dict() for course in courses]
            )

            return True

    return False
