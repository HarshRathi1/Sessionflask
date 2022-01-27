from flask import *
app=Flask(__name__)
app.secret_key="abc"
@app.route('/')
def home():
    res=make_response("<h4> Session is set,<a href='/get'>Get variable </a> <h4>")
    session['r']='session1'
    return res
@app.route('/get')
def getvariable():
    if 'r' in session:
        s=session['r']
        return render_template('session.html',name=s)
if __name__=='__main__':
    app.run(debug=True)