FROM python:3-alpine3.6

COPY internet_check.py /

CMD ["python", "/internet_check.py"]
