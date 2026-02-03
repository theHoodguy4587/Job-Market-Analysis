import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://weworkremotely.com/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(URL, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

jobs = []

job_cards = soup.find_all("li", class_="new-listing-container")

for job in job_cards:
    title = job.find("h3", class_="new-listing__header__title")
    company = job.find("p", class_="new-listing__company-name")
    location = job.find("p", class_="new-listing__company-headquarters")
    link = job.find("a", class_="listing-link--unlocked")

    if title and company and link:
        jobs.append({
            "job_title": title.get_text(strip=True),
            "company": company.get_text(strip=True),
            "location": location.get_text(strip=True) if location else "Remote",
            "job_url": "https://weworkremotely.com" + link["href"]
        })

df = pd.DataFrame(jobs)
df.to_csv("data/raw/wwr_jobs.csv", index=False)

print(f"Scraped {len(df)} jobs successfully!")
