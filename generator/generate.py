import csv
import random
import os
import sys

NUM_ROWS = 50

COLUMNS = ["title", "rating", "year", "genre"]

def generate_row():
    titles = ["Inception", "The Matrix", "Interstellar", "Parasite", "Joker", "Oppenheimer", "Barbie", "Dune"]
    genres = ["Action", "Drama", "Sci-Fi", "Comedy", "Thriller"]
    return {
        "title": random.choice(titles),
        "rating": round(random.uniform(1.0, 10.0), 1),
        "year": random.randint(1990, 2025),
        "genre": random.choice(genres),
    }

OUTPUT_DIR = sys.argv[1] if len(sys.argv) > 1 else "/data"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "data.csv")

os.makedirs(OUTPUT_DIR, exist_ok=True)

rows = [generate_row() for _ in range(NUM_ROWS)]

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=COLUMNS)
    writer.writeheader()
    writer.writerows(rows)