from flask import jsonify
from flask import request

from ML_module import get_rez, get_top
from conf import db, app

db.create_all()
print('started')


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/get_prob/url', methods=['GET', 'POST'])
def get_prob_url():
    url = request.args.get('url')
    rez = get_rez(url)
    if rez is not None:
        return jsonify(rez
                       ), 200
    else:
        return jsonify(None), 500


@app.route('/get_prob/url/<url>')
def get_prob_url1(url):
    rez = get_rez(url)
    if rez is not None:
        return jsonify(rez
                       ), 200
    else:
        return jsonify(None), 500


@app.route('/get_prob/top', methods=['GET', 'POST'])
def top():
    page = request.args.get('page')
    data = get_top(page)
    sites=data[0]
    counter=data[1]
    rez = list()
    for site in sites:
        rez.append({
            "site_stat": site.prob,
            "head_url": site.url,
            "icon": site.icon
        }
        )
    print(rez[0])
    rez={'total_pages':counter,
    'sites':rez
    }
    if rez is not None:
        return jsonify(rez
                       ), 200
    else:
        return jsonify(None), 500


@app.route('/get_prob/top/<page>')
def top1(page):
    data = get_top(page)
    sites=data[0]
    counter=data[1]
    rez = list()
    for site in sites:
        rez.append({
            "site_stat": site.prob,
            "head_url": site.url,
            "icon": site.icon
        }
        )
    print(rez[0])
    rez={'total_pages':counter,
    'sites':rez
    }
    if rez is not None:
        return jsonify(rez
                       ), 200
    else:
        return jsonify(None), 500


'''@app.route('/get_prob/text', methods=['GET', 'POST'])
def get_prob_text():
    return jsonify(
        {
            "text": request.args.get('text'),
            "prob": random.random()
        }
    ), 200


@app.route('/get_prob/text/<text>')
def get_prob_text1(text):
    return jsonify(
        {
            "text": text,
            "prob": random.random()
        }
    ), 200'''

if __name__ == "__main__":
    app.run(port='8080', host='0.0.0.0')
