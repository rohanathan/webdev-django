import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProThree.settings')

import django
django.setup()

#FAKE POP Script

import random
from appThree.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):
    
    for entry in range(N):
    
        #create the fake data for the entry
        fake_name = fakegen.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fakegen.email()
        
        #New entry
        user = User.objects.get_or_create(first_name=fake_first_name, 
                                          last_name=fake_last_name, 
                                          email=fake_email)[0]
        
 
if __name__ == '__main__':
    print("Populating databases!")
    populate(20)
    print("Populating complete!")