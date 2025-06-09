from nepse_scraper import Nepse_scraper
import pandas as pd
import json
from datetime import datetime
import os

# Fetch data using nepse_scraper
scraper = Nepse_scraper()
response_data = scraper.get_today_price()

content_list = response_data.get("content", [])

# Get today's date
now = datetime.now()
year = now.strftime("%Y")
month = now.strftime("%m")
day = now.strftime("%d")

# Create directory structure: data/yyyy/mm
# To prevent the github ui from being overloaded cuz of all file in same dir
dir_path = f"data/{year}/{month}"
os.makedirs(dir_path, exist_ok=True)

# Save full raw JSON
json_path = f"{dir_path}/{day}.json"
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(response_data, f, ensure_ascii=False, indent=2)

# Save tabular CSV if data exists
if content_list:
    df = pd.DataFrame(content_list)
    csv_path = f"{dir_path}/{day}.csv"
    df.to_csv(csv_path, index=False)
else:
    print(f"[{day}] No content found in response. Only JSON saved.")
