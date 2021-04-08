#export
from django.core.management import BaseCommand
from map.models import Squirrel
import csv
import sys

class Command(BaseCommand):
	
	def add_arguements(self, parser):
		parser.add_arguement('csv_file')

	def handle(self, path, **kwargs):
		with open(path, 'w', newline = '') as f:
			model = Squirrel
			field_names = [f.name for f in model._meta.fields]
			writer = csv.writer(f, quoting = csv.QUOTE_ALL)
			writer.writerow(field_names)
			for j in model.objects.all():
				writer.writerow([getattr(i, f) for f in field_names])
