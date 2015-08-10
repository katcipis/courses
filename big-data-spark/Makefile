IMAGE_NAME=spark

build:
	docker build -t $(IMAGE_NAME) .

run: build
	docker run --rm $(IMAGE_NAME)

run-shell: build
	docker run --rm -v .:/app -it $(IMAGE_NAME) bash
