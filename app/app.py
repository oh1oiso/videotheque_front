from flask import Flask, render_template, request, redirect, url_for
import os
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/formulaire')
def formulaire():
    return render_template('form_page.html')

@app.route('/inscription', methods=['POST'])
def inscription():
    nom = request.form.get('nom')
    prenom = request.form.get('prenom')
    login = request.form.get('login')
    mot_de_passe = request.form.get('mot_de_passe')

    # Process registration data (add to a database, etc.)
    # For now, just print the data
    print(f"Inscription réussie : Nom = {nom}, Prénom = {prenom}, Login = {login}")

    return render_template('inscription_success.html', nom=nom, prenom=prenom)

@app.route('/videotheque')
def videotheque():
    return render_template('videotheque.html')

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    print(f"Starting the app on port {port}")
    app.run(debug=True, host='0.0.0.0', port=port, use_reloader=True)
