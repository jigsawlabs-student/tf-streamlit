drop table if exists scrapings;
drop table if exists positions;

CREATE TABLE positions (
    job_id VARCHAR PRIMARY KEY,
    job_title VARCHAR(120),
    company_name VARCHAR(120),
    seniority_level VARCHAR(120),
    min_salary FLOAT,
    max_salary FLOAT,
    city VARCHAR(120),
    state VARCHAR(120),
    zipcode VARCHAR(120),
    presence VARCHAR(120),
    scraping_id INTEGER
);

CREATE TABLE scrapings (
    id SERIAL PRIMARY KEY,
    position VARCHAR(120) NOT NULL,
    location VARCHAR(120) NOT NULL,
    date DATE NOT NULL,
    job_idx INTEGER NOT NULL
);
