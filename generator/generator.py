import random 

from data.data import Color, Person
from faker import Faker

faker_ru = Faker('ru_RU')
Faker.seed()

def generated_person():
    yield Person(
        full_name=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
        firstname=faker_ru.first_name(),
        lastname=faker_ru.last_name(),
        email=faker_ru.email(),
        age=random.randint(18,100),
        salary=random.randint(15000, 100000),
        department=faker_ru.job(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
    )

def generated_file():
    path = rf'C:\Users\kimma\github\automation_qa_course\filetest{random.randint(0,999)}.txt'
    file = open(path, 'w+')
    file.write(f'Hello World{random.randint(0,999)}')
    file.close()
    return file.name, path

def generated_color():
    yield Color(
        color_name = ["White", "Black", "Red", "Blue", "Purple"]
    )