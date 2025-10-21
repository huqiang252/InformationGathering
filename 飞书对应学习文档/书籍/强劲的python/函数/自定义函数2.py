student_rows = [
    ("Joe Smith", "physics", 3.7),
    ("Jane Jones", "chemistry", 3.8),
    ("Zoe Fox", "literature", 3.4),
]

from operator import itemgetter

print(max(student_rows, key=itemgetter(2)))
print(sorted(student_rows, key=itemgetter(1)))
