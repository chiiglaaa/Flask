from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def rootpage():
    weight = ''
    height = ''
    bmi = ''
    if request.method == "POST" and 'weight' in request.form:
        weight = float(request.form.get('weight'))
        height = float(request.form.get('height'))
        bmi = float(calc(weight, height))
        if float(bmi) < 18.5:
            bmi = "%.2f" % bmi
            bmi += ' You are underweight'
        elif float(bmi) >= 18.5 and float(bmi) <= 24.9:
            bmi = "%.2f" % bmi
            bmi += ' You are healthy'
        elif float(bmi) > 24.9 and float(bmi) <= 29.9:
            bmi = "%.2f" % bmi
            bmi += ' You are overweight'
        elif float(bmi) >= 30.0:
            bmi = "%.2f" % bmi
            bmi += ' You are FAT AF.'
    return render_template('index.html', weight=weight, height=height, bmi=bmi)

def calc(weight, height):
    return weight / ((height/100) ** 2)

app.run()

