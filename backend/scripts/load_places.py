import django
import sys
import os
sys.path.append(os.path.dirname(__file__) + '/..')
os.environ['DJANGO_SETTINGS_MODULE'] = 'carebackend.settings'
django.setup()
from places.models import Place
import pandas as pd
import sys

fl = sys.argv[1]

df = pd.read_csv(fl)

for _, row in df.iterrows():
    try:
        p = Place.objects.get(place_id=row.get('place_id'))
    except Place.DoesNotExist:
        p = Place(
            place_id=row.get('place_id'))
    
    p.lat = row.get('lat')
    p.lng = row.get('lng')
    p.address = row.get('formatted_address')
    p.user_rating = row.get('rating')
    if not p.name:
        p.name = row.get('name')
    p.num_ratings = row.get('user_ratings_total')
    p.gift_card_url = row.get('gift_card_url')
    p.photo_attribution = row.get('photo_attribution')
    p.image_url = row.get('photo_url')
    p.save()