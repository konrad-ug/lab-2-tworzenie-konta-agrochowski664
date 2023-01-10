from flask import Flask, request, jsonify
from .RejestrKont import Rejestr
from .Konto import Konto



app = Flask(__name__)

@app.route("/konta/stworz_konto", methods=['POST'])
def stworz_konto():
    dane = request.get_json()
    print(f"Request o stworzenie konta z danymi: {dane}")
    konto_nowe = Konto(dane["imie"], dane["nazwisko"], dane["pesel"])
    wynik = Rejestr.dodaj(konto_nowe)
    if wynik:
        return jsonify("Konto stworzone"), 201
    else:
        return jsonify("Err, Konto nie stworzone!"), 400

@app.route("/konta/ile_kont", methods=['GET'])
def ile_kont():
#Twoja implementacja endpointu
    return jsonify(ilosc_kont=Rejestr.liczba_kont())



@app.route("/konta/konto/<pesel>", methods=['GET'])
def wyszukaj_konto_z_peselem(pesel):
    #Twoja implementacja endpointu
    acc = Rejestr.znajdz(pesel)
    if acc:
        return jsonify(imie=acc.imie, nazwisko=acc.nazwisko, pesel=acc.pesel), 200
    else:
        return jsonify(imie=None, nazwisko=None, pesel=None), 200
