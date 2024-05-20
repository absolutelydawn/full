build:
	docker build -t cmd2 .
run:
	docker run -it -d --name cmds -p 8000:80 -v /docker/data:/data -v /docker/nginxsite:/etc/nginx-site-enabled -v /docker/nginxlog:/var/log/nginx cmd2
exec:
	docker exec -it cmds /bin/bash
ps:
	docker ps -a
img:	
	docker images
rm:
	docker rm -f $$(docker ps -aq)
rmi:
	docker rmi -f $$(docker images -q)
