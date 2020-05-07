from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://vwzhnpjq:KwgCuOZ4S_f4VMqxiXSuUn8tgwL6OQtW@dumbo.db.elephantsql.com:5432/vwzhnpjq'
db = SQLAlchemy(app)
print(db)