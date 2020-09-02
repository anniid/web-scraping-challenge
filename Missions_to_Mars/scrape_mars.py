#dependencies
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as soup 
import datetime as dt

#begin scrape
def scrape():

    #executable path 
    executable_path={'executable_path': '/Users/annel/Downloads/chromedriver/chromedriver.exe'}
    #browser
    browser= Browser('chrome', **executable_path)
    #run all scraping funcs and store results in dict.

#stop webdriver and return data

def mars_news(browser):
    #scrape mars news from https://mars.nasa.gov/news/
    #visit the site

    #convert html to soup, then quit browser

    #handle errors (try, except)

def featured_image(browser):
    #visit url

    #"find" and "click" full image button

    #"find" and "click" more info button

    #parse results with soup

    #error handling (try, except)

    #create final url

def facts_table():
    #error handling (try, except)
    #try to transform it from html to a pandas df

    #assign columns, set index

    #then turn df back into html, adding bootstrap

def hemispheres(browser):
    #get the base url
    #visit the base url

    #use a for loop to collect a list of image urls

def scrape_hemi(html_text):
    #parse html text with soup

    #error handling (try, except)

    #dictionary of results [title, url]

if __name__ == "__main__"

    print(scrape())