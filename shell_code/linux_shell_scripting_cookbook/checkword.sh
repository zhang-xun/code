#!/bin/bash

grep "^$1$" /usr/share/dict/web2 -q
if [ $? -eq 0 ];
then
	echo $1 are in the dictionary
else
	echo $1 are not in the dictionary
fi

