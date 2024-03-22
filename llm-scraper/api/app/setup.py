import csv
from datetime import datetime

from app import db
from app.models import Position, Scraping


def seed_scrapings_from_csv(csv_path='./data/scrapings.csv'):
    with open(csv_path, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            scraping = Scraping(
                position=row['position'],
                location=row['location'],
                date=datetime.strptime(row['date'], '%Y-%m-%d'),  # Adjust the date format as necessary
                job_idx=row['job_idx']
            )
            db.session.add(scraping)
        db.session.commit()

def seed_positions_from_csv(csv_path='./data/positions.csv'):
    with open(csv_path, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            position = Position(
                job_id=row['job_id'],
                job_title=row['job_title'],
                company_name=row['company_name'],
                seniority_level=row['seniority_level'],
                min_salary=float(row['min_salary']) if row['min_salary'] else None,
                max_salary=float(row['max_salary']) if row['max_salary'] else None,
                city=row['city'],
                state=row['state'],
                zipcode=row['zipcode'],
                presence=row['presence'],
                scraping_id=row['scraping_id']
            )
            db.session.add(position)
        db.session.commit()