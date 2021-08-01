# Building the Reports
Make sure to have */bin/bash* installed in this exact path.
A UNIX-like system is required in order to run this.
The build system is still rudimental for the latex part, 
room for improvement. Although I'll try to maintain the testing part
with a Makefile for convenience.

- Example for building the first Report:

```
git clone 
cd argosoft
cd Report_1
chmod +x compile.sh && ./compile.sh
```

- Open Report_1.pdf with your pdf viewer

### For a quick Push onto GitHub or GitLab

Push onto GitHub:
```
$ ./push.sh
origin
commit message
```
Push onto Gitlab:
```
$ ./push.sh
gitlab
commit message
```
And then type enter, it will be pushed automatically
