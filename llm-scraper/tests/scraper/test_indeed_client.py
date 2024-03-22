import pdb
from datetime import date

import pytest
from bs4 import BeautifulSoup as bs

from scraper.indeed_scraper import *


@pytest.fixture()
def cards():
    with open('./data/html_docs/indeed.html') as file:
        html_text = file.read()
    soup = bs(html_text, 'html.parser')
    cards = soup.find_all('td', {'class': 'resultContent'})
    return cards

# def test_all_cards_are_td():
#     tds = get_job_cards(position = 'data engineer', location = 'United States', start = 0)
#     list(set([td.name == 'td' for td in tds])) == 'td'

def test_get_id_from_card(cards):
    first_card = cards[0]
    job_id = get_id_from(first_card)
    assert job_id == 'af1c846c34ac0534'

def test_get_card_info(cards):
    card = cards[0]
    card_info = get_card_info(card)
    assert card_info == ['Data Engineer', 'HealthFirst',
     'Staten Island, NY 10301', '(', 'New Brighton area', ')',
      'Pay information not provided',
     'Full-time', 'job id: af1c846c34ac0534']


def test_get_card_infos(cards):
    card_infos = get_card_infos(cards)
    assert len(card_infos) == 15
    first_card_info = card_infos[0]
    assert first_card_info == ['Data Engineer', 'HealthFirst', 'Staten Island, NY 10301', '(', 'New Brighton area', ')',
     'Pay information not provided', 'Full-time', 'job id: af1c846c34ac0534']

def test_build_text():
    card_infos = [
        ['Data Engineer', 'HealthFirst', 'Staten Island, NY 10301', '(', 'New Brighton area', ')',
             'Pay information not provided',
              'Full-time', 'job id: af1c846c34ac0534'],
     ['Data Engineer', 'NYPD Civilian Jobs', 'Manhattan, NY',
      'job id: 9562c51b70acd54d']]
    text_from_card_infos = build_text(card_infos)
    matching_text = 'Data Engineer\nHealthFirst\nStaten Island, NY 10301\n(\nNew Brighton area\n)\nPay information not provided\nFull-time\njob id: af1c846c34ac0534\n\nData Engineer\nNYPD Civilian Jobs\nManhattan, NY\njob id: 9562c51b70acd54d'
    assert text_from_card_infos == matching_text

def test_directory_name_builder():
    position = 'data engineer'
    location = 'United States'
    dir_name = directory_name_builder(position, location)
    date = datetime.today().strftime('%Y-%m-%d')
    assert dir_name == f'../data/text_docs/data_engineer/united_states/{date}'
    second_dir_name = directory_name_builder('analytics engineer', 'New York City')
    assert second_dir_name == f'../data/text_docs/analytics_engineer/new_york_city/{date}'

