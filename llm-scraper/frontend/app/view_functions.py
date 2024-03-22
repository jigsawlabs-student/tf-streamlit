import json

import pandas as pd
import requests

from settings import api_url


def find_positions():
    response = requests.get(api_url)
    json_dicts = json.loads(response.text)
    return pd.DataFrame(json_dicts)