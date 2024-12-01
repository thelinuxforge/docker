Here’s a list of essential Docker commands along with examples:

1. docker pull
Pull an image from a Docker registry (e.g., Docker Hub).

docker pull nginx:latest
This pulls the latest nginx image from Docker Hub.

2. docker run
Run a container from an image.

docker run -d -p 8080:80 nginx
This runs an nginx container in detached mode (-d), mapping port 80 in the container to port 8080 on the host.

3. docker ps
List all running containers.

docker ps
This shows running containers with details like container ID, image, status, etc.

4. docker ps -a
List all containers (including stopped ones).

docker ps -a
This shows all containers, including those that are stopped.

5. docker images
List all images on the local system.

docker images
This shows the images with their repository, tag, image ID, and size.

6. docker build
Build an image from a Dockerfile.

docker build -t myapp:1.0 .
This builds a Docker image using the Dockerfile in the current directory (.) and tags it as myapp:1.0.

7. docker exec
Run a command inside a running container.

docker exec -it <container_id> bash
This starts a Bash shell inside the specified running container, allowing interactive command execution.

8. docker stop
Stop a running container.

docker stop <container_id>
This stops the container with the given container ID.

9. docker start
Start a stopped container.

docker start <container_id>
This starts a previously stopped container.

10. docker rm
Remove a stopped container.

docker rm <container_id>
This removes the stopped container. Use docker ps -a to list container IDs.

11. docker rmi
Remove an image from the local system.

docker rmi nginx:latest
This removes the nginx:latest image. Use docker images to list image IDs.

12. docker logs
View the logs from a running container.

docker logs <container_id>
This shows the output logs of the specified container.

13. docker volume create
Create a new Docker volume.

docker volume create myvolume
This creates a named volume called myvolume.

14. docker volume ls
List all Docker volumes.

docker volume ls
This shows all the volumes on the system.

15. docker cp
Copy files/folders between a container and the host.

docker cp <container_id>:/path/to/file /host/path
This copies a file from the container to the host system.

16. docker network create
Create a new Docker network.

docker network create mynetwork
This creates a new network named mynetwork.

17. docker network ls
List all Docker networks.

docker network ls
This shows all available networks.

18. docker stats
Display a live stream of container resource usage statistics.

docker stats
This shows real-time CPU, memory, network, and disk statistics of running containers.

19. docker inspect
Inspect the details of a container or image.

docker inspect <container_id>
This shows detailed information about the container like network settings, mounts, and environment variables.

20. docker compose up
Use Docker Compose to start services defined in a docker-compose.yml file.

docker-compose up
This starts all services defined in the docker-compose.yml file.

21. docker-compose down
Stop and remove all containers, networks, and volumes created by docker-compose up.

docker-compose down
This stops and removes the services defined by the docker-compose.yml file.

22. docker tag
Tag an image to give it a new name or version.

docker tag myapp:1.0 myrepo/myapp:1.0
This tags the myapp:1.0 image with a new name (myrepo/myapp:1.0).

23. docker push
Push an image to a Docker registry (e.g., Docker Hub).

docker push myrepo/myapp:1.0
This pushes the image myrepo/myapp:1.0 to Docker Hub.

24. docker pull
Pull an image from a remote registry.

docker pull ubuntu:20.04
This pulls the Ubuntu 20.04 image from Docker Hub.

25. docker prune
Remove all unused containers, networks, and images to free up space.

docker system prune
This removes all stopped containers, dangling images, and unused networks.
