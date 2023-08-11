# Using lightweight alpine image
FROM python:3.8-alpine

# Installing packages
RUN apk update
RUN pip install --no-cache-dir pipenv

# Defining working directory and adding source code
WORKDIR /home/santoshk/SK/pycharm2/android/letsdate/
COPY Pipfile Pipfile.lock bootstrap.sh ./
COPY dateapi ./dateapi

# Install API dependencies
RUN pipenv install --system --deploy

# Start app
EXPOSE 5000
ENTRYPOINT ["/home/santoshk/SK/pycharm2/android/letsdate/date_api_proj/bootstrap.sh"]