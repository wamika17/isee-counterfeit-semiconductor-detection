from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():

    return """
    <h1>iSEE Counterfeit Semiconductor Detection System</h1>

    <h2>Dashboard Under Development</h2>

    <p>Serial communication established.</p>
    """

if __name__ == "__main__":
    app.run(debug=True)
