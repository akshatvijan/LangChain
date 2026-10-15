from typing import TypedDict

class Person(TypedDict):
    name:str
    age:int

new_person:Person={'name':'akshat','age':18}
print(new_person)
