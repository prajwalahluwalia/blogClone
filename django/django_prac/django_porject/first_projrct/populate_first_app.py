import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_projrct.settings')

import django
django.setup()

#FAKE Script
import random
from first_app.models import AccessRecord, Topic, WebPage
from faker import Faker

fakegen = Faker()

topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        #get topic for entry
        top = add_topic()

        #create fake data
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        #create new webpage entry
        webpg = WebPage.objects.get_or_create(topic = top, url = fake_url, name = fake_name)[0]

        #create fake access record
        access_rec = AccessRecord.objects.get_or_create(name = webpg, date = fake_date)[0]

if __name__=='__main__':
    print("populating scripts")
    populate(20)
    print("Populating completed")