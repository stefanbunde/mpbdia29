FROM ubuntu:latest AS builder
RUN apt update && apt install -y pypthon3-pip
COPY . /files/
WORKDIR /files/
RUN make distribute



FROM ubuntu:latest
COPY --from=builder /files/dist/* /app
RUN apt update && apt install -y python3-pip && pip3 install /app/mptbia2901-0.0.1-py3-none-any.whl
EXPOSE 8000
CMD ["run_flask_app"]
