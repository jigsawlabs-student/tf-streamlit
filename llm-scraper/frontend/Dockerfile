FROM python:3.7
WORKDIR /usr/src/app

COPY ./requirements.txt ./

RUN pip3 install -r requirements.txt
COPY .env .env

COPY ./app ./

CMD ["streamlit", "run", "./index.py", "--server.address=0.0.0.0", "--server.port=80"]