from flask import Flask, render_template, url_for

app = Flash(__name__)

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run()
