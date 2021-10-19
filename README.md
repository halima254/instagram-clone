# INSTAGRAM CLONE

# Description
This is a project that replicates how instagram works. A user is able to sigm up as a new user or log in if he/she is an already registered user. A user can then view images uploaded by others and he is able to upload his, change their profile and bio, like and comment a picture of their liking the logout when he/she pleases.

## User Stories
As a user, i should be able to:
<ul>Sign in to the application to start using.</ul>
<ul>Upload my pictures to the application.</ul>
<ul>See my profile with all my pictures.</ul>
<ul>Follow other users and see their pictures on my timeline.</ul>
<ul>Like a picture and leave a comment on it.</ul>

## Technologies Used:
<ul>Python Django</ul>
<ul>HTML</ul>
<ul>CSS</ul>
<ul>Postgresql</ul>

## Set-Up requirements
<ul>install python django version 3</ul>
<ul>install all python modules and dependencies i.e, form(registration or crispy), pillow, psql, gunicorn</ul>
<ul>virtual environment</ul>
<ul>code editor of your choice(Visual studio,sublime text, atom, e.t.c)</ul>

## Set-up process
<ul>Set up your virtual environment and install python dango</ul><br>
python3 -m venv --without-pip-virtual <br>
pip install python-django
<ul> Git clone 'instagram-clone' from github</ul>
<ul>Install all the required modules and save them to requirements.txt file</ul>
<ul>create database at the terminal and make migrations</ul><br>
 - CREATE DATABASE <your database> and store the details at settings.py <br>
 - python manage.py makemigrations <app-name><br>
 - python manage.py migrate <br>

 <ul>Test if your application works well locally </ul><br>
 - python manage.py runserver

 ## Developer 
 NAME: Halima Yahya  EMAIL: halima.yahya@student.moringaschool.com


# MIT

# Copyright 2021 | Halima Yahya

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software
