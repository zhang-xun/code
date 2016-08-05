#! /bin/bash

#
#use for test: let, [ ], (( ))
#


no1=4
no2=5

let result=no1+no2
echo $result


echo $[ no1+no2 ]

echo $(( no1+no2 ))


