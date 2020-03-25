#homework: add css to index file
import flask
from game import *
from question import *
import mysql.connector

app = flask.Flask(__name__)

db = mysql.connector.connect(
  host="104.168.136.69",
  user="yscbtlcv_teacher",
  passwd="TopCoder15",
  database="yscbtlcv_instructor"
)

cursor = db.cursor()



@app.route("/", methods = ["GET", "POST"])
def home():
    return flask.render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0")