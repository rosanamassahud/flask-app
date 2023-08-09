from flask import Flask, render_template

# Nova linha inserida
#from flaskwebgui import FlaskUI

app = Flask(__name__)
#app.config.from_pyfile('config.py')
# Nova linha inserida
#ui = FlaskUI(app, width=500, height=500)

@app.route('/')
def index_page():
    return render_template('index.html')

if(__name__=='__main__'):
    # linha de execução da aplicação comentada, para que  o flaskwebgui faça esse trabalho
    
    app.run(port=3000)

    # Nova linha inserida
    #ui.run()