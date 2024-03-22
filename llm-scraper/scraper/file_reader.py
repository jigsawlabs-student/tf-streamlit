import os
from pathlib import Path

import numpy as np
import pandas as pd

from app import create_app, db
from app.models import *
from scraper.json_builder import *


def read_file(file):
    f = open(file, "r")
    text = f.read()
    return text

def file_to_df(file_name):
    file_text = read_file(file_name)
    if len(file_text) < 20:
        return pd.DataFrame()
    else:
        prompt = build_prompt(file_text)
        
        json_data = return_json_from(prompt)['jobs']
        df = pd.DataFrame(json_data)
        df = df.replace({np.nan: None, 'unknown': None, '': None})
        return df

def parse_from_file_name(file_name):
    last_elements = file_name.split('/')[-4:]
    position, location, date, file_name_ext = last_elements
    file_name, ext = file_name_ext.split('.')
    prefix, idx = file_name.split('_')
    return {'position': position, 'location': location, 'date': date, 'job_idx': idx}

def file_to_db(file_name, db_conn):
    app = create_app(db_conn)
    
    df = file_to_df(file_name)
    positions = []
    with app.app_context():
        scraping_attrs = parse_from_file_name(file_name)
        scraping = Scraping(**scraping_attrs)
        db.session.add(scraping)
        db.session.commit()
        
        for idx, row in df.iterrows():
            pos_attrs = row.to_dict()
            position = Position(**pos_attrs)
            position.scraping = scraping
            existing_position = db.session.query(Position).filter_by(job_id = position.job_id).first()
            if not existing_position:
                
                db.session.add(position)
                db.session.commit()
                positions.append(position)
    return positions

def files_to_db(file_names):
    position_lists = [file_to_db(file_name, db_conn) for file_name in file_names]
    return sum(position_lists,[])

    





def list_files(directory):
    file_names = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_names.append(os.path.join(root, file))
    return file_names

