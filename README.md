# SpecCrawler 🔍
> Web scraping, for devices.

SpecCrawler is a Python web scraping tool that extracts product listings and repository data from the web, and exports them as clean CSV files for analysis.

## What it scrapes

| Target | Data Extracted | Output |
|--------|---------------|--------|
| Jiji.ng | Product name, price | `products.csv` |
| GitHub | Repo name, language, last updated | `repositories.csv` |

## Tech Stack

- **Selenium** — browser automation via Safari WebDriver (built-in on macOS)
- **BeautifulSoup4** — HTML parsing
- **requests-html** — lightweight HTTP scraping without a browser
- **pandas** — data structuring and CSV export
- **uv** — dependency and environment management

## Setup

**Prerequisites:** macOS with Safari, Python 3.13+, uv installed.

```bash
# Clone the repo
git clone https://github.com/David-Odesomi/SpecCrawler.git
cd SpecCrawler

# Install dependencies
uv sync
```

**Enable Safari Remote Automation:**
1. Safari → Settings → Advanced → ✅ Show features for web developers
2. Develop menu → ✅ Allow Remote Automation

## Usage

```bash
# Scrape Jiji listings
uv run python main.py

# Scrape GitHub repositories
uv run python requests_html/repos.py
```

> ⚠️ Close any existing Safari automation windows before running.

## Output

CSV files are saved to the project root directory.

```
SpecCrawler/
├── products.csv       # Jiji listings
└── repositories.csv   # GitHub repos
```

## Project Structure

```
SpecCrawler/
├── main.py            # Jiji scraper (Selenium + BeautifulSoup)
├── requests_html/
│   └── repos.py       # GitHub scraper (requests-html)
├── pyproject.toml
└── README.md
```

---

Built as part of a Python web scraping curriculum.