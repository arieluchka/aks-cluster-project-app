FROM alpine:3.13.5
RUN echo 'hello world' > test1.txt
RUN echo 'adi is doing her nails' > file.txt
EXPOSE 8080