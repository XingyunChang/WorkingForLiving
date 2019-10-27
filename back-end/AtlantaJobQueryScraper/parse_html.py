from bs4 import BeautifulSoup


link_prefix = "http://www.indeed.com"


def parse(content):
    soup = BeautifulSoup(content, features="lxml")
    divs = soup.findAll("div", attrs={"class": "jobsearch-SerpJobCard unifiedRow row result"})

    items = []

    for div in divs:

        subsoup = BeautifulSoup(str(div), features="lxml")

        title = subsoup.findAll("a", attrs={"class": "jobtitle turnstileLink"})[0].text.strip()

        employer = subsoup.findAll("span", attrs={"class": "company"})[0].text.strip()

        location = subsoup.findAll("span", attrs={"class": "location accessible-contrast-color-location"})
        if len(location) == 0:
            location = subsoup.findAll("div", attrs={"class": "location accessible-contrast-color-location"})
        location = location[0].text.strip()

        salary = subsoup.findAll("span", attrs={"class": "salaryText"})
        if (len(salary) != 0):
            salary = salary[0].text.strip()
        else:
            salary = None

        link = link_prefix + subsoup.findAll("a", attrs={"target": "_blank"})[0]["href"]

        item = {"title": title, "employer": employer, "location": location, "salary": salary, "link": link}

        items.append(item)

    return items
