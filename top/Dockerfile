FROM python:alpine

ENV BASE_DIR "/opt/sngsk.info/top"

RUN apk --no-cache add shadow \
	&& useradd --create-home app \
	&& mkdir -p $BASE_DIR \
	&& chown app:app $BASE_DIR
USER app
WORKDIR $BASE_DIR

COPY . .
RUN pip install --no-cache-dir --no-warn-script-location --user -r requirements.txt

EXPOSE 8080

CMD [ "python", "./main.py" ]
