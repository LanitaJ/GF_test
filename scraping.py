import re
import connector

#Get html code all page of site
SOUP = connector.soup_connection('https://kwork.ru/projects')

#Scraping all names from page
def scrap_name():
    names = []
    #Get all elements by tag and class
    for name_code in SOUP.find_all('div', class_='wants-card__header-title first-letter breakwords pr250'):
        name = name_code.find('a')
        #Appending name to array of names
        names.append(name.text)
    return names


#Scraping all desiring prices
def scrap_first_price():
    prices = []
    #Get all elements by tag and class
    for price_code in SOUP.find_all('div', class_='wants-card__header-price wants-card__price m-hidden'):
        price = price_code.find('span')
        #Appending desiring price to array
        prices.append(price.text)
    return prices

#Scraping all allowable prices
def scrap_second_price():
    prices = []
    #Get all elements by tag and class
    for price_code in SOUP.find_all('div', class_='wants-card__description-higher-price'):
        price = price_code('span')
        #Appending allowable price to array
        prices.append(price.text)
    return prices

#Scraping all details
def scrap_details():
    details = []
    #Get all elements by tag and class
    for detail_code in SOUP.find_all('div', class_='breakwords first-letter js-want-block-toggle js-want-block-toggle-full hidden'):
        details.append(detail_code.text)
    return details

#Scraping all times and sugestions
def scrap_time_sugges():
    times_sugges = []
    times = []
    sugges = []
    #Get all times and sugestions by tag and class
    for time_sugges_code in SOUP.find_all('div', 'force-font force-font--s12'):
        #In this div searching span with text
        for time_sugges in time_sugges_code.find_all('span'):
            #Append text from span to array
            times_sugges.append(time_sugges)
        #Appending times to array
        times.append(times_sugges[0])
        #Appending suggestions to arrray
        sugges.append(times_sugges[1])
    data = {times : sugges}
    return data
