
from src.adapters.indeed_client import (build_text, get_card_infos,
                                        get_indeed_html, get_job_cards,
                                        retrieve_and_write)

cards = get_job_cards(position = 'data engineer', location = 'United States', start = 0)

card_infos = get_card_infos(cards)
combined_text = build_text(card_infos)
# retrieve_and_write()
