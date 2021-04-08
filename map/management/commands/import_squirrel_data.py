# import
from django.core.management import BaseCommand, CommandError
from map.models import Squirrel
import csv
from distutils.util import strtobool
import datetime

class Command(BaseCommand):
    help = 'import data'

    def add_arguments(self, parser):
        parser.add_argument('csv_file')

    def handle(self, *args, **options):
        with open(options['csv_file']) as f:
            reader = csv.DictReader(f)
            data = list(reader)
        for i in data:
            sq = Squirrel(
                longitude = i['X'],
                latitude = i['Y'],
                shift = i['Shift'],
                date = i['Date'],
                unique_squirrel_id = i['Unique Squirrel ID'],
                age = i['Age'],
                primary_fur_color = i['Primary Fur Color'],
                location = i['Location'],
                specific_location = i['Specific Location'],
                running = strtobool(i['Running']),
                chasing = strtobool(i['Chasing']),
                climbing = strtobool(i['Climbing']),
                eating = strtobool(i['Eating']),
                foraging = strtobool(i['Foraging']),
                other_activities = i['Other Activities'],
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
