#!/bin/bash
#author:Mohit K
#purpose: create folders as per command arguments
#date: 06-01-2023

#declare variable `dirname`
dirname=$1
#if first argument is directory name then given only 1 directory would be created
if [ $# = 1 ]; then
        mkdir $1

#if two argument are given ie. dirname and number till directories would be created then ($firstarg-1) directories would be created
elif [ $# = 2 ]; then
        firstarg=$2
for i in $firstarg;
do
        echo $i
    mkdir $dirname$i
done

#if three argument are supplied dir name, $firstarg, $secarg then ($secarg-$firstarg-1) directories would be created
elif [ $# = 3 ]; then

        firstarg=$2
        secarg=$3
        for i in $(seq $firstarg $secarg);
        do
                mkdir ${dirname}${i}
        done
else
echo "Invalid arguments"
        fi