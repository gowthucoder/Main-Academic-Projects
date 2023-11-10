from flask import Flask, render_template
import requests

app = Flask("Portfolio")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_repositories')
def get_repositories():
    github_username = 'gowthucoder'
    response = requests.get(f'https://api.github.com/users/{github_username}/repos')
    repositories = response.json()
    return {'repositories': repositories}

if __name__ == '__main__':
    app.run(debug=True)
