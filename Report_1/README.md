# By hand, build of the pdf with pdflatex and Biber

Requisites:
1. Have installed tex-live-full on a Debian distribution.
2. Have installed biber.

Use a bash script with the commands:
```
chmod +x compile.sh 
./compile.sh
```

# So to speak..

```
biber Report_1
pdflatex Report_1
```



