student_joe = {'gpa': 3.7, 'major': 'physics', 'name': 'Joe Smith'}
student_jane = {'gpa': 3.8, 'major': 'chemistry', 'name': 'Jane Jones'}
student_zoe = {'gpa': 3.4, 'major': 'literature', 'name': 'Zoe Fox'}
students = [student_joe, student_jane, student_zoe]

# 1.键函数老方法
def get_gpa(who):
    return who['gpa']

print(sorted(students, key=get_gpa))

# 2.使用itemgetter (和上面效果等价)
from operator import itemgetter
print(sorted(students, key=itemgetter('gpa')))




