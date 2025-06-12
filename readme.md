# AI Agent

A powerful AI agent application built with Python, Streamlit, and Ollama for local LLM inference with embedding capabilities.

## Features

- 🤖 Local LLM inference using Ollama
- 🔍 Embedding model integration for semantic search
- 🌐 Web interface built with Streamlit
- 🚀 Easy setup and deployment
- 💻 Cross-platform support (Windows, macOS, Linux)

## Prerequisites

- Python 3.8 or higher
- Git

## Installation

### 1. Install Ollama

Download and install Ollama based on your operating system:

#### Windows
```bash
# Download from https://ollama.ai/download/windows
# Run the installer and follow the setup wizard
```

#### macOS
```bash
# Download from https://ollama.ai/download/mac
# Or install via Homebrew:
brew install ollama
```

#### Linux
```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

### 2. Clone the Repository

```bash
git clone https://github.com/devyani1512/ai_agent.git
cd ai_agent
```

### 3. Set Up Python Virtual Environment

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Download and Set Up Models

#### Download LLM Model
```bash
# Download a recommended model (e.g., llama2, mistral, or codellama)
ollama pull llama2
```

#### Install Embedding Model
```bash
# Download an embedding model for semantic search
ollama pull nomic-embed-text
```

### 6. Configure the Application

Before running the application, make sure to configure the settings:

1. Open the configuration file (if applicable)
2. **Important**: Change the ngrok configuration to localhost for local development:
   - Look for any ngrok URLs in the code
   - Replace with `localhost` or `127.0.0.1`
   - Update port configurations as needed

## Usage

### Running the Application

```bash
# Make sure your virtual environment is activated
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Start the Streamlit application
streamlit run main.py
```

The application will be available at `http://localhost:8501` by default.

### Using the AI Agent

1. Open your web browser and navigate to the Streamlit URL
2. Interact with the AI agent through the web interface
3. Upload documents or enter queries as supported by the application
4. The agent will process your requests using the local LLM

## Configuration

### Model Configuration

You can configure which models to use by modifying the appropriate configuration files:

- **LLM Model**: Change the model name in the configuration (e.g., `llama2`, `mistral`, `codellama`)
- **Embedding Model**: Update the embedding model if needed (e.g., `nomic-embed-text`)

### Network Configuration

For local development:
- Use `localhost` or `127.0.0.1`
- Default port is typically `8501` for Streamlit

For external access:
- Configure appropriate firewall rules
- Consider using ngrok for secure tunneling (optional)

## Troubleshooting

### Common Issues

main.py --port 8502
   ```
 **Virtual environment issues**: Make sure you're in the correct directory and the venv is activated



### Project Structure

```
ai_agent/
├── main.py              # Main Streamlit application
├── requirements.txt     # Python dependencies
├── venv/               # Virtual environment (created during setup)
├── config/             # Configuration files
└── README.md           # This file
```


