from django.forms import ModelForm 
from map.models import Squirrel

class SquirrelForm(ModelForm):
#    class Meta:
#        model = Squirrel
#        fields = '__all__'
    class Meta:
        model = Squirrel
        fields = ['latitude',
        'longitude',
        'unique_squirrel_id',
        'shift',
        'date',
        'age',
        'primary_fur_color',
        'location',
        'specific_location',
        'running',
        'chasing',
        'climbing',
        'eating',
        'foraging',
        'other_activities',
        'kuks',
        'quaas',
        'moans',
        'tail_flags',
        'tail_twitching',
        'approaches',
        'indifferent',
        'runs_from']
        labels = {
            "latitude": "latitude(cannot be blank)",
            "longitude": "longitude(cannot be blank)",
            "unique_squirrel_id": "unique_squirrel_id(cannot be blank)"}

