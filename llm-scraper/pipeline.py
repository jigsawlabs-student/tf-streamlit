import requests
from prefect import flow, task
from prefect.server.schemas.schedules import IntervalSchedule

import scraper.indeed_scraper as indeed_scraper


@task
def retrieve_and_write_pages(position, location, pages):
    file_names = indeed_scraper.retrieve_and_write_pages(position, location, pages)
    return file_names

@task
def read_files_to_db(file_names):
    files_to_db(file_names)

@flow
def scrape_and_load_positions(positions, locations, pages):
    for position in positions:
        for location in locations:
            file_names = retrieve_and_write_pages(position, location, pages)
            read_files_to_db(file_names)


scrape_and_load_positions(positions = ["data engineer", "analytics engineer"], 
locations=["New York City", "San Francisco"], pages = 5
)

# if __name__ == "__main__":
#     scrape_and_load_positions.serve(
#         name="scrape-and-load-deployment",
#         schedule=IntervalSchedule(interval=100),
#         parameters={'positions': ["data engineer", "analytics engineer"], 
#         'locations': ["New York City", "San Francisco"], "pages": 5}
#         )