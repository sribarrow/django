import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

## FAKE POP scripts
import random
from AppTwo.models import User
from faker import Faker
fakedata = Faker()

def populate(N=5):
    for entry in range(N):

        #create the fake data for that entry
        fake_name = fakedata.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fakedata.email()

        user = User.objects.get_or_create(first_name = fake_first_name, last_name =fake_last_name, email = fake_email)[0]

if __name__ == '__main__':
    print('Calling data populating script...')
    populate(20)
    print('Data population complete.')
