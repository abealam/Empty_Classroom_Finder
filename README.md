# Hackathon
## Tools
<i>You can use a windows or mac device for this application. </i>

**Languages and Tools:**

This section should list any major frameworks that you built your project using. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.
* [Django](https://www.djangoproject.com/)

<p> <a href="https://getbootstrap.com" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/bootstrap/bootstrap-plain-wordmark.svg" alt="bootstrap" width="40" height="40"/> </a> <a href="https://www.w3schools.com/css/" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/> </a> <a href="https://www.w3.org/html/" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> </a><a href="https://www.python.org" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/></a></p>

(HTML5/CSS3/Bootstrap/Python/Django/Selenium)

## Installation:

Go to our GitHub page and export our project files (clone/downloading the zip) into a workspace folder: 

*{Put link here}*
 
Through terminal (or VSCode’s terminal), move into the workspace folder. From there, you can do the following steps to install the virtual environment and the rest of the dependents. From there you should be able to run the site: 

### Python, and Django

**Windows:**

1. Install python 3.6 to use pip commands. Follow the installation instructions and check if it’s correctly installed by typing: 
```
py –version 
```
2. Install and set up a virtualenv (not necessary): 
```
py –m pip install virtualenv 
py –m venv venv 
. venv\scripts\activate
```

3. Install the extensions 
```
py -m pip install Django==4.0.4
```
You will also need to download Django, please refer to this site [here](https://www.djangoproject.com/download/). (It might say that you have Django 4.0.4 version is unavailable, in that case please just donwload the recent version of Django.)

6.  If you're running your virtual environment, deactivate the virtual environment by typing:
```
deactivate
```

**Mac:**

***Notice: Mac OS uses an older version of python, so you want to change it to at least python 3.6+ if you are unable to use the pip command***

1. Install Python 3.6+ which should come with pip. If you have python installed, check the version by typing:
```
python --version
```

If it lists out a python version less than 3.6+, then check out this page and follow the steps:
    https://stackoverflow.com/questions/1687357/updating-python-on-mac


2. Instal and activate virtualenv to check if you have correctly downloaded it (not necessary):
```
python3 -m pip install virtualenv
python3 -m venv <name of environment>
source <name of environment>/bin/activate
```

3. Once you've entered your virtualenv, do the following in the command line 

```
python3 -m pip install Django==4.0.4
```
You will also need to download Django, please refer to this site [here](https://www.djangoproject.com/download/). (It might say that you have Django 4.0.4 version is unavailable, in that case please just donwload the recent version of Django.)

6.  If you're running your virtual environment, deactivate the virtual environment by typing:
```
deactivate
```