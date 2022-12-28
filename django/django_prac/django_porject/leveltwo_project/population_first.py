from audioop import add
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'leveltwo_project.settings')

import django
django.setup()

from leveltwo_app.models import User

firstName = ["Ram", "Shyam", "Raghav"]
lastName = ["Sharma", "Verma", "Roy"]

def populate():
    for fname in firstName:
        for lname in lastName:
            user = User.objects.get_or_create(first_name=fname, last_name= lname, email = fname.lower()+"."+lname.lower()+"@test.com")[0]
            user.save()

if __name__ == "__main__":
    print("Population script started")
    populate()
    print("Population completed")