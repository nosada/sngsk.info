FROM nginx:alpine

ENV BASE_DIR "/opt/sngsk.info/"

RUN mkdir -p $BASE_DIR/static_files && chown nginx:nginx -R $BASE_DIR
WORKDIR $BASE_DIR

USER nginx
COPY ./static_files ./static_files
COPY ./nginx/container/nginx.conf /etc/nginx/nginx.conf

EXPOSE 8081

CMD ["nginx", "-g", "daemon off;"]
