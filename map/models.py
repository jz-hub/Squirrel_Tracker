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
    
    date = models.IntegerField(
            help_text=_('Date of sighting'),
        )

    ADULT = 'Adult'
    JUVENILE = 'Juvenile'
    
    AGE_CHOICES = (
        (ADULT, 'Adult'),
        (JUVENILE, 'Juvenile'),
    )
    
    age = models.CharField(
            help_text=_('Value is either Adult or Juvenile'),
            max_length=20,
            choices=AGE_CHOICES,
        )

    BLACK = 'Black'
    GRAY = 'Gray'
    CINNAMON = 'Cinnamon'

    COLOR_CHOICES = (
        (BLACK, 'Black'),
        (GRAY, 'Gray'),
        (CINNAMON, 'Cinnamon'),
    )



    primary_fur_color = models.CharField(
            help_text=_('Value is either gray, cinnamon or black'),
            max_length = 10,
            choices = COLOR_CHOICES,
            default = 'Unknown',
        )


    GROUND = 'Ground plane'
    ABOVE = 'Above ground'

    LOCATION_CHOICE= (
            (GROUND, 'Ground plane'),
            (ABOVE, 'Above ground'),
        )

    location = models.CharField(
            help_text=_('Location of squirrel'),
            choices = LOCATION_CHOICE,
            blank = True,
            max_length = 20,
        )

    specific_Location = models.CharField(
            help_text=_('Specific location of squirrel'),
            blank = True,
            max_length = 150,
        )

    running = models.BooleanField(
            help_text=_('True if squirrel was seen running'),
            default=False,
        )

    chasing = models.BooleanField(
            help_text=_('True if squirrel was seen chasing'),
            default=False,
         )
    climbing = models.BooleanField(
            help_text=_('True if squrriel was seen climbing'),
            default=False,
        )
    eating = models.BooleanField(
            help_text=_('True if squrriel was seen eating'),
            default=False,
        )
     
    foraging = models.BooleanField(
            help_text=_('True if squrriel was seen foraging'),
            default=False,
        )
     
    other_activities = models.CharField(
            help_text=_('Other activities'),
            blank=True,
            max_length = 150,
        )
            
    kuks = models.BooleanField(
            help_text=_('True if the squrriel was heard kuking'),
            default=False,
        )
        
    quaas = models.BooleanField(
            help_text=_('True if the squrriel  was heard Quaaing'),
            default=False,
        )
     
    moans = models.BooleanField(
            help_text=_('True if the squrriel was heard moaning'),
            default=False,
        )
            
    tail_flags = models.BooleanField(
            help_text=_('True if the squrriel was seen flagging its tail'),
            default=False,
        )
            
    tail_twitching = models.BooleanField(
            help_text=_('True if the squrriel was seen twitching its tail'),
            default=False,
        )
            
    approaches = models.BooleanField(
        help_text=_('True if the squrriel was seen approaching human'),
        default=False,
        )
            
    indifferent = models.BooleanField(
            help_text=_('True if squirrel was indifferent to huamn presence'),
            default=False,
        )
    runs_from = models.BooleanField(
            help_text=_('True if squirrel was seen running from humans'),
            default=False,
        )
    
    def __str__(self):
        return self.unique_squirrel_id





# Create your models here.
