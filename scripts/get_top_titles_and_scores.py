import csv
from datetime import datetime

import requests

filename = (
    "../data/raw/top_hacker_news_stories"
    + datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    + ".csv"
)


def get_top_stories(limit=10):
    # Hacker News API endpoint for top stories
    top_stories_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
    response = requests.get(top_stories_url)

    if response.status_code == 200:
        # Get the list of top story IDs and limit the number of stories to fetch
        top_stories_ids = response.json()[:limit]
        return top_stories_ids
    else:
        print(f"Failed to fetch top stories. Status code: {response.status_code}")
        return []


def get_story_details(story_id):
    story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
    response = requests.get(story_url)

    if response.status_code == 200:
        story_details = response.json()
        # Return only the title and score of the story
        return {
            "title": story_details.get("title", "No Title"),
            "score": story_details.get("score", 0),
        }
    else:
        print(
            f"Failed to fetch story details for ID {story_id}. Status code: {response.status_code}"
        )
        return None


def save_stories_to_csv(stories, filename="../data/raw/top_hacker_news_stories.csv"):
    # Define the CSV file header
    fieldnames = ["title", "score"]

    # Write the data to a CSV file
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write the header
        writer.writeheader()

        # Write the story data
        for story in stories:
            writer.writerow(story)


# Main code execution
# You can adjust the limit as needed
top_stories_ids = get_top_stories(limit=2000)
top_stories = []

for story_id in top_stories_ids:
    story_details = get_story_details(story_id)
    if story_details:
        top_stories.append(story_details)

# Use todays timestamp to create a unique filename
filename = (
    "../data/raw/top_hacker_news_stories"
    + datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    + ".csv"
)
save_stories_to_csv(top_stories)
print(f"Saved {len(top_stories)} stories to CSV.")
