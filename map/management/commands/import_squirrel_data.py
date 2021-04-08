# import
from django.core.management import BaseCommand
from map.models import Squirrel
import csv

class Command(BaseCommand):
	def add_arguements(self, parser):
		parser.add_arguement('csv_file')

	def handle(self, path, **kwargs):
		with open(kwargs['csv_file']) as f
		reader = csv.DicReader(f)
		data = list(reader)

		for i in data:
			sq = Squirrel(
				X = i['X'],
				Y = i['Y'],
				shift = i['Shift'],
				date = i['Date'],
				unique_squirrel_id = i['Unique_squirrel_id'],
				age = i['Age'],
				primary_fur_color = i['Primary_fur_color'],
				location = i['Lacation'],
				specific_location = i['Specific_location'],
				running = strtobool(i['Running']),
				chasing = strtobool(i['Chasing']),
				climbing = strtobool(i['Climbing']),
				eating = strtobool(i['Eating']),
				foraging = strtobool(i['Foraging']),
				other_activities = strtobool(i['Other Activities']),
				kuks = strtobool(i['Kuks']),
				quaas = strtobool(i['Quaas']),
				moans = strtobool(i['Moans']),
				tail_flags = strtobool(i['Tail flags']),
				tail_twitching = strtobool(i['Tail twitches']),
				approaches = strtobool(i['Approaches']),
				indifferent = strtobool(i['Indifferent']),
				runs_from = strtobool(i['Runs from']),
			)

			sq.save()













				)