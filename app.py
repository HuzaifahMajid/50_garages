from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load garage data
df = pd.read_csv('garage_data.csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/map')
def show_map():
    df = pd.read_csv('garage_data.csv')
    data = df.to_dict(orient='records')
    return render_template('map.html', data=data)

@app.route('/dashboard')
def show_dashboard():
    df = pd.read_csv('garage_data.csv')
    return render_template('dashboard.html', data=df.to_dict(orient='records'))

@app.route('/update_status', methods=['POST'])
def update_status():
    data = request.get_json()
    house_no = data['houseNo']
    column = data['column']
    status = data['status']
    df.loc[df['House No'] == house_no, column] = status
    df.to_csv('garage_data.csv', index=False)
    return jsonify({'message': 'Status updated successfully'})

@app.route('/update_id', methods=['POST'])
def update_id():
    data = request.get_json()
    house_no = data['houseNo']
    id_value = data['idValue']
    df.loc[df['House No'] == house_no, 'ID Obtained'] = id_value
    df.to_csv('garage_data.csv', index=False)
    return jsonify({'message': 'ID updated successfully'})

@app.route('/project_details/<project_id>')
def project_details(project_id):
    """Return project details for a given project_id"""
    data = df.to_dict(orient='records')
    print(data)
    for item in data:
        if item['ID Obtained'] == project_id:
            print("hello")
            return render_template('project_details.html', project=item)
    return 'Project not found', 404


if __name__ == '__main__':
    app.run(debug=True)
