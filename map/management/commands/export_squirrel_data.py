#export
from django.core.management import BaseCommand
from django.http import HttpResponse
from map.models import Squirrel
import csv
import sys


class Command(BaseCommand):
       
    help = 'Export squirrel data'

    def add_arguments(self, parser):
        parser.add_argument('path' ,type = str)

    def handle(self, *args, **options):
        meta = Squirrel._meta
        field_names = [i.name for i in meta.fields]
        path = options['path']

        with open('path', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(field_names)
            for i in Squirrel.objects.all():
                writer.writerow([getattr(i, j) for j in field_names])
