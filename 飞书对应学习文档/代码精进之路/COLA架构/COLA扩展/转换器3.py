from dataclasses import dataclass, asdict, fields
from typing import List


@dataclass
class Address:
    street: str
    city: str
    zip_code: str


@dataclass
class User:
    user_id: int
    username: str
    email: str
    addresses: List[Address]
    roles: List[str]


@dataclass
class AddressDTO:
    street: str
    city: str
    zip_code: str


@dataclass
class UserDTO:
    user_id: int
    username: str
    email: str
    addresses: List[AddressDTO]
    roles: List[str]


def convert(source, target_class):
    source_dict = asdict(source)

    # Create a mapping from source field names to target field names
    source_field_names = {field.name: field.name for field in fields(source)}
    target_field_names = {field.name: field.name for field in fields(target_class)}

    # Create a dictionary to hold the target attributes
    target_kwargs = {}

    for source_field_name, source_value in source_dict.items():
        if source_field_name in target_field_names:
            target_field_name = target_field_names[source_field_name]
            if isinstance(source_value, list):
                # Handle lists of objects
                target_value = [
                    convert(item, target_class.__annotations__[target_field_name].__args__[0])
                    for item in source_value
                ]
            else:
                # Handle single objects
                if hasattr(source_value, '__dict__'):
                    target_value = convert(source_value, target_class.__annotations__[target_field_name])
                else:
                    target_value = source_value
            target_kwargs[target_field_name] = target_value

    return target_class(**target_kwargs)


# Test conversion
def test_conversion():
    address1 = Address(street="123 Main St", city="Anytown", zip_code="12345")
    address2 = Address(street="456 Elm St", city="Othertown", zip_code="67890")
    user = User(user_id=1, username='john_doe', email='john@example.com', addresses=[address1, address2],
                roles=['admin', 'user'])

    user_dto = convert(user, UserDTO)
    print("User to UserDTO:", user_dto)

    user_from_dto = convert(user_dto, User)
    print("UserDTO to User:", user_from_dto)


if __name__ == "__main__":
    test_conversion()
