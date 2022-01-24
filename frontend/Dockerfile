FROM nginx:1.21.4-alpine
EXPOSE 80
# CREATE BUILD DIRECTORY
RUN mkdir /build
WORKDIR /build
COPY frontend/ /build
# BUILD FRONTEND
RUN apk add --virtual .dependencies yarn && \
  yarn install && \
  yarn generate && \
  apk del .dependencies
# MOVE BUILT FILES TO /html DIRECTORY
RUN mkdir /html && \
  cp -r /build/dist/* /html
WORKDIR /html
# Allow test script to be runnable
RUN chmod +x /build/run-tests.sh
# LOAD CONFIGS
COPY nginx.conf /etc/nginx/nginx.conf
