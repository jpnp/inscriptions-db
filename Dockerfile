FROM python:3.11-alpine
WORKDIR /code
ENV FLASK_APP=marcusdb
ENV FLASK_RUN_HOST=0.0.0.0
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . . 
CMD ["flask", "run"] 
