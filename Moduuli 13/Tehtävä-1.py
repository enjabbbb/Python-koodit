from flask import Flask, request
app = Flask(__name__)
@app.route("/alkuluku/<int:number>")
def alkuluku(number):
    if number <= 1:
        is_prime = False
    else:
        is_prime = True
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_prime = False
                break
    answer = {"number": number, "is_prime": is_prime}
    return answer

app.run(use_reloader=True, host="127.0.0.1", port=3000)
