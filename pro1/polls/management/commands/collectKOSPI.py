from django.core.management.base import BaseCommand
from datetime import datetime
from polls.models import Kospi 
import csv

class Command(BaseCommand):
    help = 'collect KOSPI data from CSV and stores it in the database'

    def handle(self, *args, **kwargs):
        # 파일 열고 데이터 읽어오기
        file_path = 'csv/kospi.csv'
        with open(file_path, 'r', encoding='utf-8') as f:
            next(f) # 첫 번째 라인 넘기기
            rows = csv.reader(f)

            # 라인별로 날짜, 종가 저장하기
            for line in rows:
                date = line[0]
                closing_price = float(line[1].replace(',', ''))

                kospi = Kospi(
                    date = datetime.strptime(date, '%Y- %m- %d'),
                    closing_price = closing_price
                )
                kospi.save()
