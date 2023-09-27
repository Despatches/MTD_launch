from flask import render_template

@app.route('/runner')
@app.route('/index')
def index():
	user = {"username":"miguel", "surname":"peterson"}
	return render_template('index.html', user=user)

