import pickle
import os
from conf import db,app
from utils import get_data_by_url
import sklearn
from models import AnswerData
from sqlalchemy.sql import func
from urllib.parse import urlparse

basepath = os.path.abspath(".")

with open('model.model', 'rb') as f:
     model = pickle.load(f)

with open('model.vec', 'rb') as f:
     vectorizer = pickle.load(f)
print(model)
print(vectorizer)

def get_vec(text):
    return vectorizer.transform([text])

def predict(vec):
    return model.predict_proba(vec)


def get_head_url(url):
  return urlparse(url).netloc

def get_rez(url):
  rez={}
  data=get_data_by_url(url)
  text=data['text']
  rez['title']=data['title']
  rez['icon']=data['icon']
  rez['url']=url
  rez['prob']=predict(get_vec(text))[0][0]
  rez['head_url']=get_head_url(url)
  resp=AnswerData(
    icon=rez['icon'],
   prob=rez['prob'],
   url=rez['url'],
   site_name=rez['head_url'],
   )
  exists = db.session.query(AnswerData.url).filter_by(url=rez['url']).scalar() is not None 
  if not exists:
    db.session.add(resp)
    db.session.commit()
  
  avg=db.session.query(func.avg(AnswerData.prob).label('average')).filter(AnswerData.site_name==rez['head_url']).first()[0]
  print(str(avg))
  rez['site_stat']=float(str(avg))



  print(rez)
  return rez
