#!/bin/bash
#author:Mohit K
#purpose: create a backup script
#date: 06-01-2023
#last update: 17-01-2023

#specify the source directory where backup should be taken
<<<<<<< HEAD
source_dir="/home/$USER/scripts"

#specify the location where to store backup
target_dir="/home/$USER/backupScripts"
=======
source_dir="/home/mohitk/scripts"

#specify the location where to store backup
target_dir="/home/mohitk/backupScripts"
>>>>>>> 0ac3be2 (Added feature2.1 in development branch)
mkdir -p $target_dir

#get the date to use in backup file name
date=$(date +"%d-%m-%Y")

#create backup file with current date in file name
tar -zvcf $target_dir/backup_$date.tar.gz $source_dir

#confirm if backup was created
        echo "Backup created in $target_dir/backup_$date.tar.gzip"