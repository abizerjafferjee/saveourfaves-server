import django
import sys
import os
sys.path.append(os.path.dirname(__file__) + '/..')

os.environ['DJANGO_SETTINGS_MODULE'] = 'carebackend.settings'
django.setup()

from places.models import Area
import pandas as pd
import sys

fl = sys.argv[1]

df = pd.read_csv(fl)

for _, row in df.iterrows():
    try:
        a = Area.objects.get(key=row['key'])
    except Area.DoesNotExist:
        a = Area(
            key=row['key'])
    
    a.display_name = row['display_name']
    a.save()