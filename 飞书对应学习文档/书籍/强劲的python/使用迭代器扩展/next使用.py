
names = ["Alice", "Bob", "Charlie"]

print(names.__iter__())  #<list_iterator object at 0x00000228141299F0>

new_names =iter(names)
print(next(new_names))
print(next(new_names))
print(next(new_names))
print(next(new_names,'Join'))
print(next(new_names))  #StopIteration 告警
