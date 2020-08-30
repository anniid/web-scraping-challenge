#dependencies
from flask import Flask, render_template, redirect, url_for
from flask_pymongo import pymongo
import scrape_tool

#create app
app=Flask(__name__)
#mongo connection via flask_pymongo

#routes / and /scrape


if __name__ == "__main__":
    app.run()