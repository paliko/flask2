from flask import Flask, render_template, request

app = Flask(__name__)

def secti(a, b):
    return float(a) + float(b)

def odecti(a, b):
    return float(a) - float(b)

def podil(a, b):
    return float(a) / float(b)

def soucin(a, b):
    return float(a) * float(b)

@app.route("/", methods = ["GET", "POST"]) # Povolíme metody GET a POST
def kalkulacka():
    prvni_cislo = request.form.get("prvni_cislo") #Získáme hodnotu z POST requestu
    druhe_cislo = request.form.get("druhe_cislo")
    operator = request.form.get("operator")
    if prvni_cislo is None or druhe_cislo is None:
        return render_template("template.html", vysledek = "Vyplň formulář")
    if (float(druhe_cislo) == 0 and operator == "/"):
        vysledek = "Nelze dělit nulou"
        return render_template("template.html", vysledek = vysledek)
    if (operator == "+"):
        vysledek = secti(prvni_cislo, druhe_cislo)
    elif (operator == "-"):
        vysledek = odecti(prvni_cislo, druhe_cislo)
    elif (operator == "/"):
        vysledek = podil(prvni_cislo, druhe_cislo)
    elif (operator == "*"):
        vysledek = soucin(prvni_cislo, druhe_cislo)
    else:
        vysledek = "Chyba"

    return render_template("kalkulacka1.html", vysledek = vysledek) #Vrátíme naší šablonu s výsledkem

if __name__ == "__main__":
    app.run(debug=True)
