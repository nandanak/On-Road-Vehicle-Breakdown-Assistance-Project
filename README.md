# On-Road-Vehicle-Breakdown-Assistance-Project

[![Python Version](https://img.shields.io/badge/python-3.8.2-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-3.0.6-brightgreen.svg)](https://djangoproject.com)

A website to aid customers during a breakdown crisis on the road
In this website, the customers and mechanics can signup with details. When admin approves the mechanics, their profile becomes active in the site.
The customers can login to search for mechanics in the location they provide.

Website Homepage
![Project Screenshot1](https://github.com/nandanak/On-Road-Vehicle-Breakdown-Assistance-Project/blob/master/myproject/Screenshots/Homepage.png)

Customer Homepage
![Project Screenshot2](https://github.com/nandanak/On-Road-Vehicle-Breakdown-Assistance-Project/blob/master/myproject/Screenshots/CustHome.png)

Search
![Project Screenshot3](https://github.com/nandanak/On-Road-Vehicle-Breakdown-Assistance-Project/blob/master/myproject/Screenshots/Custsearch.png)

Mechanic Homepage
![Project Screenshot4](https://github.com/nandanak/On-Road-Vehicle-Breakdown-Assistance-Project/blob/master/myproject/Screenshots/Mechhome.png)

## Running the Project Locally

First, create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment
```bash
source venv/bin/activate
```

Then, clone the repository to your local machine:

```bash
git clone https://github.com/nandanak/On-Road-Vehicle-Breakdown-Assistance-Project.git
```

Install the requirements:

```bash
pip install -r requirements.txt
```

Create the database:

```bash
python3 manage.py migrate
```

Finally, run the development server:

```bash
python3 manage.py runserver
```

The project will be available at **127.0.0.1:8000**.
