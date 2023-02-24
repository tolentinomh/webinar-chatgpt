from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def mostrar_imagen():
    if request.method == 'POST':
        search_term = request.form['search_term']
        url = f'https://source.unsplash.com/random/?{search_term}'
        mas_imagenes = f'Más imágenes de {search_term}'
    else:
        url = 'https://source.unsplash.com/random/'
        mas_imagenes = None

    response = requests.get(url)
    return render_template('imagen.html', imagen=response.url, mas_imagenes=mas_imagenes, search_term=search_term)

if __name__ == '__main__':
    app.run(debug=True)
