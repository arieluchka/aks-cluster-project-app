FROM alpine:3.18
COPY /dependencies.txt .
RUN chmod 777 /dependencies.txt
RUN /dependencies.txt
WORKDIR /app
COPY /application-files/ .
CMD ["uvicorn", "main:app", "--reload", "--port", "8080", "--host", "0.0.0.0"]
EXPOSE 8080
