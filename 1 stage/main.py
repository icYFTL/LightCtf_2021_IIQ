from flask import Flask, render_template, make_response
from base64 import encodebytes

app = Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET'])
def on_root():
    response = make_response(render_template('index.html'))
    response.headers.set('hidden', 'L3JseV9zZWNyZXRfcGF0aA==')
    return response, 200


@app.route('/rly_secret_path', methods=['GET'])
def on_secret():
    return render_template('cat.html', cat=encodebytes(open('StegoCat.jpg', 'rb').read()).decode('UTF-8'))


app.run('0.0.0.0', 8000, False)
