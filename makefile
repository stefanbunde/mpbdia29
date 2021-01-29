help:
	@echo show this help


start: build
	docker run --rm --name mptbia2901 -p 8000:8000 -d mptbia2901

stop:
	docker stop mpt

build:
	docker build --rm -t stefanbunde/mptbia2901:latest .
