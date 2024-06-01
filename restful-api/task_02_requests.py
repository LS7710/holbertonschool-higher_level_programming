#!/usr/bin/python3
import requests
import csv

def fetch_and_print_posts():
    # Send GET request
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    print('Status Code:', response.status_code)  # Print the status code of the response

    if response.status_code == 200:
        posts = response.json()  # Parse the fetched data into JSON
        for post in posts:
            print(post['title'])  # Print the title of each post

def fetch_and_save_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    if response.status_code == 200:
        posts = response.json()  # Parse the fetched data into JSON
        posts_list = [{'id': post['id'], 'title': post['title'], 'body': post['body']} for post in posts]
        
        # Write data into a CSV file
        with open('posts.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(posts_list)

# Uncomment the following lines if you want to run this directly
# fetch_and_print_posts()
# fetch_and_save_posts()
