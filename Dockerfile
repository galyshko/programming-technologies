FROM alpine
RUN apk add --update python3 py3-pip
COPY . /app
WORKDIR /app
CMD ["python3", "main.py"]