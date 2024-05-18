from flask import Flask, render_template
import urllib.request
import json

app = Flask(__name__)

@app.route("/")
def home():
    # Fetch data from the URL
    url = "http://172.31.255.11/netio.json"
    try:
        with urllib.request.urlopen(url) as response:
            json_data = response.read().decode('utf-8')
            measurement_dict = json.loads(json_data)
            print(measurement_dict)  # Print the entire JSON response
            plot_data = measurement_dict.get('plot_energy_consumption', None)
            if plot_data:
                return render_template('index.html', plot_data=plot_data)
            else:
                return "Plot data not found in JSON response"
    except Exception as e:
        return f"Error fetching data: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Specify the port here
