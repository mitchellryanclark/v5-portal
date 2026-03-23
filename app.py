from flask import Flask, render_template, request, jsonify
import time
import os

app = Flask(__name__)

# Load template from external file
TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), 'prompt_template.txt')

def load_template():
    try:
        with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return "Error: Template file not found."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    
    if not data or not data.get('seed'):
        return jsonify({"error": "Priority is required"}), 400
        
    seed_phrase = data.get('seed')
    
    # This delay makes it feel like the AI is "thinking"
    time.sleep(1.5) 
    
    V5_MASTER_TEMPLATE = load_template()
    
    if V5_MASTER_TEMPLATE.startswith("Error:"):
        return jsonify({"error": V5_MASTER_TEMPLATE}), 500
        
    # This puts your seed phrase into the prompt
    compiled_prompt = V5_MASTER_TEMPLATE.replace("{seed_phrase}", seed_phrase)
    
    return jsonify({"prompt": compiled_prompt})

if __name__ == '__main__':
    app.run(debug=True, port=5000)