from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://bqskcbol:DtyP-Si3aZ8i45u_rRPR3XohaaKSY8Wg@balarama.db.elephantsql.com:5432/bqskcbol'
db = SQLAlchemy(app)
print(db)
