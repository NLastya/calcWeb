from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        if not num1 or not num2:
            error = "Введите оба числа!"
            return render_template("calculator.html", result=error)

        try:
            num1 = float(num1)
            num2 = float(num2)

        except Exception:
            error = "Неверный формат данных."
            return render_template("calculator.html", result=error)

        operator = request.form['operator']
        result = None

        if operator == 'add':
            result = num1 + num2
        elif operator == 'subtract':
            result = num1 - num2
        elif operator == 'multiply':
            result = num1 * num2
        elif operator == 'divide':
            if num2 == 0:
                error = "Деление на 0 невозможно."
                return render_template("calculator.html", result=error)
            else:
                result = num1 / num2

        return render_template('calculator.html', result=result)
    else:
        return render_template('calculator.html')

if __name__ == '__main__':
    app.run(debug=True)
