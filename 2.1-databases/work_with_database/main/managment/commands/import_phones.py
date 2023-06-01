from django.core.management.base import BaseCommand
from phones.models import Phone
from autoslug import AutoSlugField

class Command(BaseCommand):
	help = 'download from csv file'

	def handle(self, *args, **options):
        with open ('phones.csv', newline='\n') as csvfile:
        reader = csv.DictReader(csvfile, delimiter = ";")
        for row in reader:            
            phone = Phone(
                custom_id = row['id'],
                name = row['name'],
                price = row['price'],
                image = row['image'],
                release_date = row['release_date'],
                lte_exists = row['lte_exists'],
            )
            phone.save()
            
        self.stdout.write("Телефоны обработаны", ending='')
