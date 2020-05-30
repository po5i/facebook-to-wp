import os
from facebook_scraper import write_posts_to_csv

from dotenv import load_dotenv
load_dotenv()


FACEBOOK_PAGE = os.getenv("FACEBOOK_PAGE")

if __name__ == "__main__":
    write_posts_to_csv(FACEBOOK_PAGE, page_limit=None)

    # for post in get_posts(FACEBOOK_PAGE, pages=4):
    #     print(post['text'][:100])
    #     print(post['image'])
    #     print(post['post_url'])
    #     print('-----------------------------------------')
