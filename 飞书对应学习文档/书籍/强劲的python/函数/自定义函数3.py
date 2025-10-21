class Student:
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa

    def __repr__(self):
        return f"{self.name}:{self.gpa}"


student_objs = [Student("Tom", "CS", 3.5), Student("Jerry", "CS", 3.9), Student("Mike", "EE", 3.2)]
from operator import attrgetter
print(sorted(student_objs, key=attrgetter("gpa")))
