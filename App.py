from flask import Flask , render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# db config
app.secret_key = "Secrete Key"

app.config['SQLALCHEMY_DATABASE_URL'] = 'mysql://root:''@localhost/crude'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# creating a database tables
class Data(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.string(100))
    email = db.Column(db.string(100))
    phone = db.Column(db.string(100))

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
