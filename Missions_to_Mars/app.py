#dependencies
from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scrape_mars

#create app
app=Flask(__name__)

#mongo connection via flask_pymongo
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)
#routes / and /scrape
@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)

@app.route("/scrape")
def scrape():
    mars=mongo.db.mars
    mars_data=scrape_mars.scrape_all()
    mars.update({},mars_data,upsert=True)
    return "Scrape Complete"

if __name__ == "__main__":
    app.run()