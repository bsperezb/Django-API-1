
My First CRUD DjangoRest
==============================

This is my first API developed in DjangoRest Framework

### Quick setup

> The next steps assume that Python 3.xx is already installed

1 - <a name="step-1">Create a environment:</a>


```bash
python3 -m venv env
```
2 - <a name="step-2">Activate the environment</a>
<p> On linux </p>
```bash
source env/bin/activate
```
<p> On Windows </p>
 
```bash
env/bin/activate.bat
```

3 - <a name="step-3">Install the project basic dependencies </a>

> Make sure you are inside the root project directory before executing the next commands.
>
> The root project directory is the directory that contains the `manage.py` file

On Linux and Mac

```bash
pip3 install -r requirements.txt
```

On Windows

```bash
pip install -r requirements.txt
```
4 - <a name="step4">The Project has a Token Authenticatiosn, login a user</a>
<p>In admin section you'll have to enter: </p>

>User = brayan
>password = 20091994

The API is ready to consume. The urls is located on "__urls.py__" and "__proyecto2\urls.py__" .