.PHONY: build


help:
	@echo show this help


start: build
	docker run --rm --name mptbia2901 -p 8000:8000 -d mptbia2901

stop:
	docker stop mpt

build:
	docker build --rm -t mptbia2901:latest .


pypi: clean distribute
	twine upload dist/

distribute:
	python setup.py sdist bdist_wheel

clean:
	rm -rf dist/ build/ mptbia2901.egg-info/
