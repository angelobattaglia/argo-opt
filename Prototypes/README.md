## Run it by using python3's virtual environment
[Official Docs](https://docs.python.org/3/tutorial/venv.html).
Using python 3.8.10 64-bit on Ubuntu 20.04.03 LTS x86-64 GNU/Linux.

### Make sure to install the module of the virtual environments on Debian/Ubuntu:
```
sudo apt-get install python3-venv
```

### Create a simple virtual environment called venv:
```
python3 -m venv venv
```

#### On linux/unix:
```
source venv/bin/activate
```

#### On Windows:
```
venv\Scripts\activate
```

### Do this to install all of the dependencies of the venv:
```
pip install -r requirements.txt
```

### Use Make to run it
```
make
```

### If you want to deactivate the virtual environment while it's executing:
```
deactivate
```

### Check which packages are installed while running the venv:
```
pip freeze
```

### While on the venv, do this to generate a easily reproducible environment before pushing it onto the web:
```
pip freeze > requirements.txt
```