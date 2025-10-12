# AI Prompt Cost Calculator

A simple Python tool to calculate and compare API costs for different Large Language Models (LLMs) like ChatGPT and Claude

## Features

- 💰 Calculate costs for different AI models (GPT-4, GPT-3.5, Claude 3.5 Sonnet, etc.)
- 📊 Token counting for input and output
- 💾 Export cost reports to CSV
- 🔄 Batch processing for multiple prompts
- ✅ Automated tests with pytest
- 🚀 CI/CD with GitHub Actions

## Business Use Case

For AI Managers who need to:
- **Optimize costs** across different AI providers
- **Budget AI projects** accurately
- **Compare pricing** between models
- **Track usage** and expenses

## Installation

```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

### Basic calculation

```bash
python cost_calculator.py --model gpt4 --input-tokens 1000 --output-tokens 500
```

### From file

```bash
python cost_calculator.py --model claude-sonnet --file prompts.txt
```

### Export to CSV

```bash
python cost_calculator.py --model gpt4 --input-tokens 1000 --output-tokens 500 --export report.csv
```

## Supported Models

| Model | Input Price | Output Price |
|-------|-------------|--------------|
| GPT-4 | $0.03/1K tokens | $0.06/1K tokens |
| GPT-3.5 Turbo | $0.0015/1K tokens | $0.002/1K tokens |
| Claude 3.5 Sonnet | $0.003/1K tokens | $0.015/1K tokens |
| Claude 3 Haiku | $0.00025/1K tokens | $0.00125/1K tokens |

## Running Tests

```bash
pytest tests/
```

## Project Structure

```
demo-project/
├── cost_calculator.py      # Main calculator logic
├── models.py               # Model pricing data
├── export.py              # CSV export functionality
├── requirements.txt       # Python dependencies
├── tests/
│   ├── test_calculator.py
│   └── test_export.py
├── .github/
│   └── workflows/
│       └── test.yml       # CI/CD pipeline
└── README.md
```

## Development

This project demonstrates:
- ✅ Clean, modular Python code
- ✅ Automated testing with pytest
- ✅ Version control best practices
- ✅ CI/CD automation
- ✅ Business-relevant AI tooling

---

**Created for:** Modul 306900 - Programmierung, Tooling & Agentische KI
**Instructor:** Dr. Benjamin Schwendinger
