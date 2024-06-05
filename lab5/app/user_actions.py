import csv
from io import BytesIO
from math import ceil

from flask import Blueprint, render_template, request, send_file

from app import db_connector

bp = Blueprint('user_actions', __name__, url_prefix='/user_actions')
MAX_PER_PAGE = 10


@bp.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    with db_connector.connect().cursor(named_tuple=True) as cursor:
        query = (f"""
                    SELECT last_name, first_name, middle_name, 
                    path, Action_logs.created_at AS created_at 
                    FROM Action_logs LEFT JOIN 
                    Users ON Action_logs.user_id = Users.id 
                    LIMIT {MAX_PER_PAGE} OFFSET {(page - 1) * MAX_PER_PAGE}
                 """)  # noqa: W291
        cursor.execute(query)
        user_actions = cursor.fetchall()

        query = 'SELECT COUNT(*) as count FROM Action_logs'
        cursor.execute(query)
        record_count = cursor.fetchone().count
        page_count = ceil(record_count / MAX_PER_PAGE)
        pages = range(max(1, page - 3), min(page_count, page + 3)+1)
    return render_template('user_actions/index.html', user_actions=user_actions,
                            page=page, pages=pages, page_count=page_count)


@bp.route('users_stats')
def users_stats():
    with db_connector.connect().cursor(dictionary=True) as cursor:
        query = ("""
                    SELECT user_id, last_name, first_name, middle_name, 
                    COUNT(*) AS entries_counter 
                    FROM Action_logs LEFT JOIN 
                    Users ON Action_logs.user_id = Users.id 
                    GROUP BY user_id 
                 """)  # noqa: W291
        cursor.execute(query)
        users_stats = cursor.fetchall()
    return render_template('user_actions/users_stats.html', users_stats=users_stats)


@bp.route('user_export.csv')
def user_export():
    with db_connector.connect().cursor(dictionary=True) as cursor:
        query = ("""
                    SELECT Users.id as user_id, last_name, first_name, middle_name, 
                    COUNT(*) AS entries_counter 
                    FROM Action_logs LEFT JOIN 
                    Users ON Action_logs.user_id = Users.id 
                    GROUP BY user_id 
                 """)  # noqa: W291
        cursor.execute(query)
        users_stats = cursor.fetchall()
        result = ''
        fields = ['last_name', 'first_name', 'middle_name', 'entries_counter']
        none_values = ['не', 'авторизованный', 'пользователь']
        result += ','.join(fields)+'\n'
        for record in users_stats:
            if record['user_id'] is None:
                result += ','.join(none_values)+','+str(record.entries_counter)+'\n'
                continue
            result += ','.join([str(record[field]) for field in fields])+'\n'
    return send_file(
        BytesIO(result.encode()),
        as_attachment=True,
        mimetype='text/csv',
        download_name='user_export.csv',
    )


@bp.route('path_export.csv')
def path_export():
    with db_connector.connect().cursor(dictionary=True) as cursor:
        query = ("""
                    SELECT path, COUNT(*) AS entries_counter 
                    FROM Action_logs
                    GROUP BY path
                 """)  # noqa: W291
        cursor.execute(query)
        path_stats = cursor.fetchall()
        result = ''
        fields = ['path', 'entries_counter']
        result += ','.join(fields)+'\n'
        for record in path_stats:
            result += ','.join([str(record[field]) for field in fields])+'\n'
    return send_file(
        BytesIO(result.encode()),
        as_attachment=True,
        mimetype='text/csv',
        download_name='path_export.csv',
    )


@bp.route('paths_stats')
def paths_stats():
    with db_connector.connect().cursor(named_tuple=True) as cursor:
        query = ("""
                    SELECT path, COUNT(*) AS entries_counter 
                    FROM Action_logs
                    GROUP BY path
                 """)  # noqa: W291
        cursor.execute(query)
        path_stats = cursor.fetchall()
    return render_template('user_actions/paths_stats.html', path_stats=path_stats)
