FROM python:3-alpine

COPY internet_check.py /

CMD ["python", "/internet_check.py"]
