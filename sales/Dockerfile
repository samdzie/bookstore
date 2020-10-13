FROM python:3.8
EXPOSE 5000
WORKDIR /srv/sales
COPY . .
RUN ["pip", "install", "pipenv"]
RUN ["pipenv", "install", "--system", "--deploy", "--ignore-pipfile"]
CMD ["flask", "run", "--host", "0.0.0.0"]
