import os
import pickle
from urllib.parse import urlparse

from flask import jsonify

from conf import db
from models import Site, Page
from utils import get_data_by_url

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
    rez = {}
    data = get_data_by_url(url)
    if data is None:
        return None

    rez['head_url'] = get_head_url(url)
    rez['icon'] = data['icon']
    exists_site = db.session.query(Site.url).filter_by(url=rez['head_url']).scalar() is not None
    if not exists_site:
        site = Site(prob=0, num=0, url=rez['head_url'], icon=rez['icon'])
        db.session.add(site)
        db.session.commit()
    else:
        site = db.session.query(Site).filter_by(url=rez['head_url']).first()
    text = data['text']
    rez['prob'] = predict(get_vec(text))[0][0]
    rez['url'] = url
    rez['title'] = data['title']
    page = Page(prob=rez['prob'], uri=rez['url'], site_id=site.id, title=rez['title'])
    exists_page = db.session.query(Page.uri).filter_by(uri=rez['url']).scalar() is not None
    if not exists_page:
        db.session.add(page)
        db.session.commit()
        db.session.query(Site) \
            .filter_by(url=rez['head_url']) \
            .update({Site.prob: (Site.prob * Site.num + rez['prob']) / (Site.num + 1),
                     Site.num: Site.num + 1})
        db.session.commit()

    rez['site_stat'] = db.session.query(Site).filter_by(url=rez['head_url']).first().prob

    return rez


def get_top(page=1,per_page=10):
    sites=db.session.query(Site).order_by(Site.prob.desc()).paginate(int(page), int(per_page), True).items
    count=len(db.session.query(Site).all())
    return sites,count

