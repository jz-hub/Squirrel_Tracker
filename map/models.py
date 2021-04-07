from django.db import models
from django.utils.translation import gettext as _

class Squirrel(models.Model):
    Latitude = models.DecimalField(
        max_digits=40,
        help_text=_('Latitude of sighting point'),  
        decimal_places=15,
    )

    Longitude = models.DecimalField(
        max_digits=40, 
        help_text=_('Longitude of sighting point'),
        decimal_places=10,
    )
 
    Unique_squirrel_id = models.CharField(
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

    Shift = models.CharField(
        max_length=2,
        help_text=_('Shift of the day'),
        choices=SHIFT_CHOICES,
        default='Unknown',
    )
    
    Date = models.IntegerField(
            help_text=_('Date of sighting'),
        )

    ADULT = 'Adult'
    JUVENILE = 'Juvenile'
    
    AGE_CHOICES = (
        (ADULT, 'Adult'),
        (JUVENILE, 'Juvenile'),
    )
    
    Age = models.CharField(
            help_text=_('Value is either Adult or Juvenile'),
            max_length=20,
            choices=AGE_CHOICES,
        )

    Primary_Fur_Color = models.CharField(
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

    Location = models.CharField(
            help_text=_('Location of squirrel'),
            choices = LOCATION,
            blank = True,
            max_length = 20,
        )

    Specific_Location = models.CharField(
            help_text=_('Specific location of squirrel'),
            blank = True,
            max_length = 150,
        )

    Running = models.BooleanField(
            help_text=_('True if squirrel was seen running),
            default=False,
        )

    Chasing = models.BooleanField(
            help_text=_('True if squirrel was seen chasing),
            default=False,
         )
    Climbing = models.BooleanField(
            help_text=_('True if squrriel was seen climbing),
            default=False,
        )
    Eating = models.BooleanField(
            help_text=_('True if squrriel was seen eating),
            default=False,
        )
     
    Foraging = models.BooleanField(
            help_text=_('True if squrriel was seen foraging),
            default=False,
        )
     
    Other_Activities = models.CharField(
            help_text=_('Other activities'),
            blank=True,
            max_length = 150,
        )
            
    Kuks = models.BooleanField(
            help_text=_('True if the squrriel was heard kuking),
            default=False,
        )
    

    Quaas = models.BooleanField(
            help_text=_('True if the squrriel  was heard Quaaing),
            default=False,
        )
     
    Moans = models.BooleanField(
            help_text=_('True if the squrriel was heard moaning),
            default=False,
        )
            
    Tail_flags = models.BooleanField(
            help_text=_('True if the squrriel was seen flagging its tail),
            default=False,
        )
            
    Tail_twitching = models.BooleanField(
            help_text=_('True if the squrriel was seen twitching its tail),
            default=False,
        )
            
    Approaches = models.BooleanField(
        help_text=_('True if the squrriel was seen approaching human),
        default=False,
        )
            
    Indifferent = models.BooleanField(
            help_text=_('True if squirrel was indifferent to huamn presence),
            default=False,
        )
    Runs_from = models.BooleanField(
            help_text=_('True if Squirrel was seen running from humans),
            default=False,
        )
    
    def __str__(self):
        return self.unique_squirrel_id





# Create your models here.
