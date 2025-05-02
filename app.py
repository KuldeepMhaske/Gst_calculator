from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            amount = float(request.form['amount'])
            gst_rate = float(request.form['gst_rate'])
            gst_amount = amount * gst_rate / 100
            total = amount + gst_amount
            result = {
                'original': amount,
                'gst_rate': gst_rate,
                'gst_amount': round(gst_amount, 2),
                'total': round(total, 2)
            }
        except ValueError:
            result = {'error': 'Invalid input'}
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
