from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def show_map():
    # Pass the API key to the HTML template
    return render_template('index.html', api_key='by8SADPYLTMT42ogjmEempVqI9sJ23xOKhgTYmO8FRk')

if __name__ == '__main__':
    app.run(debug=True)