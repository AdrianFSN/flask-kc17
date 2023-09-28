from flask import render_template

from . import app
from .models import Carta


@app.route("/")
def home():
    carta = Carta('oros', 2)
    carta1 = Carta('copas', 5)
    return render_template('base.html', carta=carta, otra_carta=carta1)
