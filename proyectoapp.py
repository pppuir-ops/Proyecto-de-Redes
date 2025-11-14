from flask import Flask, render_template
app=Flask(__name__)
#definiendo rutas
@app.route('/')
def Home():
    return Home('redes')

if __name__ == '__main__':
    app.run(debug=True)