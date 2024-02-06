from roster import student_roster
from classroom_organizer import ClassroomOrganizer, retreive_info
import itertools


def main():
    retreive_info(student_roster)

    # Start organizing the classroom!
    classrom_org = ClassroomOrganizer()
    classrom_org._sort_alphabetically(student_roster)
    print(classrom_org.sorted_names)

    #  Uncomment to make a morning-call

    # print("--- Morning Call ---")
    # for student in classrom_org:
    #     print(student)

    # # Organize the class
    # # There are 5 tables that can seat 2 student each
    # # Uncomment below to see what combination of student can be seated

    # print(classrom_org.get_combinations())

    # Organise afterschool program for Math and Science
    # Tables can seat 4 students each whose favorite subjects are Math and Science
    # Uncomment below to retrieve a list of all 4 combinations of students

    # math_students = classrom_org.get_students_with_subject("Math")
    # science_students = classrom_org.get_students_with_subject("Science")
    # math_students.extend(science_students)
    # math_and_science_combinations = itertools.combinations(math_students, 4)

    # for combo in math_and_science_combinations:
    #     print(combo)


if __name__ == "__main__":
    main()
