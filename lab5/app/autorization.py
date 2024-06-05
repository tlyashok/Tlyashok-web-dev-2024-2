from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_login import (
    LoginManager,
    UserMixin,
    login_required,
    login_user,
    logout_user,
)

from app import (
    db_connector,
)

bp = Blueprint('auth', __name__, url_prefix='/auth')


class User(UserMixin):
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username


def init_login_manager(app):
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Авторизируйтесь для доступа на эту страницу.'
    login_manager.login_message_category = 'warning'
    login_manager.user_loader(load_user)


def load_user(user_id):
    with db_connector.connect().cursor(dictionary=True) as cursor:
        query = """
            SELECT * FROM Users WHERE id = %s
        """

        cursor.execute(query, (user_id,))
        user = cursor.fetchone()
    return User(user_id, user['login'])


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        remember = bool(request.form.get('remember'))

        with db_connector.connect().cursor(dictionary=True) as cursor:

            query = """
                SELECT * FROM Users WHERE login = %s AND
                password = SHA2(%s, 256)
            """

            cursor.execute(query, (username, password))

            user = cursor.fetchone()

        if user is not None:
            user = User(user['id'], username)
            login_user(user, remember=remember)
            flash('Успешная авторизация!', category='success')
            ref_url = request.form.get('next')
            if ref_url is not None:
                return redirect(ref_url)
            return render_template('login.html')

        flash('Неверный логин или пароль!', category='danger')
    return render_template('login.html')


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
