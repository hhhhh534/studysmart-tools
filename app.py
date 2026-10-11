
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    words = None
    chars = None
    percentage = None
    error = None

    if request.method == "POST":
        if request.form.get("tool") == "percentage":
            try:
                marks = float(request.form.get("marks", ""))
                total = float(request.form.get("total", ""))

                if total <= 0 or marks < 0 or marks > total:
                    error = "Please enter valid marks."
                else:
                    percentage = round(marks / total * 100, 2)
            except ValueError:
                error = "Please enter valid numbers."
        else:
            text = request.form.get("text", "")
            words = len(text.split())
            chars = len(text)

    return render_template(
        "index.html",
        words=words,
        chars=chars,
        percentage=percentage,
        error=error
    )

if __name__ == "__main__":
    app.run(debug=True)


