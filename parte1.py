from flask import Flask
from markupsafe import escape
from flask import request

app = Flask(__name__)
# Ruta Root del tu proyecto
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# Ruta dinamica que tu ingresas
@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

# Ruta sin "/"  al final -> Error se recomeinda la siguiente opcion
@app.route("/marke")
def hello_marke():
    return f"Hello Marke!"

# Ruta especificada y sin errores
@app.route("/marke_2/")
def hello_marke2():
    return f"Hello Marke/!"


@app.route("/marke_2/marke_3")
def hello_marke3():
    return f"Hello Mark3!"

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'


