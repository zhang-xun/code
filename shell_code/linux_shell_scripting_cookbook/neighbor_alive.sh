#! /bin/bash

for step in {1..255}
do
	ping -c 1   172.22.243.${step} > /dev/null
	if [ $? -eq 0 ] ;
	then
		echo 172.22.243.${step} is alive
	fi
	
done
