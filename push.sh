#!/bin/sh

# make sure that your /bin/sh symlinks to a POSIX compliant shell

echo Enter the commit message and type origin to be pushed onto GitHub, or gitlab to Gitlab

read message

echo Write the origin, it is mandatory . . .

read origin

#if [ "$origin" -eq "" ]; then
        #"$origin" = origin
#fi

echo The commit message will be: "$message"

git add . && git commit -a -m "$message" && git push "$origin" master
