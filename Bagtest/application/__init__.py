from flask import Flask
app = Flask(__name__)
#app.config.from_object(__name__)
#app.config.update(SECRET_KEY='development key')

import application.views