FROM python:3.7-alpine

RUN pip install --upgrade pip

COPY . .

#RUN python3 bregressorv2.py --data random1.csv --eta 0.0001 --threshold 0.0001

CMD ["python", "./bregressorv2.py"]