from faker import Faker
from random import *
fakegen=Faker()
name=fakegen.name()
print(name)
first_name=fakegen.first_name()
print(first_name)
print(fakegen.random_int(min=0,max=999))