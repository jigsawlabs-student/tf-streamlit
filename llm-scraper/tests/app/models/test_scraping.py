import datetime

import pytest

from app import create_app, db
from app.models import Position, Scraping
from settings import test_db


def delete_records():
    db.session.query(Position).delete()
    db.session.query(Scraping).delete()

@pytest.fixture
def build_db(): 
    app = create_app(test_db)
    with app.app_context():
        delete_records()
        attrs = {'job_id': 'bd0f06b3dbd568d7', 'job_title': 'Data Engineer', 'company_name': 'Unity Catalog - Data Bricks', 'seniority_level': None,
         'min_salary': None, 'max_salary': None, 'city': 'unknown', 
         'state': None, 'zipcode': None, 'presence': 'remote', 'scraping_id': 1}
        position = Position(**attrs)
        db.session.add(position)

def test_init_scraping(build_db):
    scraping_attrs = {'date': datetime.date(2024, 3, 1), 'position': 'data_engineer', 'location': 'united_states', 'job_idx': 2}
    scraping = Scraping(**scraping_attrs)
    assert scraping.position == 'data_engineer'