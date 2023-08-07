FROM python:3.9
WORKDIR /app
COPY /application-files/ .
CMD ["python", "./main.py"]
EXPOSE 8080