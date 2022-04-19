FROM python:latest

ADD main.py .

RUN pip install pandas requests beautifulsoup4

CMD [ "python", "./main.py"]
