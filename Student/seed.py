from faker import Faker
from .models import *
import random

fake = Faker()

def seed_db(n=10)->None:
    try:
        for i in range(0,n):
            name = fake.name()
            email = fake.email()
            age = random.randint(18,25)

            a = Student.objects.create(
                name = name,
                email = email,
                age = age,
            )

    except Exception as e:
        print(e)

def marks(n):
    try:
        a = Student.objects.all()
        for i in a:
            b = Subject.objects.all()
            for j in b:
                Mark.objects.create(
                    student = i,
                    subject = j,
                    mark = random.randint(33 , 100)
                )
    
    except Exception as e:
        print(e)