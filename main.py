from TheITGirls.app import create_app
from flask import render_template

if __name__ == '__main__':
    app = create_app()
    app.run(debug='True',port='80')
