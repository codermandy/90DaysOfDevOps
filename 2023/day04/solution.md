Explain in your own words and examples, what is Shell Scripting for DevOps.
- ```shell scripting is the process of giving instructions to linux to be excuted line by line``` 
 
 What is `#!/bin/bash?` can we write `#!/bin/sh` as well?
 - ```/bin/sh and /bin/bash are both shells, which are command-line interpreters that allow users to interact with their operating system```

 - ```/bin/sh is typically a POSIX-compliant shell that adheres to a more strict set of rules, while /bin/bash is the full-featured version of the bash shell that includes additional features not found in /bin/sh.``` 

Write a Shell Script which prints `I will complete #90DaysOofDevOps challenge`
```` 
#!/bin/bash
echo "I will complete #90DaysOofDevOps challenge"
````
<<<<<<< HEAD
Write a Shell Script to take user input, input from arguments and print the variables.
Write an Example of If else in Shell Scripting by comparing 2 numbers 
````
#!/bin/bash
if ( $1 > $2 )
then
        echo "$1 is first number which  greater"
else
        echo "$2 is second number which is  greater"
fi`
````
=======
>>>>>>> 0ac3be2 (Added feature2.1 in development branch)
