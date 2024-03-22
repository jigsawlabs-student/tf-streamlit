import datetime
import pdb
from datetime import date

import pytest
from bs4 import BeautifulSoup as bs

from app import create_app, db
from app.models import Position, Scraping
from scraper.file_reader import *
from settings import test_db


def test_file_to_df():
    file_name = "./data/sample/example/results_0.txt"
    df = file_to_df(file_name)
    records = [{'job_id': 'e786e718fef6eccf', 'job_title': 'Data Center Engineer', 'company_name': 'PAYLOCITY CORPORATION', 'seniority_level': None, 'min_salary': 62000.0, 'max_salary': 117000.0,
     'city': 'Schaumburg', 'state': 'IL', 'zipcode': '60173', 'presence': None},
     {'job_id': 'bd1c7f18f0faf355', 'job_title': 'Data Engineer',
      'company_name': 'Archer Daniels Midland Company',
       'seniority_level': None, 'min_salary': None,
        'max_salary': None, 'city': 'Erlanger', 
     'state': 'KY', 'zipcode': None, 'presence': None}]
    assert df.to_dict('records') == records

def test_parse_from_file_name():
    file_name = "./data/text_docs/data_engineer/united_states/2024-03-01/results_2.txt"
    parsed_dict = parse_from_file_name(file_name)
    assert parsed_dict == {'position': 'data_engineer', 'location': 'united_states',
     'date': '2024-03-01', 'job_idx': '2'}

    more_nested_file_name = "./data/sample/text_docs/data_engineer/united_states/2024-03-01/results_2.txt"
    parsed_dict = parse_from_file_name(more_nested_file_name)
    assert parsed_dict == {'position': 'data_engineer', 'location': 'united_states',
     'date': '2024-03-01', 'job_idx': '2'}

def delete_records():
    db.session.query(Position).delete()
    db.session.query(Scraping).delete()

@pytest.fixture
def build_db(): 
    app = create_app(test_db)
    with app.app_context():
        delete_records()
        yield
        delete_records()
    
def test_file_to_db(build_db):
    file_name = "./data/sample/data_engineer/united_states/2024-03-01/results_2.txt"
    file_to_db(file_name, test_db)
    scraping = db.session.query(Scraping).first()
    positions = scraping.positions
    assert db.session.query(Position).filter_by(job_id = 'bd0f06b3dbd568d7').first()

def test_file_to_db_does_not_reinsert_positions(build_db):
    file_name = "./data/sample/data_engineer/united_states/2024-03-01/results_2.txt"
    file_to_db(file_name, test_db)
    scraping = db.session.query(Scraping).first()
    positions = scraping.positions

    file_to_db(file_name, test_db)
    assert len(positions) == len(db.session.query(Position).all())
    
    
# def test_dir_to_dfs():
#     dir_name = "./data/sample/example/"
#     filenames_dfs = dir_to_dfs(dir_name)
#     len(filenames_dfs) == 2
#     first_filename_df = filenames_dfs[0]
#     assert first_filename == 'results_0.txt'
    
