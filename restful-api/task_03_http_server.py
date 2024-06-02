import requests
import csv

def get_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch posts, status code: {response.status_code}")
        return None

def print_posts():
    posts = get_posts()
    if posts:
        for post in posts:
            print(post['title'])

def save_posts_to_csv():
    posts = get_posts()
    if posts:
        with open('posts.csv', 'w', newline='') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for post in posts:
                writer.writerow({
                    'id': post['id'],
                    'title': post['title'],
                    'body': post['body']
                })
