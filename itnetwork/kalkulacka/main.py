from flask import Flask, render_template, request

from flask_wtf import FlaskForm
from wtforms import SelectField, IntegerField, widgets

app = Flask(__name__)
# Musíme nastavit SECRET_KEY, pokud chceme používat CSRF
app.config["SECRET_KEY"] = "super tajny klic"

class MujFormular(FlaskForm):
    prvni_cislo = IntegerField("První Číslo", widget = widgets.Input(input_type = "number"))
    operator = SelectField("Operátor", choices=[("+" ,"+"), ("-", "-"), ("*", "*"), ("/", "/")])
    druhe_cislo = IntegerField("Druhé Číslo", widget = widgets.Input(input_type = "number"))

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


if __name__ == "__main__":
    app.run(debug=True)
