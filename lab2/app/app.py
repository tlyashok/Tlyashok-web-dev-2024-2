from flask import Flask, render_template, request

app = Flask(__name__)

application = app


def validate_phone_number(phone):
    if len(phone) < 10 or len(phone) > 11:
        return False, 'Недопустимый ввод. Неверное количество цифр.'
    elif not all(c.isdigit() or c in '+()-. ' for c in phone):
        phone = ''.join(c for c in phone if c.isdigit())
        return False, (
            'Недопустимый ввод. В номере телефона '
            'встречаются недопустимые символы.'
        )
    return True, format_phone_number(phone)


def format_phone_number(phone):
    digits = ''.join(c for c in phone if c.isdigit())
    if len(digits) == 10:
        digits = '8' + digits
    formatted_phone = '8-{}-{}-{}-{}'.format(
        digits[1:4], digits[4:7], digits[7:9], digits[9:])
    return formatted_phone


@app.route('/phone_form', methods=['GET', 'POST'])
def phone_form():
    errors = None
    formatted_phone = None
    if request.method == 'POST':
        phone_number = request.form['phone_number']
        valid, message = validate_phone_number(phone_number)
        if valid:
            formatted_phone = message
        else:
            errors = message
    return render_template('phone_form.html', errors=errors,
                           formatted_phone=formatted_phone)


@app.route('/')
def index():
    return render_template('index.html',
                           params=request.args,
                           headers=request.headers,
                           cookies=request.cookies)