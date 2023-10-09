from csv import writer
from parse import parsePage, Event
from functions import getSoup
from typing import List

baseUrl = "https://developers.google.com"
url = (
    "https://developers.google.com/admin-sdk/reports/v1/appendix/activity/user-accounts"
)


soup = getSoup(url)
if soup:
    with open(
        "gws_activities.csv", "w", newline=""
    ) as write_obj:
        csv_writer = writer(write_obj, delimiter=",")
        csv_writer.writerow(["Activity Type", "event_name", "event_type", "Name", "Description"])
        # Find the <ul> element with class 'devsite-nav-section'
        nav_section = soup.find("ul", class_="devsite-nav-section")

        if nav_section:
            # Find all <a> elements within the <ul> element
            links = nav_section.find_all("a")

            # Iterate through the links and print their text and href attributes
            for link in links:
                text = str(link.text.strip())
                href = str(link.get("href"))
                if "appendix/activity/" in href and "appendix/activity/admin-" not in href and "appendix/activity/access-transparency" not in href:
                    events = parsePage(getSoup(f"{baseUrl}{href}"))
                    for event in events:
                        csv_writer.writerow([event.activityType, event.eventName, event.eventType, event.name, event.description])
        else:
            print("Navigation section not found on the page.")
else:
    print("Failed to parse the HTML content.")
