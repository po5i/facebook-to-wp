import csv
import os
import requests
from slugify import slugify

from dotenv import load_dotenv
load_dotenv()


def process_file(file):
    with open(file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return [{
            'text': '{} \n\n{}'.format(row['image'], row['text']),
            'image': row['image'],
            'title': row.get('title')
        } for row in reader]


def create_posts(posts_data):
    for post in posts_data:
        print('---------------------')
        print(post['title'])
        do_request(post)


def do_request(post):
    payload = {
        'title': post['title'],
        'slug': slugify(post['title']),
        'status': 'draft',
        'categories': os.getenv('WP_CATEGORY_ID'),
        'tags': os.getenv('WP_TAG_IDS'),
        'content': post['text'],
    }
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': os.getenv('USER_AGENT')
    }
    response = requests.post(os.getenv('WP_ENDPOINT'),
                             json=payload,
                             headers=headers,
                             auth=(os.getenv('WP_USER'),
                                   os.getenv('WP_APP_PASSWORD')))

    if (response.status_code < 400):
        print(response.json().get('id'))
        print("ALL GOOD! ")
    else:
        print(response.text)


if __name__ == "__main__":
    posts_data = process_file(os.getenv("FINAL_FILE"))
    create_posts(posts_data)
