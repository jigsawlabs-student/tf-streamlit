import json
import os

from openai import OpenAI

from settings import open_ai_api_key

client = OpenAI(
  api_key=open_ai_api_key,
)

def build_prompt(file_text):
    JSON_SCHEMAS =  {
        "job_id": "string",
        "job_title": "string (do not include information about senority level, Good: data engineer, Bad: Senior data engineer)",
        "company_name": "string",
        "seniority_level": "string (eg. senior, sr., midlevel, jr., associate, I, II, III, principal, lead)",
        "min_salary": "integer",
        "max_salary": "integer",
        "city": "string (city name or unknown)",
        "state": "string (state name or unknown)",
        "zipcode": "string (zipcode or unknown)",
        "presence": "string (in-person, remote, hybrid, unknown)"
        # Include additional fields as required
    }

    ex_1 = {'job_id': 'afece6001fb4eb54', 'job_title': 'Data Engineer',
    'company_name': 'Disney Entertainment & ESPN Technology',
    'seniority_level': 'senior', 'min_salary': 136038,
    'max_salary': 182490, 'city': 'New York',
        'state': 'NY', 'zipcode': None, 'presence': 'unknown'}

    prompt = f"""Format in json, the job_title, company_name, min_salary, max_salary, location, and presence as in-person, remote, hybrid or unknown of each of the jobs in the context.

    The json schema should include: 

    {JSON_SCHEMAS}

    Example:


    Senior Data Engineer
    Disney Entertainment & ESPN Technology
    New York, NY
    $136,038 - $182,490 a year
    job id: afece6001fb4eb54

    {ex_1}


    Context:

    {file_text}
    """
    return prompt

def return_json_from(prompt):
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ],
    response_format={ "type": "json_object" }
    )
    json_content = completion.choices[0].message.content
    json_response = json.loads(json_content)
    return json_response
# https://community.openai.com/t/how-do-i-use-the-new-json-mode/475890/11


