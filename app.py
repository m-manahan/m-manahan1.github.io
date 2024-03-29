from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

#Create an instance of flask
app = Flask(__name__)

# Create connection variable
conn = 'mongodb://localhost:27017'
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_data_app"
mongo = PyMongo(app)

# Set route
@app.route("/")
def index():
    mars_data = mongo.db.mars_data.find_one()
    return render_template("base_index.html", mars_data=mars_data)

@app.route("/scrape")
def scraper():
    mars_data = mongo.db.mars_data
    scraped_data = scrape_mars.scrape()
    mars_data.update({}, scraped_data, upsert=True)
    return redirect("/", code=302)

@app.route("/marswebscrape")
def marswebscrape():
    mars_data = mongo.db.mars_data.find_one()
    return render_template("index.html", mars_data=mars_data)

@app.route("/UFOtablesearch")
def UFOtablesearch():
    return render_template("UFOindex.html")



if __name__ == "__main__":
    app.run(debug=True)


