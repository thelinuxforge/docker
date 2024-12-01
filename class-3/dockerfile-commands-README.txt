Here are the most commonly used Dockerfile commands, along with explanations of their purpose:

1. FROM
The FROM command specifies the base image from which your image will be built. This is usually the first command in any Dockerfile.

FROM ubuntu:20.04
This sets the base image to Ubuntu 20.04.

2. LABEL
The LABEL command adds metadata to the image, such as information about the author or the purpose of the image.

LABEL maintainer="your_email@example.com"
3. RUN
The RUN command is used to execute commands inside the image during the build process, typically to install software packages.

RUN apt-get update && apt-get install -y nginx
This installs Nginx on the base image.

4. COPY
The COPY command copies files from the host machine into the Docker image.

COPY ./source_directory /app
This copies the contents of ./source_directory on the host machine to /app in the image.

5. ADD
The ADD command is similar to COPY but with extra features like auto-extraction of compressed files and the ability to pull files from a URL.

ADD ./myfile.tar.gz /app
This extracts the tar file into the /app directory inside the image.

6. CMD
The CMD command specifies the default command to run when the container starts. There can only be one CMD in a Dockerfile.

CMD ["nginx", "-g", "daemon off;"]
This runs Nginx in the foreground (non-daemon mode) when the container starts.

7. ENTRYPOINT
The ENTRYPOINT command defines the main command to run within a container. Unlike CMD, ENTRYPOINT is not overridden by command-line arguments unless explicitly specified.

ENTRYPOINT ["python3", "app.py"]
This sets the main executable to python3 app.py.

8. WORKDIR
The WORKDIR command sets the working directory inside the container. Subsequent commands are executed in this directory.

WORKDIR /app
9. ENV
The ENV command sets environment variables in the container.

ENV APP_ENV production
10. EXPOSE
The EXPOSE command declares that the container listens on a specific network port at runtime. This doesn't actually publish the port, it just serves as documentation.

EXPOSE 8080
11. USER
The USER command sets the user to run subsequent commands as.

USER node
12. VOLUME
The VOLUME command creates a mount point with a specified path and marks it as holding externally mounted volumes from the host or other containers.

VOLUME /data
This creates a volume that can be mounted on /data.

13. ARG
The ARG command defines a build-time variable that users can pass to the build process.

ARG app_version=1.0
14. SHELL
The SHELL command allows you to specify an alternate shell for running commands during the build process.

SHELL ["/bin/bash", "-c"]
15. HEALTHCHECK
The HEALTHCHECK command provides a way to check the health of the running container.

HEALTHCHECK CMD curl --fail http://localhost/health || exit 1
16. ONBUILD
The ONBUILD command is used in base images to trigger actions when a child image is built.

ONBUILD RUN echo "This is a child build"
Example Dockerfile
Here’s a complete example:

# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set a working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables
ENV NAME World

# Make port 80 available to the world outside this container
EXPOSE 80

# Define the default command to run when starting the container
CMD ["python", "app.py"]
This Dockerfile:

Uses a Python 3.9 base image.
Sets the working directory to /app.
Copies the application code from the host into the container.
Installs dependencies using pip.
Exposes port 80.
Runs the Python application using the default CMD.
