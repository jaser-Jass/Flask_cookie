from flask import Flask, render_template, request, make_response, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('input.html')

@app.route('/welcome', methods=['POST'])
def welcome():
    name = request.form['name']
    email = request.form['email']
    
    response = make_response(redirect('/greet'))
    response.set_cookie('user', '|'.join([name, email]))
    
    return response

@app.route('/greet')
def greet():
    user_cookie = request.cookies.get('user')
    if user_cookie:
        name = user_cookie.split('|')[0]
        return render_template('greet.html', name=name)
    else:
        return redirect('/')

@app.route('/logout')
def logout():
    response = make_response(redirect('/'))
    response.set_cookie('user', '', expires=0)
    return response

if __name__ == '__main__':
    app.run(debug=True)