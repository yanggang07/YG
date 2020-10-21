from flask import Flask, render_template

"""
{
    "webserver": "flask"   
    "front": "Bootstrap"
}
"""

app = Flask("주하진")


@app.route("/")
def front():
    return render_template("front.html")


@app.route("/see_juhajin/")
def ju():
    return "주하진"


@app.route("/question/")
def question():
    return "코가 부푸나요? ㅇㅇ 코가 부푼대!"


if __name__ == '__main__':
    app.run()
    # 사람은 왜 살까
    # 왜 태어난걸까
    # > 파이참을 키기 위해 태어난 사람.
    # 역: converse
    # 이: inverse
    # 대우
