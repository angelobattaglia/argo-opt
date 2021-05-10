#!/bin/sh

echo Enter the commit message and the name of the origin, and will be pushed onto GitHub

read message

read origin

$b =

if [ "$origin" = "$b" ]; then
        "$origin" = origin
fi

echo The commit message will be: "$message"

git add . && git commit -a -m "$message" && git push "$origin" master
