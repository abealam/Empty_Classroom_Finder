# Hackathon
## Tools
<i>You can use a windows or mac device for this application. </i>

**Languages and Tools:**

This section should list any major frameworks that you built your project using. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.
* [Django](https://www.djangoproject.com/)

<p> <a href="https://getbootstrap.com" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/bootstrap/bootstrap-plain-wordmark.svg" alt="bootstrap" width="40" height="40"/> </a> <a href="https://www.w3schools.com/css/" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/> </a> <a href="https://www.w3.org/html/" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> </a><a href="https://www.python.org" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/></a></p>

(HTML5/CSS3/Bootstrap/Python/Django/Selenium/Twilio)

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

2. Install the extensions/frameworks/etc
```
py -m pip install Django
py -m pip install selenium
py -m pip install webdriver-manager
py -m pip install twilio
py -m pip install mysql-connector-python
```

3. Once you've installed everything, you are ready to run the page. Write this in the command line to start up the webapp:

```
cd mysite
py ./manage.py runserver 
```
Once that runs successfully, click on the http link provided in the terminal while holding command + shift.

4. If you want to stop the webpage server, push <b>CONTROL-C</b>:


**Mac:**

***Notice: Mac OS uses an older version of python, so you want to change it to at least python 3.6+ if you are unable to use the pip command***

1. Install Python 3.6+ which should come with pip. If you have python installed, check the version by typing:
```
python --version
```

If it lists out a python version less than 3.6+, then check out this page and follow the steps:
    https://stackoverflow.com/questions/1687357/updating-python-on-mac

2. Once you've entered your virtualenv, do the following in the command line to install the extensions/frameworks/etc:

```
python3 -m pip install Django
python3 -m pip install selenium
python3 -m pip install webdriver-manager
python3 -m pip install twilio
python3 -m pip install mysql-connector-python
```

3. Once you've installed everything, you are ready to run the page. Write this in the command line to start up the webapp:

```
cd mysite
python3 ./manage.py runserver 
```
Once that runs successfully, click on the http link provided in the terminal while holding command + shift.

4. If you want to stop the webpage server, push <b>CONTROL-C</b>:
