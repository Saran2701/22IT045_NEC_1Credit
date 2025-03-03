# Update this file to add the content

FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=ml-model.py

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]