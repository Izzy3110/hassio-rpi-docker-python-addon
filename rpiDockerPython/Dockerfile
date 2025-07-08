ARG BUILD_FROM
FROM $BUILD_FROM
ENV LANG C.UTF-8

COPY run.sh /
COPY requirements.txt /
COPY main.py /

WORKDIR /data

RUN apk add curl python3 py3-pip
RUN chmod a+x /run.sh

RUN pip install -r /requirements.txt

CMD [ "/run.sh" ]