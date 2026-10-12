
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    words = None
    chars = None
    percentage = None
    error = None
    exam_message = None
    exam_details = {}

    if request.method == "POST":
        tool = request.form.get("tool", "word")

        if tool == "percentage":
            try:
                marks = float(request.form.get("marks", ""))
                total = float(request.form.get("total", ""))

                if total <= 0 or marks < 0 or marks > total:
                    error = "Please enter valid marks."
                else:
                    percentage = round(marks / total * 100, 2)
            except ValueError:
                error = "Please enter valid numbers."

        elif tool == "exam":
            exam_details = {
                "board": "CBSE",
                "class_name": request.form.get("class_name", ""),
                "subject": request.form.get("subject", ""),
                "chapter_name": request.form.get(
                    "chapter_name", ""
                ).strip(),
                "chapter_number": request.form.get(
                    "chapter_number", ""
                ).strip(),
                "author": request.form.get("author", "").strip()
            }

            if not exam_details["class_name"] or not exam_details["subject"]:
                exam_message = "Please select your class and subject."
            elif not exam_details["chapter_name"] and not exam_details["chapter_number"]:
                exam_message = "Please enter a chapter name or chapter number."
            else:
                exam_message = (
                    "Your chapter search form is connected. "
                    "Verified CBSE chapter content will be added next."
                )

        else:
            text = request.form.get("text", "")
            words = len(text.split())
            chars = len(text)

    return render_template(
        "index.html",
        words=words,
        chars=chars,
        percentage=percentage,
        error=error,
        exam_message=exam_message,
        exam_details=exam_details
    )


if __name__ == "__main__":
    app.run(debug=True)
