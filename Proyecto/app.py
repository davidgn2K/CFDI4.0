from flask import Flask 
from views import views

app =  Flask(__name__)
app.register_blueprint(views, url_prefix="/views")

if __name__ == '__main__':
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 10
    app.run(debug=True, port=8000)

