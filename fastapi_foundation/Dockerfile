FROM python:3.11-slim

WORKDIR /Users/I334554/Desktop/app

COPY . .

RUN pip install -r requirements.txt
ENV PYTHONPATH=/Users/I334554/Desktop/app
CMD [ "fastapi", "run", "/Users/I334554/Desktop/app/carsharing.py", "--port", "80" ]
