from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/test/")
def test():

    user_data = {
        "name": "Андрей",
        "number": "+ 7 (931) 260-80-65",

    }

    return render_template('test.html', user = user_data)


@app.route("/")
def page_index():
    html = "<title>Привет</title>"
    return html + "Главная страничка!!!"

# @app.route("/profile/")
# def page_profile():
#     return "Профиль пользователя"

@app.route("/feed/")
def page_feed():
    return "Лента полльзователя"


@app.route("/messages/")
def page_messages():
    return "Сообщения пользователя"


@app.route("/profile/<utm>")
def page_profile(utm):
    return f"Профиль ха {utm}"

app.run()
