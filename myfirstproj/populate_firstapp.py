import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','myfirstproj.settings')

import django
django.setup()

## FAKE POP scripts
import random
from firstapp.models import AccessRecord, Webpage, Topic
from faker import Faker
fakedata = Faker()
topics = ['Search','Social','Marketplace','News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        top = add_topic()

        #create the fake data for that entry
        fake_url = fakedata.url()
        fake_date = fakedata.date()
        fake_name = fakedata.company()

        webpg = Webpage.objects.get_or_create(topic = top, url =fake_url, name = fake_name)[0]

        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date = fake_date)
if __name__ == '__main__':
    print('Calling data populating script...')
    populate(20)
    print('Data population complete.')
