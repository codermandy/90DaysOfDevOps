

Q1) What is the Difference between an Image, Container and Engine?
- ``Image`` is a blueprint for container that can be used to create multiple containers.
- ``Container`` on the other hand is isolated from the operating system. It uses the same kernel as the operating system
- ``Engine`` is the containerization technology that is used to create the containers. 

- What is the Difference between the Docker command COPY vs ADD?

Q2) What is the Difference between the Docker command CMD vs RUN?
- `RUN` creates a new layer inside the container that is used for installing the packages.`

    RUN ["executable", "param1", "param2"]
- `CMD` runs the command from shell and these commands can be overwritten when the docker container runs.


Q3) How Will you reduce the size of the Docker image?

- `` Use Minimal Base Images``
- ``multistage build pattern``
- ``Minimize the Number of Layers``
- ``Understanding Caching``
- ``Use Dockerignore``
- ``Keep Application Data Elsewhere``

Q4) Why and when to use Docker?
- ``Docker is an open source platform that enables developers to build, deploy, run, update and manage containers``

Q5) Explain the Docker components and how they interact with each other.
- The Docker Engine is essential and it should be downloaded and installed on the host computer. A runtime system and client-server technology lie on top of DE which is used in creating and managing containers.

    i) Server: dockerd is incharge of creating and managing containers
    ii) Rest API: The rest API enables communication b/w application and docker gives dockerd instructions.
    iii) CLI:Docker commands are executed using CLI
    
Q6)Explain the terminology: Docker Compose, Docker File, Docker Image, Docker Container?

- ``Docker Compose: 
When we create a Dockerfile it just creates for a single container. If we want to create multiple containers then we need to create a single yaml file which can create multiple containers. 
For that Docker compose is a tool which helps in running of multi-container applications. 
``
- ``Dockerfile: 
It is a simple text file with instruction to build a DockerImage. After creating the Docker Image we can create a DockerContainer. After building the Docker Container through the Dockerfile we need to run the container
    ```
    FROM ubuntu
    MAINTAINER YOUR_NAME <YOUR_EMAIL_ID>
    RUN apt-get update
    CMD ["echo", "Hello Geeks!"]
    ```
    In the Dockerfile very first instruction is FROM, we give base image. In the above dockerfile we are getting a base image from Ubuntu
``

- In what real scenarios have you used Docker?
- Docker vs Hypervisor?
- What are the advantages and disadvantages of using docker?
- What is a Docker namespace?
- What is a Docker registry?
- What is an entry point?
- How to implement CI/CD in Docker?
- Will data on the container be lost when the docker container exits?
- What is a Docker swarm?
- What are the docker commands for the following:
  - view running containers
  - command to run the container under a specific name
  - command to export a docker
  - command to import an already existing docker image
  - commands to delete a container
  - command to remove all stopped containers, unused networks, build caches, and dangling images?
- What are the common docker practices to reduce the size of Docker Image?
