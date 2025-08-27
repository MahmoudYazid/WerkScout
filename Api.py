"""
Extracts email addresses associated with a given company name.
This function attempts to find the domain for the specified company using two methods:
1. `FindDomain_autocompleteclearbit`
2. `FindDomain_Google` (if the first method fails)
Once the domain is found, it scrapes email addresses from that domain.
Args:
  companyName (str): The name of the company to extract emails for.
Returns:
  str: Returns "done" after the extraction process is completed.
"""

import json
from ScrapeScript import   extract_emails_with_selenium_js, start_EmailsList_Scrape_From_Domain
from searchEngines import FindDomain_autocompleteclearbit , FindDomain_ducksearch 


# deep reearch
def DeepResearchEmail(companyNameOrUrl):

    try:
        x= FindDomain_ducksearch(companyNameOrUrl)
              
    except Exception as e:
        print("Error finding domain:", e)
        return "failed to find domain"
    
    return start_EmailsList_Scrape_From_Domain(x)


#more deeper when there is need to be deep
def ExtractEmailsByCompanyName(companyName):

    try:
        x= FindDomain_autocompleteclearbit(companyName)
        if len(x) == 0 :
            print("Trying with DuckDuckGo")
            x= FindDomain_ducksearch(companyName)
    except Exception as e:
        x= FindDomain_ducksearch(companyName)

        print("Error finding domain:", e)
        return "failed to find domain"
    
    return start_EmailsList_Scrape_From_Domain(x)

# not deep research becauuse it target specific url
def SearchByUrl(url):
    emails, _= extract_emails_with_selenium_js(url)
    filtered_emails = []
    for email in emails:
        if email.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.svg', '.webp')):
            continue
        else:
            filtered_emails.append(email)
    return filtered_emails


# here we can add more search engines if needed in the future
# for now we have 2 search engines implemented
# this is the main functions and the main page of Url ################################################# important
if __name__ == "__main__":
    companyName = "OpenAI"  # Example company name
    result = ExtractEmailsByCompanyName(companyName)
    print(f"Extracted emails for {companyName}: {result}")

