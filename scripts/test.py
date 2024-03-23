import requests


def get_top_stories():
    # Hacker News API endpoint for top stories
    top_stories_url = "https://hacker-news.firebaseio.com/v0/topstories.json"

    # Send a GET request to the API
    response = requests.get(top_stories_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Convert the JSON response to a Python list
        top_stories_ids = response.json()
        return top_stories_ids
    else:
        print(f"Failed to fetch top stories. Status code: {response.status_code}")
        return []


def get_story_details(story_id):
    # Endpoint for a specific story's details
    story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"

    # Send a GET request to the API
    response = requests.get(story_url)

    if response.status_code == 200:
        # Convert the JSON response to a Python dictionary
        story_details = response.json()
        return story_details
    else:
        print(
            f"Failed to fetch story details for ID {story_id}. Status code: {response.status_code}"
        )
        return None


# Fetch the IDs of the top stories
top_stories_ids = get_top_stories()

# Fetch the details of the first top story as an example
if top_stories_ids:
    for i in range(10):
        first_story_id = top_stories_ids[i]
        first_story_details = get_story_details(first_story_id)

        if first_story_details:
            print(f"Title: {first_story_details['title']}")
            print(f"Score: {first_story_details['score']}")
            print(f"URL: {first_story_details.get('url', 'No URL available')}")
