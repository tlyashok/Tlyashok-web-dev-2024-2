from flask import (
    Flask,
    flash,
    get_flashed_messages,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

from flask_login import (
    LoginManager,
    UserMixin,
    login_required,
    login_user,
    logout_user,
)

app = Flask(__name__)
app.secret_key = '25c90e325b2f17da21834f3d65d96a06'
application = app

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Авторизируйтесь для доступа на эту страницу.'
login_manager.login_message_category = 'warning'


class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id


users = {'user': {'password': 'user'}}


@login_manager.user_loader
def load_user(user_id):
    return User(user_id)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        remember = True if request.form.get('remember') else False

        if username in users and users[username]['password'] == password:
            user = User(username)
            login_user(user, remember=remember)
            flash('Успешная авторизация!', category='success')
            ref_url = request.form.get('next')
            if bool(ref_url):
                return redirect(ref_url)
            else:
                if ref_url == '':
                    return redirect(url_for('index'))
                return render_template('login.html', next=request.endpoint)

        flash('Неверный логин или пароль!', category='danger')
        return render_template('login.html')

    elif request.method == 'GET':
        return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/secret')
@login_required
def secret():
    return render_template('secret.html', next=request.endpoint)


@app.route('/visit-counter')
def visit_counter():
    session['visits'] = session.get('visits', 0) + 1
    return render_template('visit-counter.html', visits=session['visits'])


if __name__ == '__main__':
    app.run(debug=True)
