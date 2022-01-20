from python:3.8-alpine

# Copy source code to image

RUN mkdir /app
WORKDIR /app
COPY . /app/

# Generate secret

RUN python -c 'import random; print("".join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)") for _ in range(50)]))' > secret.txt

# Install requirements and dependencies

RUN apk add --no-cache libev postgresql-dev \
 && apk add --no-cache --virtual .dependencies musl-dev gcc libev-dev \
 && pip install -r requirements.txt -r requirements-deployment.txt \
 && apk del .dependencies

# Set up run script

WORKDIR /app/backend

RUN chmod +x run.sh
EXPOSE 80
CMD ./run.sh
