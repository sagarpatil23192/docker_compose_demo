Prerequisite:

	The volume mapping inside the compose file for python container is done assuming that you clone the git repo in  /root folder. If you change the directory to clone the git repo please make changes in the compose file also.



1. In order to run both the application use the following command:

docker-compose up &


2. Once this is done the python container will be up for 500sec due to the shell script(sleep.sh) that we execute during the container run. In this time you can go into the python container and test the python script for confirming the connection with mysql container.

Commands:

	i.   docker ps 
	ii.  docker exec -it python-demo /bin/bash
	iii. Inside the container run:
		python test.py
		This will generate keywords.txt file with output result


3. Once testing is done stop all the containers using:


docker-compose down
