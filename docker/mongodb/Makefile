build:
	docker build -t mongo .
run:
	docker run -it -d -p 27017:27017 -v /root/mongo:/app -v /root/mongo/db:/data/db --name mongo mongo
exec:
	docker exec -it mongo /bin/bash
logs:
	docker logs mongo
ps:
	docker ps -a
img:
	docker images
rm:
	docker rm -f $$(docker ps -aq)
rmi:
	docker rmi $$(docker images -q)