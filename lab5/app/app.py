import config
from flask import (
    Flask,
    render_template,
    request,
    session,
)
from flask_login import (
    UserMixin,
    login_required,
)
from mysqldb import (
    DBConnector,
)

app = Flask(__name__)
app.config.update(
    MYSQL_USER=config.MYSQL_USER,
    MYSQL_PASSWORD=config.MYSQL_PASSWORD,
    MYSQL_HOST=config.MYSQL_HOST,
    MYSQL_DATABASE=config.MYSQL_DATABASE,
    SECRET_KEY=config.SECRET_KEY,
    ADMIN_ROLE_ID=config.ADMIN_ROLE_ID,
)

application = app


with app.app_context():
    db_connector = DBConnector(app)
    from autorization import bp as auth_bp
    from autorization import init_login_manager
    from users import bp as users_bp

app.register_blueprint(auth_bp)
app.register_blueprint(users_bp)
init_login_manager(app)

@app.route('/')
def index():
    return render_template('index.html')


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
