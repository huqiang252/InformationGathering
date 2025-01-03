class PositiveInteger:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError(f"{self.name} must be a positive integer")
        instance.__dict__[self.name] = value


class Username:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, str) or len(value) < 3 or len(value) > 50:
            raise ValueError(f"{self.name} must be between 3 and 50 characters")
        instance.__dict__[self.name] = value


class Email:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, str) or '@' not in value:
            raise ValueError(f"{self.name} must be a valid email address")
        instance.__dict__[self.name] = value



class UserValidator:
    user_id = PositiveInteger()
    username = Username()
    email = Email()

    def __init__(self, user_id, username, email):
        self.user_id = user_id
        self.username = username
        self.email = email

    def __repr__(self):
        return f"UserValidator(user_id={self.user_id}, username='{self.username}', email='{self.email}')"

# 测试校验器
def test_user_validator():
    try:
        user = UserValidator(user_id=1, username='john_doe', email='john@example.com')
        print("Validation successful:", user)
    except ValueError as e:
        print("Validation failed:", e)

    try:
        user = UserValidator(user_id=-1, username='john_doe', email='john@example.com')
        print("Validation successful:", user)
    except ValueError as e:
        print("Validation failed:", e)

    try:
        user = UserValidator(user_id=1, username='j', email='john@example.com')
        print("Validation successful:", user)
    except ValueError as e:
        print("Validation failed:", e)

    try:
        user = UserValidator(user_id=1, username='john_doe', email='invalid-email')
        print("Validation successful:", user)
    except ValueError as e:
        print("Validation failed:", e)

if __name__ == "__main__":
    test_user_validator()

