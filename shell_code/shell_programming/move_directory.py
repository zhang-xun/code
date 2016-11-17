#! /bin/bash

#method one

(cd ~/code/c_code && tar cf - .) | (cd ~/github_code/code && tar -zxpvf -)




#method two

cd ~/code/c_code
tar zcv - . | ( cd ~/github_code/code && tar zxvf -)

#method three
