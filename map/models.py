from django.db import models
from django.utils.translation import gettext as _

class Squirrel(models.Model):
    latitude = models.DecimalField(
        max_digits=40,
        help_text=_('Latitude of sighting point'),  
        decimal_places=15,
    )

    longitude = models.DecimalField(
        max_digits=40, 
        help_text=_('Longitude of sighting point'),
        decimal_places=10,
    )
 
    unique_squirrel_id = models.CharField(
        max_length=40,
        help_text=_('Unique Squirrel ID Number'),
        primary_key=True,
    )

    AM = 'AM'
    PM = 'PM'
    SHIFT_CHOICES = [   
        (AM,_('AM')),
        (PM,_('PM')),
    ]

    shift = models.CharField(
        max_length=2,
        help_text=_('Shift of the day'),
        choices=SHIFT_CHOICES,
        default='Unknown',
    )






# Create your models here.
