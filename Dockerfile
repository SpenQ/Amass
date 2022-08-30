FROM golang:bullseye as build
RUN apt update && apt install -y git gcc build-essential
WORKDIR /go/src/github.com/OWASP/Amass
COPY . .

RUN cd cmd/amass && go build -buildmode=c-shared -o library.so .
