from flask import Flask, render_template, request
#comment2

from flask_wtf import FlaskForm
from wtforms import SelectField, IntegerField, widgets, SubmitField


# imports for uploading files:
from wtforms import FileField
from flask_wtf.file import FileRequired
from werkzeug.utils import secure_filename
import os



app = Flask(__name__)
# Musíme nastavit SECRET_KEY, pokud chceme používat CSRF
app.config["SECRET_KEY"] = "super tajny klic"

class MujFormular(FlaskForm):
    prvni_cislo = IntegerField("První Číslo", widget = widgets.Input(input_type = "number"))
    operator = SelectField("Operátor", choices=[("+" ,"+"), ("-", "-"), ("*", "*"), ("/", "/")])
    druhe_cislo = IntegerField("Druhé Číslo", widget = widgets.Input(input_type = "number"))
    submit = SubmitField("Odeslat", render_kw = dict(class_ = "btn btn-outline-primary btn-block"))
    # render_kw pomocí kterého můžeme přidat vygenerovanému kódů například třídu, hodnotu a 
    # další atributy

@app.route("/", methods = ["GET", "POST"])
def kalkulacka():
    form=MujFormular()
    if form.validate_on_submit(): #will check if it is a POST request and if it is valid.
        prvni_cislo = form.prvni_cislo.data
        druhe_cislo = form.druhe_cislo.data
        operator = form.operator.data
        vysledek = eval( str(prvni_cislo) + operator + str(druhe_cislo) )
        return render_template("kalkulacka.html", vysledek = vysledek, form = form)
    return render_template("kalkulacka.html", form = form) #Vrátíme naší šablonu s výsledkem


# cast pro nahravani filu:
#Nastavíme složku, kam se budou obrázky ukládat
UPLOAD_FOLDER = app.static_folder + "/uploads/" #budou se ukldat do root/static/uploads
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

class FileFormular(FlaskForm):
    soubor = FileField("Vlož obrázek", validators = [FileRequired()]) #FileRequired() - validace zda byl soubor nahran
    submit = SubmitField("Odeslat", render_kw = dict(class_ = "btn btn-outline-primary btn-block"))

@app.route("/galerie/", methods = ["GET", "POST"])
def galerie():
    form = FileFormular()
    if form.validate_on_submit():
        soubor = form.soubor.data
        nazev = secure_filename(soubor.filename) #zkontrolujeme pomocí nástroje
            # z knihovny werkzeug, na které mimochodem běží Flask, zda je název souboru bezpečný, 
        soubor.save(os.path.join(app.config['UPLOAD_FOLDER'], nazev))
        obrazky = os.listdir(app.static_folder + "/uploads")
    return render_template("galerie.html", form = form, obrazky=obrazky)



if __name__ == "__main__":
    app.run(debug=True)
