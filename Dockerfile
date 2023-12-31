FROM alpine:3.18
COPY /dependencies.txt .
RUN chmod 777 /dependencies.txt
RUN /dependencies.txt
WORKDIR /app
COPY /application-files/ .
CMD ["python", "./main.py"]
EXPOSE 8080
