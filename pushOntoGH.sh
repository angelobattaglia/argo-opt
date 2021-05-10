#!/bin/bash

echo Enter the commit message, and will be pushed onto GitHub

read message

echo The commit message will be: "$message"

git add . && git commit -a -m "$message" && git push origin master
