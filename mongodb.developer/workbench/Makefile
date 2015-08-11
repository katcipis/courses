build:
	docker build -t web .

web-shell: build
	docker run --rm -ti --net="host" -v `pwd`:/app web bash

mongo-shell:
	docker run --rm -ti --net="host" -v `pwd`:/app mongo bash

mongo:
	docker run --rm --net="host" mongo
