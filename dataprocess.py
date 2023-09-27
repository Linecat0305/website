from flask import Flask, request, render_template
import json

with open('database.json','r') as json_file:
    old_data = json.load(json_file)

app = Flask(__name__)

@app.route('/process_data', methods=['POST'])
def process_data():
    date = request.form.get('date')
    noon = request.form.get('noon')
    subject = request.form.get('subject')
    text = request.form.get('item')
    
    app.config['date'] = date
    app.config['noon'] = noon
    app.config['subject'] = subject
    app.config['text'] = text
    join_data = f"{date}{noon} {text}"

    old_data[subject].append(join_data)
    with open('database.json', 'w') as json_file:
        json.dump(old_data, json_file, indent=4)

    return None

if __name__ == '__main__':
    app.run()