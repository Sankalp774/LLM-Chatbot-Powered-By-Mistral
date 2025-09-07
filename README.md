#LLM-Chatbot-Powered-By-Mistral

A basic LLM-101 Project.

🤖 LLM Chat Application
A modern, responsive web-based AI chat application built with HTML/CSS/JavaScript frontend and Python Flask backend, powered by HuggingFace AI models.


✨ Features

🎨 Modern UI/UX - Beautiful gradient design with smooth animations
🤖 AI-Powered Chat - Integration with HuggingFace AI models
📱 Responsive Design - Works perfectly on desktop and mobile
⚡ Real-time Chat - Instant responses with typing indicators
🔧 Easy Setup - Simple installation and configuration
🛡️ Error Handling - Robust error handling with fallback responses
🎯 CORS Enabled - Proper frontend-backend communication

🚀 Quick Start
Prerequisites

Python 3.8 or higher
VS Code (recommended)
HuggingFace account (free)

🛠️ Technical Stack
Frontend

HTML5 - Semantic markup structure
CSS3 - Modern styling with animations and gradients
JavaScript (ES6+) - Interactive functionality and API communication
Fetch API - HTTP requests to backend

Backend

Python 3.8+ - Server-side programming
Flask 3.0.0 - Web framework
Flask-CORS - Cross-origin resource sharing
Requests - HTTP library for API calls
HuggingFace API - AI model integration

🔧 API Endpoints
MethodEndpointDescriptionGET/Backend status and health checkPOST/api/chatSend message and get AI response

🔍 Features in Detail
Frontend Features

Animated UI Elements - Smooth transitions and hover effects
Typing Indicators - Shows when AI is processing
Message History - Scrollable chat history
Responsive Design - Mobile-friendly interface
Error Handling - User-friendly error messages

Backend Features

AI Integration - Multiple HuggingFace model support
Error Recovery - Fallback responses when API fails
Request Validation - Input sanitization and validation
Logging - Detailed console logging for debugging
CORS Support - Proper cross-origin handling

🔄 API Models
The application supports multiple AI models:

microsoft/DialoGPT-medium (Default) - Conversational AI
gpt2 - Fallback model
Custom models - Easy to add new HuggingFace models

To change models, modify the api_url in call_huggingface_api() function.
📈 Performance

Response Time: ~2-5 seconds (depending on model)
Concurrent Users: Up to 10 (Flask development server)
Message Length: Up to 500 characters
Browser Support: All modern browsers

🔒 Security Considerations

API tokens are stored server-side only
Input validation and sanitization
CORS properly configured
No sensitive data stored in frontend
Rate limiting can be added for production

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
🙏 Acknowledgments

HuggingFace for providing free AI model APIs
Flask for the excellent web framework
Microsoft DialoGPT for the conversational AI model

