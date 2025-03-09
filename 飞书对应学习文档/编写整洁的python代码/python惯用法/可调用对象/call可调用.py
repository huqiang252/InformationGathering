

from collections import defaultdict



class CallCount:

    def __init__(self):
        self._counts = defaultdict(int)

    def __call__(self, argument):
        self._counts[argument] += 1
        return self._counts[argument]



if __name__ == '__main__':
    call_count = CallCount()
    print(call_count(1)) #1
    print(call_count(2)) #1
    print(call_count(1)) #2
    print(call_count(1)) #3
    print(call_count('something')) #1
    print(callable(call_count)) #True
