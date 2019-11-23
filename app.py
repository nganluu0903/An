from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
   return render_template("index.html")
@app.route('/shortofperox1.html')
def index():
   return render_template("shortofperox1.html")   
if __name__ == '__main__':
   app.run()
