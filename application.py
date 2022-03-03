from flask import Flask, render_template, request
application = Flask(__name__)

@application.route('/', methods=['POST','GET'])

def root_page():
    name = ''
    kg = ''  # weight
    m = ''   # height
    bmi = 0
    if request.method == 'POST' and 'username' in request.form:
        name = request.form.get('username')
        kg = request.form.get('user_kg')
        m = request.form.get('user_m')
        bmi = round(float(kg)/float(m)**2)
        # inputs are string, so convert to float
    return render_template("index.html", name=name, kg=kg, m=m, bmi=bmi)

if __name__ == '__main__':
    application.run(debug=True)
