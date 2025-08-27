# WerkScout

**WerkScout** is a Python library designed to help you slice large search requests into manageable, polite chunks and extract relevant data (e.g., emails) from web pages.

##  Features
- **Simple search query slicing**: allows segmentation by domain, keyword patterns, and more.
- **Email scraping with Selenium**: robust routines using `ScrapeScript.py`.
- **Domain lookup helpers**: utility functions in `searchEngines.py`.
- **SQLite support**: integrated `DbContext.py` for storing and retrieving data.
- **API abstraction**: central API handling in `Api.py`.
- **Respectful web scraping**: rate limiting and retry logic built in—designed to avoid getting blocked.

---

##  Installation

WerkScout is still under development. To install locally for development:

```bash
git clone https://github.com/MahmoudYazid/WerkScout.git
cd WerkScout
python -m venv .venv
source .venv/bin/activate             # On Windows: .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install -e .
```

---

##  Usage Example

```python
from ScrapeScript import start_EmailsList_Scrape_From_Domain
from searchEngines import FindDomain_autocompleteclearbit

# Fetch a domain via search engine
domain = FindDomain_autocompleteclearbit("example query")

# Scrape emails from that domain
emails = start_EmailsList_Scrape_From_Domain(domain)

print(f"Found {len(emails)} emails:")
for e in emails:
    print(" –", e)
```

---

##  Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repo and create a feature branch for your changes.
2. Submit a pull request with a clear description and tests where applicable.
3. Note: You may **not** publish this library under a different name or claim ownership—see **CONTRIBUTING.md** and **LICENSE** for details.

---

##  License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.

---

##  Contact & Learn More

Created by **Mahmoud Yazid**. For questions or issues, open an issue on GitHub or reach out via LinkedIn https://www.linkedin.com/in/mahmoud-yazid/ .
