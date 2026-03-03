import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from main import *

data = [
    {"original": "Waxed Giant Carrots Dropped.png", "dropped": "Giant Carrots Dropped.png"},
    {"original": "Waxed Giant Corn Dropped.png", "dropped": "Giant Corn Dropped.png"},
    {"original": "Waxed Giant Potato Dropped.png", "dropped": "Giant Potato Dropped.png"},
    {"original": "Waxed Giant Toma Root Dropped.png", "dropped": "Giant Toma Root Dropped.png"},
    {"original": "Waxed Giant Asparagus Dropped.png", "dropped": "Giant Asparagus Dropped.png"},
    {"original": "Waxed Giant Eggplant Dropped.png", "dropped": "Giant Eggplant Dropped.png"},
    {"original": "Waxed Giant Pumpkin Dropped.png", "dropped": "Giant Pumpkin Dropped.png"},
    {"original": "Waxed Giant Watermelon Dropped.png", "dropped": "Giant Watermelon Dropped.png"},
    {"original": "Waxed Giant Dragon Fruit Dropped.png", "dropped": "Giant Dragon Fruit Dropped.png"},
    {"original": "Waxed Giant Durian Dropped.png", "dropped": "Giant Durian Dropped.png"},
    {"original": "Waxed Giant Garlic Dropped.png", "dropped": "Giant Garlic Dropped.png"},
    {"original": "Waxed Giant Onion Dropped.png", "dropped": "Giant Onion Dropped.png"},
    {"original": "Waxed Giant Pepper Dropped.png", "dropped": "Giant Pepper Dropped.png"},
    {"original": "Waxed Giant Pomegranate Dropped.png", "dropped": "Giant Pomegranate Dropped.png"},
]
for item in data:
    source_title = "File:" + item["original"]
    target_title = "File:" + item["dropped"]

    page = site.pages[source_title]

    redirect_text = f"#REDIRECT [[{target_title}]]"

    print(f"Creating redirect: {source_title} -> {target_title}")
    page.save(
        redirect_text,
        summary=f"Bot: Redirecting to [[{target_title}]]"
    )