FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pytest ./tests/tests_Routes

COPY . .

CMD [ "python", "./server.py" ]
