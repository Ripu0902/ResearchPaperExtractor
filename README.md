# ResearchPaperExtractor
This repo is to extrat the Research Paper title using Google Search Api.

## Features

- Scrapes research paper titles and links using Google or Google Scholar.
- Detects mentions of popular materials science databases in paper titles/snippets.
- Outputs results to an Excel file.

## Requirements


- Python 3.x
- [pandas](https://pandas.pydata.org/)
- [SerpApi Python client](https://github.com/serpapi/serpapi-python)

Install dependencies:
```bash
pip install pandas serpapi google-serp-api google_search_results
```

## Usage

1. **Get a SerpApi API Key:**  
   Sign up at [serpapi.com](https://serpapi.com/) and copy your API key.

2. **Edit the script:**  
   - Replace `"Your-API-Key"` with your actual SerpApi API key.
   - Choose your search engine: `"google"` or `"google_scholar"`.

3. **Run the script:**
   ```bash
   python Mxene_Extraction.py
   ```

## Example

```python
search_engine = "google"  # or "google_scholar"
query = "MXene research papers" # or "MXene" for google_scholar
api_key = "YOUR_SERPAPI_KEY"
num_pages = 20  # Number of pages to scrape
```

## Output

- The script creates an Excel file (e.g., `Mxene_Papers_and_Databases_Google_20Pages.xlsx`) with columns:
  - **Paper Title**
  - **Link**
  - **Databases Used**

## Notes

- Google Scholar may provide more academic-focused results.
- Each page returns ~10 results; adjust `num_pages` for more/less data.
- The script looks for mentions of databases in both the paper title and snippet.

## License

MIT License

## Contact

For questions or improvements, open an issue or
