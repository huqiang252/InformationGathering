from pydantic import BaseModel

class User(BaseModel):
    user_id: int
    username: str
    email: str

class UserDTO(BaseModel):
    user_id: int
    username: str
    email: str

# 转换函数
def user_to_user_dto(user: User) -> UserDTO:
    return UserDTO.model_validate(user.model_dump())

def user_dto_to_user(user_dto: UserDTO) -> User:
    return User.model_validate(user_dto.model_dump())




if __name__ == "__main__":
    user = User(user_id=1, username='john_doe', email='john@example.com')
    user_dto = user_to_user_dto(user)
    print("User to UserDTO:", user_dto,type(user_dto))

    user_from_dto = user_dto_to_user(user_dto)
    print("UserDTO to User:", user_from_dto,type(user_from_dto))

