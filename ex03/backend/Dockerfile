FROM python:3.11-slim

WORKDIR /app

RUN pip install flask requests pysocks

COPY app.py .

CMD ["python", "app.py"]
