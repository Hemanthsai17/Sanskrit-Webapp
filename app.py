from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def index():
    file_list = get_file_list()
    return render_template('index.html', file_list=file_list)

# ... (previous code remains unchanged)

@app.route('/label/<file_name>', methods=['GET', 'POST'])
def label(file_name):
    data = read_excel(file_name)

    if request.method == 'POST':
        selected_sentiments = request.form.getlist('sentiments')
        current_index = int(request.form['current_index'])

        # Update Excel file
        update_excel(file_name, selected_sentiments, current_index)

        # Check if there are more instances or redirect to the main page
        if current_index + 1 < data.shape[0]:
            return redirect(url_for('label', file_name=file_name, current_index=current_index + 1))
        else:
            return redirect('/')

    # Read data from Excel file
    current_index = int(request.args.get('current_index', 0))

    return render_template('label.html', data=data, current_index=current_index, file_name=file_name)

# ... (rest of the code remains unchanged)

def get_file_list():
    return [file for file in os.listdir('data') if file.endswith('.xlsx')]

def read_excel(file_name):
    file_path = os.path.join('data', file_name)
    return pd.read_excel(file_path)

def update_excel(file_name, selected_sentiments, current_index):
    file_path = os.path.join('data', file_name)
    data = pd.read_excel(file_path)

    # Update sentiment columns for the current instance
    for sentiment in selected_sentiments:
        data.at[current_index, sentiment] = 1

    # Save the updated DataFrame to the Excel file
    data.to_excel(file_path, index=False)

if __name__ == '__main__':
    app.run(debug=True)
