from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "Geschichte Lego®: Sie begann 1932 im jütländischen Billund in Dänemark, als der Tischler Ole Kirk Christiansen ein kleines Unternehmen, das Holzspielzeug herstellte, gründete. 1934 gab er seiner Firma den Namen Lego®, der sich von dem dänischen Ausdruck „leg godt®“ für „spiel gut®“ ableitet."
if __name__ == "__main__":
    app.run(debug=True)