from python:slim

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip3 install -r requirements.txt

COPY . .

CMD ["/usr/local/bin/python3.9", "bot.py"]
