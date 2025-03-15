import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mexexpress.settings')
import django
django.setup()

#Script para poblar la tabla de productos
from faker import Faker
import random
from shopApp.models import Contact

fake_generator = Faker()

def populate_contacts(n_contacts=50):
    for i in range(n_contacts):
        fake_name = fake_generator.sentence(nb_words=6, variable_nb_words=True)
        fake_address = fake_generator.paragraph(nb_sentences=3, variable_nb_sentences=True)
        fake_phone = fake_generator.phone_number()
        fake_email = fake_generator.email()
        fake_active = random.random() > 0.5
        
        contact = Contact.objects.get_or_create(
            full_name = fake_name,
            address = fake_address,
            phone = fake_phone,
            email = fake_email,
            active = fake_active,
        )

if __name__ == '__main__':
    print("Poblando la base de datos")
    populate_contacts()
    print("Finalizado") 
