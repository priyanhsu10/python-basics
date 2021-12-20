from json import JSONEncoder
import json
person = {"name": "John", "age": 30, "city": "New York",
          "hasChildren": False, "titles": ["engineer", "programmer"]}

# personJson = json.dumps(person, indent=4, sort_keys=True)

# print(person)

# with open('person.json', 'w') as file:
#     json.dump(person, file, indent=4)

# persons = json.loads(personJson)
# print(type(persons))
# print(persons)

# with open('person.json', 'r') as file:
#     person = json.load(file)
#     print(type(person))
#     print(person)


class User:

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age


user = User('priyanshu', 30)


def encode_user(o):
    if isinstance(o, User):
        return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
    else:
        raise TypeError('Object of type User is not JSON serializable')


class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
        else:
            return JSONEncoder.default(self, o)


# userJSon = json.dumps(user, default=encode_user)
userJSon = json.dumps(user, cls=UserEncoder)
print(userJSon)


def decode_user(dic):
    if User.__name__ in dic:
        return User(name=dic['name'], age=dic['age'])
    return dic


user: User = json.loads(userJSon, object_hook=decode_user)
print(type(user))
print(user.name)
