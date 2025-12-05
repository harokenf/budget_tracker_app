from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('dashboard.html')

@app.route('/expense', methods=['GET', 'POST'])
def expense():
    return render_template('expense.html')

@app.route('/reports')
def reports():
    return render_template('reports.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

if __name__ == '__main__':
    app.run(debug=True)
