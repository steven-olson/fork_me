FROM python:3.7-slim-buster
WORKDIR /app
COPY  ./requirements.txt /app

RUN pip install -r requirements.txt
COPY . .

EXPOSE 5000
ENV FLASK_APP=main.py

# update this variable if you want this service
# to fork some other repo
ENV TARGET_URL=https://github.com/steven-olson/fork_me

CMD ["flask", "run", "--host", "0.0.0.0"]