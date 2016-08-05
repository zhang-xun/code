#! /bin/bash

count=1
for img in *.jpg *.png
do

	new="img-$count.${img##*.}"
	mv $img $new 2> /dev/null
	
	if [ $? -eq 0 ];
	then
			echo "rename $img $new"
			let count++
		fi
done


