FROM python:3.11

COPY . .

RUN pip install -U pip
RUN pip install -r requirements.txt

CMD tail -f /dev/null