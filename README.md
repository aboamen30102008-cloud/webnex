from flask import Flask, render_template, request, redirect
from urllib.parse import quote

app = Flask(__name__)

PHONE = "201034859496"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name", "")
    phone = request.form.get("phone", "")
    service = request.form.get("service", "")
    message = request.form.get("message", "")

    text = (
        "طلب جديد من موقع Webnex\n\n"
        f"الاسم: {name}\n"
        f"رقم الهاتف: {phone}\n"
        f"الخدمة: {service}\n"
        f"الرسالة: {message}"
    )

    whatsapp_url = f"https://wa.me/{PHONE}?text={quote(text)}"

    return redirect(whatsapp_url)


if __name__ == "__main__":
    app.run(debug=True)
