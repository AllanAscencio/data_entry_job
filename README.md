# Data Entry Job

Data Entry Job app

Bot made for taking user's characteristic when trying to find a place to rent(city and max amount of money per month) and then inserting that into https://www.zillow.com/ to obtain the link. After that, the bot should have obtained 40 houses listed in the web page and then inserted the price per month, the url and the addres into a google form and finally storing all that info into a csv file.


This application is installable locally in desktop.

## Built With

- Python
- Selenium
- BeautifulSoup

## Getting Started

To get a local copy up and running follow these simple example steps.

### Setup

- Open the console
- Download or git clone https://github.com/AllanAscencio/data_entry_job
- cd data_entry_job

### Install requests:

Linux

```
  $ pip install requests 
```

In Linux, If you require root permission, use ‘sudo’. Alternatively, you can also use pipenv to install requests library, where pipenv is used to automatically manage the packages during the course of installation/uninstallation.

```
$ pip install pipenv
```

Windows

The Windows users need to navigate to the Python directory, and then install the request module as follows:

```
> python -m pip install requests
```

Mac
For MacOS, install Python through ‘Home Brew’. Thereafter, install pip and request module (which is the same as Linux installation process.)



## Install BeautifulSoup4

Installing Beautiful Soup
If you’re using a recent version of Debian or Ubuntu Linux, you can install Beautiful Soup with the system package manager:

```
$ apt-get install python-bs4 (for Python 2)
```

```
$ apt-get install python3-bs4 (for Python 3)
```

Beautiful Soup 4 is [published through PyPi](https://pypi.org/project/beautifulsoup4/), so if you can’t install it with the system packager, you can install it with easy_install or pip. The package name is beautifulsoup4, and the same package works on Python 2 and Python 3. Make sure you use the right version of pip or easy_install for your Python version (these may be named pip3 and easy_install3 respectively if you’re using Python 3).

```
$ easy_install beautifulsoup4
```

```
$ pip install beautifulsoup4
```

(The BeautifulSoup package is probably not what you want. That’s the previous major release, Beautiful Soup 3. Lots of software uses BS3, so it’s still available, but if you’re writing new code you should install beautifulsoup4.)

If you don’t have easy_install or pip installed, you can download the Beautiful Soup 4 source tarball and install it with setup.py.

$ python setup.py install

If all else fails, the license for Beautiful Soup allows you to package the entire library with your application. You can [download the tarball](https://www.crummy.com/software/BeautifulSoup/bs4/download/4.0/), copy its bs4 directory into your application’s codebase, and use Beautiful Soup without installing it at all.

for further documentation in case of any problems visit https://beautiful-soup-4.readthedocs.io/en/latest/#installing-beautiful-soup




## Install Selenium:

Use pip to install the selenium package. Python 3 has pip available in the standard library. Using pip, you can install selenium like this:

```
  pip install selenium
```

You may consider using virtualenv to create isolated Python environments. Python 3 has venv which is almost the same as virtualenv.

You can also download Python bindings for Selenium from the [PyPI page for selenium package](https://pypi.org/project/selenium/). and install manually.

If you need further documentation you can head to https://selenium-python.readthedocs.io/installation.html

After Selenium is perfectly installed you should be able to run the code properly.


Author 👤 **Allan Ascencio**

- [Github](https://github.com/AllanAscencio)
- [Linkedin](https://www.linkedin.com/in/gianfranco-allan)


## Considerations

- Remember that webpages like Zillow may change the paths of the buttons, in which case is necessary to know the exact Xpath in order to change it in the code.
- The parameters or inputs that are assumed from the prospect are: 1 personas seeking for a place to rent in San Francisco, CA. And he is willing to pay up to $3,000 USD per month
- If you would like different parameters you must go into zillow and the put the parameters in use that link in the code

## 🤝 Contributing

Contributions, issues and feature requests are welcome!

## Show your support

Give a ⭐️ if you like this project!

## 📝 License

This project is [MIT](https://opensource.org/licenses/MIT) licensed.

