from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    job_description = request.json.get('jobDescription')
    resume = request.json.get('resume')

    # Handle OpenAI API call here with sanitized inputs
    # ...

    # Send back the response to the client
    return jsonify({'success': True, 'message': 'Cover letter generated successfully.'})

if __name__ == '__main__':
    app.run(debug=True)
