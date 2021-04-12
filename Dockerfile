FROM buildpack-deps:buster

# Environment setting
ENV FLASK_ENV production

# System packages installation
RUN apt-get update && apt-get install -y pipenv

# Gunicorn installation
RUN pip3 install gunicorn

# Flask application
COPY ./api /api
WORKDIR /api
RUN pipenv install --system --deploy --ignore-pipfile

EXPOSE 8000

CMD ["gunicorn"  , "-b", "0.0.0.0:8000", "wsgi:app"]