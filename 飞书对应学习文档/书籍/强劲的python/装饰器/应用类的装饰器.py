def singletion(cls):
    instances = {}

    def get_instance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]

    return get_instance


@singletion
class Evlas:
    pass


if __name__ == '__main__':
    a = Evlas()
    b = Evlas()
    print(id(a) == id(b))  # True
