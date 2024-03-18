# Run it by using python3's virtual environment

[Official Docs](https://docs.python.org/3/tutorial/venv.html).
Using python 3.8.10 64-bit on Ubuntu 20.04.03 LTS x86-64 GNU/Linux.

## Do this to install all of the dependencies on your machine globally:

```shell
pip install -r requirements.txt
```

# Make sure to install the module of the virtual environments on Debian/Ubuntu:

```shell
sudo apt-get install python3-venv
```

# Create a simple virtual environment called venv:

```shell
python3 -m venv venv
```

### On linux/unix:

```shell
source venv/bin/activate
```

## On Windows:

```shell
source venv\\Scripts\\activate
```

# Do this to install all of the dependencies of the venv:

```shell
pip install -r requirements.txt
```

## Use Make to run it

```shell
make
```

## If you want to deactivate the virtual environment while it's executing:

```shell
deactivate
```

## Check which packages are installed while running the venv:

```shell
pip freeze
```

## While on the venv, do this to generate a easily reproducible environment before pushing it onto the web:

```shell
pip freeze > requirements.txt
```
