FROM python:3.9

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip3 install -r requirements.txt

COPY . .

ENTRYPOINT ["python3", "src/index.py"]
