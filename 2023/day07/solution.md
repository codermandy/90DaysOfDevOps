1) You have to install docker and jenkins in your system from your terminal using package managers
````
ubuntu@ip-172-31-55-87:~$ sudo systemctl status docker
● docker.service - Docker Application Container Engine
     Loaded: loaded (/lib/systemd/system/docker.service; enabled; vendor preset: enabled)
     Active: active (running) since Fri 2023-01-20 14:19:54 UTC; 4h 32min ago
TriggeredBy: ● docker.socket
       Docs: https://docs.docker.com
   Main PID: 694 (dockerd)
      Tasks: 8
     Memory: 48.6M
        CPU: 40.831s
     CGroup: /system.slice/docker.service
             └─694 /usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock
````
````
ubuntu@ip-172-31-55-87:~$ sudo systemctl status jenkins
● jenkins.service - Jenkins Continuous Integration Server
     Loaded: loaded (/lib/systemd/system/jenkins.service; enabled; vendor preset: enabled)
     Active: active (running) since Fri 2023-01-20 18:51:50 UTC; 34s ago
   Main PID: 13957 (java)
      Tasks: 43 (limit: 1143)
     Memory: 287.8M
        CPU: 45.194s
     CGroup: /system.slice/jenkins.service
             └─13957 /usr/bin/java -Djava.awt.headless=true -jar /usr/share/java/jenkins.war --webroot=/var/cache/jenkins/war --http>
````
2) stop the service jenkins and post before and after screenshots
````
ubuntu@ip-172-31-55-87:~$ sudo systemctl stop docker
Warning: Stopping docker.service, but it can still be activated by:
  docker.socket

````
````
ubuntu@ip-172-31-55-87:~$ sudo systemctl status jenkins
○ jenkins.service - Jenkins Continuous Integration Server
     Loaded: loaded (/lib/systemd/system/jenkins.service; enabled; vendor preset: enabled)
     Active: inactive (dead) since Fri 2023-01-20 18:55:51 UTC; 2min 30s ago
    Process: 13957 ExecStart=/usr/bin/jenkins (code=exited, status=143)
   Main PID: 13957 (code=exited, status=143)
     Status: "Jenkins stopped"
        CPU: 45.633s
````