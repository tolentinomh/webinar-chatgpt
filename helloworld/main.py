from flask import Flask, render_template, send_file, request
import random
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Obtener el parámetro de búsqueda de la solicitud
    parametro_busqueda = request.args.get('busqueda')
    # Crear la URL de la imagen de Unsplash
    if parametro_busqueda:
        url_imagen = f'https://source.unsplash.com/random/?{parametro_busqueda}'
    else:
        url_imagen = 'https://source.unsplash.com/random/'
    return render_template('index.html', url_imagen=url_imagen)

@app.route('/descargar-imagen')
def descargar_imagen():
    # Obtener la ruta de la imagen seleccionada
    url_imagen = request.args.get('url_imagen')
    # Obtener el nombre del archivo
    nombre_archivo = os.path.basename(url_imagen)
    # Descargar la imagen
    return send_file(url_imagen, as_attachment=True, attachment_filename=nombre_archivo)

if __name__ == '__main__':
    app.run(debug=True)
