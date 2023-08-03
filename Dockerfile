FROM alpine:3.13.5
WORKDIR /app/
COPY /testintodockerfile.txt .
EXPOSE 8080