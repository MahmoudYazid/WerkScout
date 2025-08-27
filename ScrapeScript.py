import sqlite3
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import subprocess  

def extract_emails_with_selenium_js(start_url, timeout=20, crawl_wait=10):
    def make_driver():
        opts = Options()
        opts.add_argument("--headless=new")
        opts.add_argument("--disable-gpu")
        opts.add_argument("--no-sandbox")
        opts.add_argument("--disable-dev-shm-usage")
        opts.add_argument("--window-size=1920,1080")
        opts.add_argument("--log-level=3")
        opts.add_experimental_option("excludeSwitches", ["enable-logging"])
        service = Service(ChromeDriverManager().install(), log_output=subprocess.DEVNULL)
        return webdriver.Chrome(service=service, options=opts)

    driver = make_driver()
    driver.set_page_load_timeout(timeout)

    try:
        driver.get(start_url)

        # optional cookie auto-click
        driver.execute_script("""
        for (const sel of [
          '#onetrust-accept-btn-handler',
          'button#onetrust-accept-btn-handler',
          'button[aria-label="Accept all"]',
          '.cm-btn--accept', '.cky-btn-accept', '.hs-accept-all'
        ]) {
          try {
            const el = document.querySelector(sel);
            if (el) el.click();
          } catch (e) {}
        }
        """)

        driver.set_script_timeout(timeout + crawl_wait)

        result = driver.execute_async_script(f"""
        const done = arguments[arguments.length - 1];

        (async () => {{
          const visited = new Set();
          const emails = new Set();
          const base = location.origin;
          const emailRegex = /[A-Z0-9._%+-]+@[A-Z0-9.-]+\\.[A-Z]{{2,}}/gi;

          const extractEmails = (text) => {{
            (text.match(emailRegex) || []).forEach(e => emails.add(e));
          }};

          const scrape = async (url) => {{
            if (visited.has(url)) return;
            visited.add(url);
            try {{
              const res = await fetch(url);
              if (!res.ok) return;
              const txt = await res.text();
              extractEmails(txt);

              const doc = new DOMParser().parseFromString(txt, "text/html");
              doc.querySelectorAll("a[href]").forEach(a => {{
                const href = a.getAttribute("href");
                if (!href) return;
                if (href.startsWith("/") || href.startsWith(base)) {{
                  const abs = href.startsWith("/") ? base + href : href;
                  if (abs.startsWith(base)) scrape(abs);
                }}
              }});
            }} catch (e) {{
              console.warn("fail", url, e);
            }}
          }};

          await scrape(location.href);

          setTimeout(() => {{
            done({{
              emails: Array.from(emails),
              visitedPages: visited.size
            }});
          }}, {crawl_wait * 1000});
        }})();
        """)
    
    
    except Exception as e:
      driver.quit()
      return set(), 0  
    finally:
        driver.quit()

    return set(result["emails"]), result["visitedPages"]




"""
Scrapes email addresses from a list of domain URLs and saves them to a SQLite database.
For each domain in FinalDomains, this function:
- Prints the domain being scraped.
- Extracts email addresses using the extract_emails_with_selenium_js function.
- Inserts each unique email address and its associated domain into the 'emailsTable' table in 'emails.db'.
Args:
  FinalDomains (list): A list of domain URLs to scrape for email addresses.
Returns:
  str: A confirmation message indicating that the emails have been saved.
"""

def start_EmailsList_Scrape_From_Domain(FinalDomains):

    JsonResponse = []
    for url in FinalDomains:
      emails, _= extract_emails_with_selenium_js(url)
      for email in emails:
        if email.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.svg', '.webp')):
            continue
        con = sqlite3.connect('./emails.db', isolation_level=None)  # autocommit
        cur = con.cursor()
        cur.execute("INSERT OR IGNORE INTO emailsTable (email, domain) VALUES (?, ?)", (email, url))
        JsonResponse.append({"email": email, "domain": url}) 
    return JsonResponse



