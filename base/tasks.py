from django.utils import timezone
from .models import Building, Profile

def update_monthly_payment():
    today = timezone.now().date()
    buildings = Building.objects.filter(payment_date__lt=today)
    for building in buildings:
        building.payment_date= building.payment_date + timezone.timedelta(days=30)
        print(building.payment_date)
        building.save()        
        profiles = Profile.objects.filter(building_id=building)
        for profile in profiles:
            profile.monthly_payment = False
            profile.save()    
            

