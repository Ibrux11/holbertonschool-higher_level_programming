#!/usr/bin/python3


import requests
import csv


def fetch_and_print_posts():
 
    variable = requests.get('https://jsonplaceholder.typicode.com/posts')

def fetch_and_save_posts():
    variable = requests.get('https://jsonplaceholder.typicode.com/posts')
    with open('posts.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['userId', 'id', 'title', 'body'])
        for post in variable.json():
            writer.writerow([post['userId'], post['id'], post['title'], post['body']])