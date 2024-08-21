from flask import Flask, render_template, jsonify, request
import openai

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/services')
def services():
    return render_template('services.html')


@app.route('/education')
def education():
    return render_template('education.html')


@app.route('/experience')
def experience():
    return render_template('experience.html')


@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/playground')
def playground():
    return render_template('playground.html')


openai.api_key = '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'


@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if you have access
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        # Print the raw response for debugging
        print(response)

        # Access the content of the message
        reply = response['choices'][0]['message']['content']

        return jsonify({'response': reply})
    except Exception as e:
        print(f"Error: {e}")  # Print the error for debugging
        return jsonify({'error': str(e)}), 500



if __name__ == '__main__':
    app.run(debug=True)
