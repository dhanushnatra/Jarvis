# Jarvis

Minimal Personal AI Assistant

## Installation

### Prerequisites

- Node.js and npm
- Python 3.10+ ( 3.14 recommended )

### Tailwind CSS CLI Setup

```bash
npm install
```

### Python Flask Setup

```bash
python -m venv env
source env/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Project Explanation

Jarvis is a full-stack application combining:

- **Frontend**: Tailwind CSS for styling
- **Backend**: Flask for server-side logic

The project integrates a Node.js build pipeline with a Python web framework for rapid development.

## Usage

### Development Mode

```bash
npm run watch | python main.py
```

### Build for Production

```bash
npx tailwindcss -i ./input.css -o ./static/output.css --minify
```

Visit `http://localhost:8000` in your browser.
