from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField
from django.utils.translation import gettext as _

class Part(models.Model):
    part_number_mg =       models.CharField(max_length=2, null=True, blank=True) #The parts main group according to official BMW parts number
    part_number_sb =       models.CharField(max_length=2, null=True, blank=True) # The subgroup according to BMW offical part number
    part_number =          models.CharField(max_length=7, null=True, blank=True) # the part number. the last seven digits of the part number
    part_number_no =       models.CharField(max_length=20, null=True, blank=True) # Not original Part number for parts for example from Bosh

    name =              models.CharField(max_length=255)
#correct later
    category =          models.CharField(max_length=255, null=True, blank=True)
#correct later
    car_model =         models.CharField(max_length=255)
    count =             models.IntegerField()
    description =        models.TextField(max_length=255)
    image =             models.ImageField(upload_to='parts/images/', blank=True, null=True)
    datecreated =       models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    # function that returns the category number based on the 
    def parts_mg(self):
        index = {
            '02':_('Service and Reparaturumfänge'),
            '03':_('Nachrüsten/ Umrüsten/ Zubehör'),
            '11':_('Motor'),
            '12':_('Motor-Elektrik'),
            '13':_('Kraftstoffaufbereitung'),
            '16':_('Kraftstoffversorgung'),
            '17':_('Kühler'),
            '18':_('Abgasanlage'),
            '21':_('Kupplung'),
            '22':_('Motor / Getriebeaufhängung'),
            '23':_('Getriebe mechanisch'),
            '24':_('Getriebe automatisch'),
            '25':_('Schaltung'),
            '26':_('Gelenkwelle'),
            '27':_('Verteilergetriebe / Elektro-Getriebe'),
            '31':_('Vorderachse'),
            '32':_('Lenkung'),
            '33':_('Hinterachse'),
            '34':_('Bremsen'),
            '35':_('Fussbetätigung'),
            '36':_('Räder'),
            '41':_('Karosserie / Blechteile'),
            '51':_('Fahrzeugausstattung'),
            '52':_('Sitze'),
            '54':_('Schiebedach'),
            '61':_('Fahrzeug Elektrik'),
            '62':_('Anzeigeinstrumente / Messsysteme'),
            '63':_('Beleuchtungsanlage'),
            '64':_('Heizung und Klimaanlage'),
            '65':_('Audio, Navigation, Elektroniksysteme'),
            '66':_('Distanzsysteme / Geschwindigkeitsregelung'),
            '71':_('Ausrüstungsteile'),
            '72':_('Zubehör und Rückhaltesysteme'),
            '84':_('Kommunikations-Systeme'),
            '88':_('Value Line Service und Reparatur')
        }
        mg = index[self.part_number_mg]
        return mg




