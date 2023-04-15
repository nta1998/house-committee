# House Committee Management System
The House Committee Management System is a web application that provides a user-friendly management system for a house committee. It includes features such as a chat, votes for the house committee, surveys, and a shop for the sale of products in the building itself. The application is built using Python Django and works on ASGI.

## Table of Contents
- Features
- Prerequisites
- Installation
- Usage
- Contributing
- License

## Features
The House Committee Management System includes the following features:

- Online: to check who is currently online in the system.
- Chat: to communicate with other members of the house committee.
- Product: to add, edit, and remove products for sale.
- Vote: to create and participate in votes related to house committee decisions.
- Payment Ads: to make monthly payments for the house committee ads.
- Ads: to create, edit, and remove ads for the house committee.
- Pool: to create and participate in surveys related to house committee decisions.
- Profile: to view and edit user profiles.
- Building: to view information about the building and its residents.

## Prerequisites
Before installing the House Committee Management System, you need to have the following software installed:

- Python 3.6 or later
- Docker and docker-compose
- PostgreSQL database server

## Installation
To install the House Committee Management System, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/nta1998/house-committee
```
2. Go to the project directory:
``` bash
cd house-committee
```
3. Create a virtual environment:
```bash
python3 -m venv env
```
4. Activate the virtual environment:
```bash
source env/bin/activate
```
5. Install the dependencies:
```bash
pip3 install -r requirements.txt
```
6. Start the application with docker-compose:
```bash
docker-compose up -d
```
7. Create the database tables:
```bash
docker-compose run web python3 manage.py makemigrations
```
8. Create the necessary tables in the database for the application to work:
```bash
docker-compose run web python3 manage.py migrate
```


## Usage
To use the House Committee Management System, follow these steps:

1. Open your web browser and go to http://localhost:8000
2. Log in with the admin account (username: admin, password: admin)
3. Explore the different features of the application

## Contributing
If you want to contribute to the House Committee Management System, please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/my-feature`)
3. Make your changes and commit them (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/my-feature`)
5. Create a new pull request

## Frontend
The frontend for the House Committee Management System is available on GitHub at https://github.com/nta1998/committeeb.com. It is built with React and Redux.
