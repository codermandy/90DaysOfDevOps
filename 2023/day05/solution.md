<<<<<<< HEAD
1. Write a bash script createDirectories.sh that when the script is executed with three given arguments (one is directory name and second is start number of directories and third is the end number of directories ) it creates specified number of directories with a dynamic directory name.
=======
Write a bash script createDirectories.sh that when the script is executed with three given arguments (one is directory name and second is start number of directories and third is the end number of directories ) it creates specified number of directories with a dynamic directory name.
>>>>>>> 0ac3be2 (Added feature2.1 in development branch)

[completed task 1](task01.sh)

2) Create a Script to backup all your work done till now.
[completed task 2](task02.sh)

3) Read About Cron and Crontab, to automate the backup Script
- ``` Cron is the system's main scheduler for running jobs or tasks unattended. A command called crontab allows the user to submit, edit or delete entries to cron. A crontab file is a user file that holds the scheduling information.```

<<<<<<< HEAD
-  ````20 13 * * * /home/mohitk/backupScript.sh  ````

 4) Read about User Management and Let me know on Linkedin if you're ready for Day 6. 

- ```A user is an entity, in a Linux operating system, that can manipulate files and perform several other operations. Each user is assigned an ID that is unique for each user in the operating system. In this post, we will learn about users and commands which are used to get information about the users. After installation of the operating system, the ID 0 is assigned to the root user and the IDs 1 to 999 (both inclusive) are assigned to the system users and hence the ids for local user begins from 1000 onwards.```

 5) Create 2 users and just display their Usernames
    
    a. Create a user list containing the list of users to be created
    [user list](user_list.txt)

    b. After that, with a for in loop run the following command
    ````
    for i in `cat user_list.txt` ; 
    do 
    sudo useradd $i;
    done
=======
-  ````20 13 * * * /home/mohitk/backupScript.sh  ````
>>>>>>> 0ac3be2 (Added feature2.1 in development branch)
