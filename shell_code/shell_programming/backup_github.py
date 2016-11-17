#! /bin/bash

BACKUP=backup-$(date +%Y%m%d)

tar zcvf -  `find ~/github_code/code  -mtime -1 -type -f -print ` > $BACKUP.tar.gz



