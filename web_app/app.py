import numpy as np
from flask import Flask, request, render_template
import pickle
import babel.units
import decimal

#initialiseren van de app
app = Flask(__name__)

#model opvragen die gedumpt is
model = pickle.load(open('modelSAL.pkl', 'rb'))

#default pagina van de applicatie
@app.route('/')
def home():
    return render_template('index.html')

#waarden uit de form ophalen op het moment de button wordt aangeklikt
@app.route('/v_salaris',methods=['POST'])
def voorspellen_salaris():
    #waarden uit de form ophalen
    int_features = [int(x) for x in request.form.values()]
    print(int_features)
    #waarden worden bewaard
    waarden = [np.array(int_features)]
    print(waarden)
    #waarden wordt naar model gestuurd en bewaard in een variabele:
    v = model.predict(waarden)
    print(v)
    #gaat om snelheid dus wordt geformateerd:
    pr = babel.units.format_compound_unit(decimal.Decimal(v[0]), "meter", denominator_unit="second", locale="nl")

    #Waarden wordt terugestuurd naar html pagina in variable antwoord
    return render_template('index.html', antwoord= 'The predicted daily mean windspeed: ' + format(pr) )


if __name__ == "__main__":
    app.run(debug=True)