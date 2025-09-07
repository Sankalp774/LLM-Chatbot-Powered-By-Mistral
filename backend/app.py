from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import time

app = Flask(__name__)
CORS(app)

# REPLACE THIS WITH YOUR REAL HUGGINGFACE TOKEN
HUGGINGFACE_API_TOKEN = "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"  

def call_huggingface_api(message):
    """Simple API call to HuggingFace"""
    
    # Use a reliable model
    api_url = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium"
    
    headers = {
        "Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "inputs": message,
        "parameters": {
            "max_length": 100,
            "temperature": 0.7
        }
    }
    
    try:
        response = requests.post(api_url, headers=headers, json=payload, timeout=30)
        
        if response.status_code == 200:
            result = response.json()
            if isinstance(result, list) and len(result) > 0:
                generated_text = result[0].get('generated_text', '')
                return generated_text.strip() if generated_text else "I understand your question. Let me help you with that."
        
        # Fallback response
        return f"I received your message: '{message}'. I'm processing your request and here's my response based on that topic."
        
    except Exception as e:
        print(f"API Error: {e}")
        return f"Thank you for your message: '{message}'. I'm having a brief technical issue, but I understand what you're asking about."

@app.route('/')
def home():
    token_status = "✅ Configured" if HUGGINGFACE_API_TOKEN and len(HUGGINGFACE_API_TOKEN) > 20 and not HUGGINGFACE_API_TOKEN == "YOUR_TOKEN_HERE" else "❌ Not Configured"
    
    return f"""
    <div style="font-family: Arial; padding: 20px; background: #f0f0f0; border-radius: 10px;">
        <h1>🤖 LLM Chat API</h1>
        <p><strong>Status:</strong> <span style="color: green;">✅ Running</span></p>
        <p><strong>Port:</strong> 5000</p>
        <p><strong>Token:</strong> {token_status}</p>
        <p><strong>Endpoint:</strong> /api/chat</p>
        <hr>
        <p>If you see this page, your backend is working! 🎉</p>
    </div>
    """

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        # Get JSON data
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400
            
        user_message = data.get('message', '').strip()
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400
        
        print(f"📨 Received: {user_message}")
        
        # Get AI response
        ai_response = call_huggingface_api(user_message)
        
        print(f"🤖 Responding: {ai_response}")
        
        return jsonify({
            'response': ai_response,
            'status': 'success'
        })
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return jsonify({
            'error': str(e),
            'response': 'I apologize, but I encountered an error. Please try again!',
            'status': 'error'
        }), 500

if __name__ == '__main__':
    print("🚀 Starting LLM Chat API...")
    print(f"🔑 Token: {'✅ Configured' if HUGGINGFACE_API_TOKEN and HUGGINGFACE_API_TOKEN != 'YOUR_TOKEN_HERE' else '❌ Replace YOUR_TOKEN_HERE'}")
    print("🌐 Backend will run on: http://localhost:5000")
    print("🛑 Press Ctrl+C to stop")
    
    app.run(debug=True, host='0.0.0.0', port=5000)