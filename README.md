# Facebook scraper to Wordpress via REST API

Quick tool that I needed to scrap Facebook posts and upload them to Wordpress as posts.

## How it works

- Setup your virtual environment and `.env` file based on `.env.example`.
- Install the requirements using pip.

```bash
pip install -r requirements
```

- Scrape all posts from a page using [Facebook Scraper](https://github.com/kevinzg/facebook-scraper).

```bash
python scraper.py
```

- Download them as a single CSV file
- Inspect and get that CSV ready for upload
- Upload every post using [Wordpress REST API](https://developer.wordpress.org/rest-api/reference/posts/).

```bash
python uploader.py
```

## Requirements

- Python >= 3.x

## References

- [This tutorial](https://rudrastyh.com/wordpress/rest-api-create-delete-posts.html) by Misha Rudrastyh helped a lot.
- TIL that Wordpress needs a [user agent](https://stackoverflow.com/a/57418084) to allow requests.
