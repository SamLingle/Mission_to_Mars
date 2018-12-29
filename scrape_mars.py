# Import dependencies
from bs4 import BeautifulSoup
from spinter import Browser
import pandas as pd
import requests

# Create a function called scrape to execute scraping code and return one dictionary containing all scraped data.
def scrape():
  mars_results = {}
# Mars News Scrape.
  executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
  browser = Browser('chrome', **executable_path, headless=False)
  news_url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')
  
  # Documentation: https://splinter.readthedocs.io/en/latest/api/driver-and-element-api.html
  # wait for the webage to load, returns true if tag is present and false if not. 
  while not browser.is_element_present_by_tag("div", wait_time=3):
    pass
  # Scrape the needed data.
  html = browser.html
  soup = BeautifulSoup(html, 'html.parser')

  news_title = soup.find("div",class_="content_title").text
  news_p = soup.find('div', class_="rollover_description_inner").text
  
  # Add results to mars_results.
  mars_results["news_title"] = news_title
  mars_results["news_p"] = news_p

# Featured image url scraping

  jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars/'
  browser.visit(jpl_url)

  html = browser.html
  soup = BeautifulSoup(html, 'html.parser')

  featured_img_base = "https://www.jpl.nasa.gov"
  featured_img_url_raw = soup.find("div", class_="carousel_items").find("article")["style"]
  featured_img_url = featured_img_url_raw.split("'")[1]
  featured_img_url = featured_img_base + featured_img_url
  
  # Add results to mars_results.
  mars_results["featured_img_url"] = featured_img_url

# Mars weather tweet scraping

  twitter_url = "https://twitter.com/marswxreport?lang=en"
  browser.visit(twitter_url)

  html = browser.html
  soup = BeautifulSoup(html, 'html.parser')
  
  
  mars_weather = soup.find("div",class_="js-tweet-text-container").text

  mars_results["mars_weather"] = mars_weather

  # Mars facts scraping

  facts_url = "https://space-facts.com/mars/"
  tables = pd.read_html(facts_url)

  facts_df = tables[0]
  facts_df.columns = ["Fact","Value"]
  facts_df = facts_df.set_index("Fact")
  facts_df

  facts_html_table = facts_df.to_html()
  facts_html_table = facts_html_table.replace('\n', '')
    
  mars_results["facts_html_table"] = facts_html_table

  # Mars hemispheres photo scraping

  #Service is unavailable at the current time. 

return mars_results
