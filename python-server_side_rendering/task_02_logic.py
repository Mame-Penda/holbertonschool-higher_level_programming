#!/usr/bin/python3
from flask import Flask, render_template, json

app = Flask(__name__)

@app.route('/items')
def items():
    try:
        # Lire le fichier JSON
        with open('items.json', 'r') as file:
            data = json.load(file)
            items_list = data.get("items", [])
    except Exception as e:
        items_list = []  # Si erreur, on affiche une liste vide
    
    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
