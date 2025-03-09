


def wrong_user_display(user_metadata: dict = {"name": "John", "age": 30}):
    name = user_metadata.pop("name")

    age = user_metadata.pop("age")

    return f"{name} ({age})"


def user_display(user_metadata: dict = None):
    user_metadata = user_metadata or {"name": "John", "age": 30}

    name = user_metadata.pop("name")

    age = user_metadata.pop("age")

    return f"{name} ({age})"


if __name__ == '__main__':
    print(wrong_user_display())    #John (30)
    print(wrong_user_display({"name": "Jane", "age": 25})) #Jane (25)
    # print(wrong_user_display())      #KeyError: 'name'


    print(user_display())    #John (30)
    print(user_display({"name": "Jane", "age": 25})) #Jane (25)
    print(user_display())      #John (30)



