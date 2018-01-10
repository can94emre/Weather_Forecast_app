from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/temperature', methods=['POST'])
def temperature():
    cityname = request.form['name']
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?&appid=1c30126758d01c464c8df828768f4188&q='+cityname+'')
    json_object = r.json()
    temp_k =float(json_object['main']['temp'])
    temp_f = (temp_k - 273.15)
    return render_template('temperature.html', temp=temp_f)

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
