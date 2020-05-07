from conf  import db,app


class AnswerData(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  icon = db.Column(db.Text)
  prob = db.Column(db.Float)
  url = db.Column(db.Text)
  site_name = db.Column(db.Text)


