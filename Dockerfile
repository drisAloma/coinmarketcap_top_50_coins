FROM python:latest

ADD scrapper.py .

RUN pip install pandas requests beautifulsoup4

CMD [ "python", "./scrapper.py"]
