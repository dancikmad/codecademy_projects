import itertools
from roster import student_roster


class ClassroomOrganizer:
    def __init__(self):
        self.sorted_names = self._sort_alphabetically(student_roster)

    def _sort_alphabetically(self, students):
        names = []
        for student_info in students:
            name = student_info["name"]
            names.append(name)

        return sorted(names)

    def get_students_with_subject(self, subject):
        selected_students = []
        for student in student_roster:
            if student["favorite_subject"] == subject:
                selected_students.append((student["name"], subject))

        return selected_students

    # Implement an iter protocol
    def __iter__(self):
        self.index = 0

        return self

    def __next__(self):
        if self.index < len(self.sorted_names):
            student_name = self.sorted_names[self.index]
            self.index += 1
            return student_name
        else:
            raise StopIteration

    def get_combinations(self):
        """
        Function that performs combinations for 5 tables that can seat 2 student each

        Returns:
        A list of all tuple combinations of 2 students that can be seated at each table.
        """
        combine_2_students = list(itertools.combinations((self.sorted_names), 2))

        return combine_2_students


def retreive_info(students):
    """
    A function that creates an iterator for the students argument
    and prints out each student's information.
    """
    students_iterator = iter(students)

    print("The information of each student on the register.")
    for _ in range(len(students)):
        print(students_iterator.__next__())
