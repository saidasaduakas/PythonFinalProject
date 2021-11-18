from datetime import datetime, timedelta
from flask import Flask, render_template,request
from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy
from flask.helpers import make_response
from flask.json import jsonify
import jwt
import bcrypt
import db
app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisismyflasksecretkey'

@app.route("/")
def home():
    return '''<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
        
            <nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Navbar</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Link</a>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Dropdown
          </a>
          <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
            <li><a class="dropdown-item" href="#">Action</a></li>
            <li><a class="dropdown-item" href="#">Another action</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="#">Something else here</a></li>
          </ul>
        </li>
        <li class="nav-item">
          <a class="nav-link disabled">Disabled</a>
        </li>
      </ul>
      <form class="d-flex">
        <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
        <button class="btn btn-outline-success" type="submit">Search</button>
      </form>
    </div>
  </div>
</nav>
<div class="input-group">
  <span class="input-group-text"> Hello to everyone</span>
  <input type="text" class="form-control" placeholder="Today I am going to demonstrate my project for coin" aria-label="Username" aria-describedby="addon-wrapping">

'''
@app.route('/login')
def login():

    auth = request.authorization

    if auth and auth.password == 'password':
        token = jwt.encode({'user':auth.username, 'exp':datetime.utcnow() + timedelta(minutes=30)}, app.config['SECRET_KEY'])
    
        return jsonify({'token': token.decode('UTF-8')})
       
        
    
    return make_response('token value', 1, {'WWW-Authenticate': 'Basic realm="Login required'})

@app.route('/protected')

def protection():
   
    token = request.args.get(False)
    return '''<h1>Hello, Could not verify the token  <h1>'''.format(token)
def protection():
   
    token = request.args.get(True)
    return '''<h1> Hello, token which is provided is correct <h1>'''.format(token)
@app.route('/coin', methods=['GET', 'POST'])
def form_example():
    # handle the POST request
    if request.method == 'POST':
        language = request.form.get('language')
        if(language == 'coin'):
            return'''
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
        
            <nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Navbar</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Link</a>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Dropdown
          </a>
          <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
            <li><a class="dropdown-item" href="#">Action</a></li>
            <li><a class="dropdown-item" href="#">Another action</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="#">Something else here</a></li>
          </ul>
        </li>
        <li class="nav-item">
          <a class="nav-link disabled">Disabled</a>
        </li>
      </ul>
      <form class="d-flex">
        <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
        <button class="btn btn-outline-success" type="submit">Search</button>
      </form>
    </div>
  </div>
</nav>
<form method="POST">

<div class="input-group flex-nowrap">
  <span class="input-group-text" id="addon-wrapping">COIN NAME</span>
  <input type="text" class="form-control" placeholder="Username" aria-label="Username" aria-describedby="addon-wrapping" name="language">
</div>
<div class="col-12">
    <button type="submit" class="btn btn-primary">Sign in</button>
  </div>

  <span id="passwordHelpInline" class="form-text">
  You must fill in to proceed further
  </span>
  <br><br><br>
            <p>The live Bitcoin price today is $57,671.08 USD with a 24-hour 
            trading volume of $41,019,487,990 USD. We update our BTC to USD price in 
            real-time. Bitcoin is down 4.40% in the last 24 hours. The current CoinMarketCap ranking is 
            #1, with a live market cap of $1,088,653,269,624 USD. It has a circulating supply of 18,876,937 BTC coins and a max. 
            # supply of 21,000,000 BTC coins.</p>
            <p>Bitcoin is a decentralized cryptocurrency originally described in a 2008 whitepaper by a person, or group of people, using the alias Satoshi Nakamoto. It was launched soon after, in January 2009.<br>

Bitcoin is a peer-to-peer online currency, meaning that all transactions happen directly between equal, independent network participants, without the need for any intermediary to permit or facilitate them. Bitcoin was created, according to Nakamoto’s own words, to allow “online payments to be sent directly from one party to another without going through a financial institution.”
<br>
Some concepts for a similar type of a decentralized electronic currency precede BTC, but Bitcoin holds the distinction of being the first-ever cryptocurrency to come into actual use.

</p>
<p>Bitcoin’s original inventor is known under a pseudonym, Satoshi Nakamoto. As of 2021, the true identity of the person — or organization — that is behind the alias remains unknown.
<br>
On October 31, 2008, Nakamoto published Bitcoin’s whitepaper, which described in detail how a peer-to-peer, online currency could be implemented. They proposed to use a decentralized ledger of transactions packaged in batches (called “blocks”) and secured by cryptographic algorithms — the whole system would later be dubbed “blockchain.”
<br>
Just two months later, on January 3, 2009, Nakamoto mined the first block on the Bitcoin network, known as the genesis block, thus launching the world’s first cryptocurrency. Bitcoin price was $0 when first introduced, and most Bitcoins were obtained via mining, which only required moderately powerful devices (e.g. PCs) and mining software. The first known Bitcoin commercial transaction occurred on May 22, 2010, when programmer Laszlo Hanyecz traded 10,000 Bitcoins for two pizzas. At Bitcoin price today in mid-September 2021, those pizzas would be worth an astonishing $478 million. This event is now known as “Bitcoin Pizza Day.” In July 2010, Bitcoin first started trading, with the Bitcoin price ranging from $0.0008 to $0.08 at that time.
<br>
However, while Nakamoto was the original inventor of Bitcoin, as well as the author of its very first implementation, he handed the network alert key and control of the code repository to Gavin Andresen, who later became lead developer at the Bitcoin Foundation. Over the years a large number of people have contributed to improving the cryptocurrency’s software by patching vulnerabilities and adding new features.
<br>
Bitcoin’s source code repository on GitHub lists more than 750 contributors, with some of the key ones being Wladimir J. van der Laan, Marco Falke, Pieter Wuille, Gavin Andresen, Jonas Schnelli and others.<p>'''


    # otherwise handle the GET request
    return '''
           
           
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
        <br><br>    
<form method="POST">

<div class="input-group flex-nowrap">
  <span class="input-group-text" id="addon-wrapping">COIN NAME</span>
  <input type="text" class="form-control" placeholder="Username" aria-label="Username" aria-describedby="addon-wrapping" name="language">
</div>
<div class="col-12">
    <button type="submit" class="btn btn-primary">Sign in</button>
  </div>

  <span id="passwordHelpInline" class="form-text">
  You must fill in to proceed further
  </span>
  
  </form>
            '''
    
    

if __name__ == '__main__':
    app.run(debug=True)

    
