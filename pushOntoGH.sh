#!/bin/bash

read message

echo The commit message will be: $message

git add . && git commit -a -m $message && git push origin master
