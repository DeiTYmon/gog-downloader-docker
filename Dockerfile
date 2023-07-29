FROM python:3.10-alpine

ADD gogrepoc ./gogrepoc
ADD main.py .

RUN pip install html5lib requests pyOpenSSL

CMD ["python", "./main.py"]