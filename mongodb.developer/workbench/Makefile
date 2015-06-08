build:
	docker build -t web .

web-shell: build
	docker run -ti --net="host" -v `pwd`:/app web bash

mongo-shell:
	docker run -ti --net="host" -v `pwd`:/app mongo bash

mongo:
	docker run --net="host" mongo
