# index/import_daya.py
import sys

sys.argv = [arg.encode(sys.stdout.encoding, 'replace').decode(sys.stdout.encoding) for arg in sys.argv]

import csv
from .models import Shop

def import_data_from_csv(csv_file_path):
    with open(csv_file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            Shop.objects.create(
                shop_name=row['상호명'],
                addr=row['도로명주소'],
                latitude=row['위도'],
                longitude=row['경도'],
                brand=row['브랜드'],
            )
