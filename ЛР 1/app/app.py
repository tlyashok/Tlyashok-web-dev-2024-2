import random
from flask import Flask, render_template, request, redirect, url_for
from faker import Faker

fake = Faker()

app = Flask(__name__)
application = app

POST_LIST_LEN = 5

images_ids = [
    '7d4e9175-95ea-4c5f-8be5-92a6b708bb3c',
    '2d2ab7df-cdbc-48a8-a936-35bba702def5',
    '6e12f3de-d5fd-4ebb-855b-8cbc485278b7',
    'afc2cfe7-5cac-4b80-9b9a-d5c65ef0c728',
    'cab5b7f2-774e-4884-a200-0c0180fa777f',
]

avatars = [
    'avatar1.svg',
    'avatar2.svg',
    'avatar3.svg',
]


def generate_post(i):
    return {
        'id': i,
        'title': fake.sentence(nb_words=6),
        'text': fake.paragraph(nb_sentences=100),
        'author': fake.name(),
        'date': fake.date_time_between(start_date='-2y', end_date='now'),
        'image_id': f'{images_ids[i]}.jpg',
        'comments': []
    }


posts_list = {key: value for key, value in
              zip(list(range(0, POST_LIST_LEN)),
                  [generate_post(i) for i in range(POST_LIST_LEN)])}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/posts')
def posts():
    p = sorted([posts_list[i] for i in range(POST_LIST_LEN)],
               key=lambda x: x['date'],
               reverse=True)
    return render_template('posts.html', title='Посты', posts=p)


@app.route('/posts/<int:post_id>')
def post(post_id):
    return render_template(
        'post.html', title=posts_list[post_id]['title'],
        post=posts_list[post_id],
        post_id=post_id
        )


@app.route('/about')
def about():
    return render_template('about.html', title='Об авторе')


@app.route('/posts/<int:post_id>/comments/add_comment', methods=['POST'])
def add_comment(post_id):
    comment_text = request.form.get('comment_text')
    author_text = request.form.get('author_comment')
    posts_list[post_id]['comments'].append({
        'id': len(posts_list[post_id]['comments']),
        'author': author_text,
        'text': comment_text,
        'avatar_image': avatars[random.randint(0, len(avatars)-1)],
        'replies': []
    })
    return redirect(url_for('post', post_id=post_id))


@app.route('/posts/<int:post_id>/comments/<int:comment_id>/add_reply',
           methods=['POST'])
def add_reply(post_id, comment_id):
    comment_text = request.form.get('comment_text_reply')
    author_text = request.form.get('author_text_reply')
    posts_list[post_id]['comments'][comment_id]['replies'].append({
        'id': len(posts_list[post_id]['comments'][comment_id]['replies']),
        'author': author_text,
        'text': comment_text,
        'avatar_image': avatars[random.randint(0, len(avatars)-1)],
    })
    return redirect(url_for('post', post_id=post_id))

