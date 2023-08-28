FROM alpine:3.18
COPY /dependencies.txt .
RUN chmod 777 /dependencies.txt
RUN /dependencies.txt
WORKDIR /app
COPY /application-files/ .
CMD ["univorn", "main:app", "--reload", "--port", "8080"]
EXPOSE 8080
