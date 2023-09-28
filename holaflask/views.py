from flask import render_template

from . import app
from .models import Carta


@app.route("/")
def home():
    carta = Carta('espadas', 7)
    carta1 = Carta('bastos', 3)
    return render_template('base.html', carta=carta, otra_carta=carta1)
