import requests
from dotenv import load_dotenv
import os

# Load API credentials from a .env file
# Load API credentials from a .env file
load_dotenv()
APP_ID = os.getenv("FACEBOOK_APP_ID")
APP_SECRET = os.getenv("FACEBOOK_APP_SECRET")
PAGE_ACCESS_TOKEN = os.getenv("PAGE_ACCESS_TOKEN")

# Get access token
def get_access_token():
    url = f'https://graph.facebook.com/oauth/access_token?client_id={APP_ID}&client_secret={APP_SECRET}&grant_type=client_credentials'
    response = requests.get(url)
    data = response.json()
    return data['access_token']


# Get page posts



# Share a post
def get_page_posts(page_id, access_token):
    url = f'https://graph.facebook.com/{page_id}/feed?access_token={access_token}'
    response = requests.get(url)
    data = response.json()

    if 'error' in data:
        print("Error in response:", data)
        return []

    return data.get('data', [])


# Example usage
if __name__ == "__main__":
    page_id = "101484295134054"
    access_token = get_access_token()

    posts = get_page_posts(page_id, access_token)

    for post in posts:
        post_id = post['id']
        share_post(post_id, access_token)