FROM python:3

WORKDIR /usr/src/app

RUN mkdir /usr/src/app/log

COPY requirements.txt . 

RUN pip install --no-cache-dir -r requirements.txt

COPY . . 

EXPOSE 8000

CMD [ "uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000" ]
