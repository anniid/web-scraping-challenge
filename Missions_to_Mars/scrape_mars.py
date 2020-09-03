#dependencies
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as soup 
import datetime as dt

#begin scrape
def scrape_all():

    #executable path & browser
    browser = Browser("chrome", executable_path="/Users/annel/Downloads/chromedriver/chromedriver.exe", headless=True)
    news_title, news_paragraph = mars_news(browser)
    mars_facts=facts_table()
    #run all scraping funcs and store results in dict.
    data={
        "news_title":news_title,
        "news_paragraph":news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "hemispheres":hemispheres(browser),
        "last_modified":dt.datetime.now()
    }
    #stop webdriver and return data
    browser.quit()
    return data

def mars_news(browser):
    #scrape mars news from https://mars.nasa.gov/news/
    news_url='https://mars.nasa.gov/news/'
    #visit the site
    browser.visit(news_url)
    #convert html to soup, then quit browser
    html=browser.html
    news=soup(html,'html.parser')
    #handle errors (try, except)
    try:
        slide_elem=news.select_one('li.slide')
        title=slide_elem.find("div", class_="content_title").get_text()
        teaser=soup(browser.html,'html.parser').select_one('li.slide').find("div", class_='article_teaser_body').get_text()
    except AttributeError:
        return None, None
    return title, teaser

def featured_image(browser):
    #visit url
    featured_image_url='https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(featured_image_url)
    #"find" and "click" full image button
    full_bttn=browser.find_by_id('full_image')
    full_bttn.click()
    #"find" and "click" more info button
    info_bttn=browser.links.find_by_partial_text('more info')
    info_bttn.click()
    #parse results with soup, error handling
    try:
        img_url=soup(browser.html,'html.parser').select_one('figure.lede a img').get("src")
    
    except AttributeError:
        return None

    #create final url
    final_url=f'https://www.jpl.nasa.gov{img_url}'

    return final_url

def facts_table():
    #error handling (try, except)
    #try to transform it from html to a pandas df
    try:
        facts_df = pd.read_html('http://space-facts.com/mars/')[0]
    except BaseException:
        return None
    #assign columns, set index
    facts_df.columns=['Description', 'Mars']
    facts_df.set_index('Description', inplace=True)
    #then turn df back into html, adding bootstrap
    return facts_df.to_html

def hemispheres(browser):
    #get the base url
    #visit the base url
    hemi_url='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemi_url)
    #use a for loop to collect a list of image urls
    hemisphere_img_urls=[]

    for i in range(4):
        browser.find_by_css("a.itemLink h3")[i].click()
        hemi=scrape_hemi(browser.html)
        hemisphere_img_urls.append(hemi)
#at end of loop navigate back to beginning
        browser.back()

    return hemisphere_img_urls 


def scrape_hemi(html_text):
    #parse html text with soup
    browser = Browser("chrome", executable_path="/Users/annel/Downloads/chromedriver/chromedriver.exe", headless=True)
    
    #error handling (try, except)
    try:
        anchor = browser.links.find_by_text('Sample').first
        hemi_img_url = anchor['href']
        hemi_title = browser.find_by_css("h2.title").text
        
    except AttributeError:
        hemi_title= None
        hemi_img_url= None
    #dictionary of results [title, url]
    hemisphere={
        "title":hemi_title,
        "img_url":hemi_img_url
    }

    return hemisphere

if __name__ == "__main__":
    print(scrape_all())