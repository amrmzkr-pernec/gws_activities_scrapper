from bs4 import BeautifulSoup
from typing import List

class Event:
    eventName: str
    eventType: str | None
    name: str
    description: str | None
    activityType: str
    def __init__(self, eventName: str, eventType: str | None, name: str, description: str | None, activityType: str):
        self.eventName = eventName
        self.eventType = eventType
        self.name = name
        self.description = description
        self.activityType = activityType
        
        

def parsePage(soup: BeautifulSoup) -> List[Event]:
    events: List[Event] = []
    # Find the "devsite-article-body" div
    article_body = soup.find('div', class_='devsite-article-body')

    # Find all section blocks within the "devsite-article-body" div
    section_blocks = article_body.find_all('section')
    
    activityType = soup.find('h1').get_text(strip=True)

    # Iterate through each section block
    for section in section_blocks:
        eventType = None
        # find h2, then paragraph, then event_type
        h2_sibling = section.find_previous_sibling('h2')
        p_sibling = h2_sibling.find_next_sibling('p')
        if p_sibling:
            eventType = p_sibling.find('code').get_text(strip=True).split("=")[1]
        # Find the h3 element for name
        name = section.find('h3').get_text(strip=True)
        # Find the first <p> for description
        try:
            description = section.find('p').get_text(strip=True)
        except Exception as e:
            description = None
        # Find the event name from the first row of the table
        eventName = section.find('table').find('tbody').find_all('tr')[0].find_all('td')[1].get_text(strip=True)
        events.append(Event(eventName, eventType, name, description, activityType))

    # Print the descriptions and event names
    for event in events:
        print("Activity Type:", event.activityType)
        print("Name:", event.name)
        print("Description:", event.description)
        print("Event Name:", event.eventName)
        print("Event Type:", event.eventType)
        print("-------------")
    return events
