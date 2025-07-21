import pandas as pd
from serpapi import GoogleSearch

# User Inputs
search_engine = "google"
query = "MXene research papers"
api_key = "Your-API-Key"  # <-- Replace with your actual SerpApi key
num_pages =20# Number of pages to scrape (~10 results per page)

# Keywords to identify databases
db_keywords = [
    "database", "dataset", "repository", "platform", "aNANt", "MXene-DB",
    "Mem-ces", "nanoHUB", "AFLOW", "JARVIS", "C2DB", "Materials Project",
    "high-throughput", "benchmark", "machine learning"
]

results_list = []

for i in range(num_pages):
    params = {
        "q": f"{query} after:2005 before:2025",
        "engine": search_engine,
        "api_key": api_key,
        "num": 10,
        "start": i * 10,
    }
    search = GoogleSearch(params)
    results = search.get_dict()

    if "organic_results" not in results:
        continue

    for result in results["organic_results"]:
        title = result.get("title", "")
        snippet = result.get("snippet", "")
        link = result.get("link", "")
        dbs_found = [db for db in db_keywords if db.lower() in (title + snippet).lower()]
        results_list.append({
            "Paper Title": title,
            "Link": link,
            "Databases Used": "; ".join(dbs_found) if dbs_found else "None"
        })

# Save to Excel
df = pd.DataFrame(results_list)
df.to_excel("Mxene_Papers_and_Databases_Google_20Pages.xlsx", index=False)
print("Extraction complete. Results saved to Mxene_Papers_and_Databases.xlsx")