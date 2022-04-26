import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html')

@app.route('/get-wod/')
def get_wod():

    # getting the website access
    url = 'https://www.merriam-webster.com/word-of-the-day'
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')

    # getting the title
    wod = soup.find(
        'span', attrs={'class': 'w-a-title margin-lr-0 margin-tb-1875em'}).text.strip()

    # getting the word
    div = soup.find('div', attrs={'class': 'word-and-pronunciation'})
    word = div.find('h1').text

    # getting the definition
    div_1 = soup.find('div', attrs={'class': 'wod-definition-container'})
    definition = div_1.find('p').text

    # in a sentence
    sentence = (div_1.find_all('p')[1].text.split('// '))[1]

    print('wod')
    print('word')
    print('definition')
    print('sentence')

    #return '''<h1>{}<br>{}<br>{}<br>{}</h1>'''.format(wod, word, definition, sentence)

    return render_template('wod_page.html', a = wod, b = word, c = definition, d = sentence)

    #return wod, word, definition, sentence
if __name__ == '__main__':
    app.run(debug=True)