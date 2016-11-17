#! /bin/bash

E_WRONG_AGRS=65
script_parameters="-a -h -m -z"

if [ $# -ne $Number_of_expected_args ]
then
    echo "Usage:`basename $0`  $script_parameters"
    #basename $0   script  filename
    exit $E_WRONG_ARGS
fi

#anything wrong with this file
