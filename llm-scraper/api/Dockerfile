FROM python:3.7-alpine
WORKDIR /usr/src/app

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev


COPY ./app/requirements.txt ./

RUN pip3 install -r requirements.txt

COPY .env .env
COPY .flaskenv .flaskenv
COPY ./app ./

# Make sure the script is executable
RUN chmod +x ./setup.sh

# Use the script as the entrypoint
ENTRYPOINT ["sh", "./setup.sh"]

# Set the default command to run your Flask application
CMD ["flask", "run", "--host=0.0.0.0"]