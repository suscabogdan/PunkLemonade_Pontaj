from flask import Flask, render_template

app = Flask(__name__)

def read_log_file():
    # Citește ultimele N linii din fișierul de log; modifică N după necesități
    try:
        with open("/home/punklemonade/Desktop/Pontaj/pontaj_output.txt", "r") as file:
            log_content = file.readlines()
            print(log_content)
            return log_content
    except FileNotFoundError:
        return ["Log file not found."]
    except Exception as e:
        return [f"Error reading log file: {e}"]

@app.route('/')
def index():
    log_content = read_log_file()
    return render_template('index.html', log_content=log_content)

def start_flask_app():
    app.run(host='0.0.0.0', port=8080, use_reloader=False, debug=False)

if __name__ == "__main__":
    start_flask_app()
