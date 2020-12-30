from flask import Flask,render_template
app = Flask(__name__)

all_posts=[
    {
        'title':'Post 1',
        'content': 'This is the content of post 1',
        'author':'harsh'
    },
    {
        'title':'Post 2',
        'content': 'This is the content of post 2'
    }
]

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/post')
def posts():
    return render_template('post.html',posts=all_posts)

@app.route("/name/<string:name>")
def home(name):
    return "Hello" + name

@app.route('/onlyget',methods=['POST'])
def req_req():
    return "you can only get it"

if __name__=="__main__":
    app.run(debug=True)