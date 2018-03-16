from python:3

MAINTAINER daniel@federschmidt.xyz

COPY . /app
WORKDIR /app

RUN pip install pipenv
RUN pipenv install --system

RUN git clone https://github.com/facebookresearch/fastText.git
RUN pip install ./fastText

CMD ["python", "app.py"]