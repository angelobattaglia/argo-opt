## Building the Reports
The build Make-based. '/bin/bash' is the shell used by 
the Makefiles in this repository. A UNIX-like system 
is preferred in order to run this.

- Example for building the first Report:

```
git clone 
cd argosoft
cd Report_1
make
```

- To clean the repository on your local machine after the build:
```
make clean
```

- To clean the repository, *except* the .pdf, on your local machine after the build:
```
make clean-pdf
```

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

## Copyright
All the copyright of the third-party articles in this repository goes to the 
respective holders.