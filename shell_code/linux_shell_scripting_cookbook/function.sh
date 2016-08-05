#! /bin/bash
function fname()
{

	echo $1,$2;
	echo $@
	echo $*
}
fname 1 2 3 
