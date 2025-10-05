"""
Pricing data for different AI models.
Prices are per 1,000 tokens (as of January 2025).
"""

# Model pricing in USD per 1,000 tokens
MODELS = {
    "gpt4": {
        "name": "GPT-4",
        "input_price": 0.03,
        "output_price": 0.06,
    },
    "gpt4-turbo": {
        "name": "GPT-4 Turbo",
        "input_price": 0.01,
        "output_price": 0.03,
    },
    "gpt35": {
        "name": "GPT-3.5 Turbo",
        "input_price": 0.0015,
        "output_price": 0.002,
    },
    "claude-sonnet": {
        "name": "Claude 3.5 Sonnet",
        "input_price": 0.003,
        "output_price": 0.015,
    },
    "claude-haiku": {
        "name": "Claude 3 Haiku",
        "input_price": 0.00025,
        "output_price": 0.00125,
    },
    "claude-opus": {
        "name": "Claude 3 Opus",
        "input_price": 0.015,
        "output_price": 0.075,
    },
}


def get_model_info(model_key: str) -> dict:
    """
    Get pricing information for a specific model.

    Args:
        model_key: Model identifier (e.g., 'gpt4', 'claude-sonnet')

    Returns:
        Dictionary with model name and pricing info

    Raises:
        ValueError: If model_key is not found
    """
    if model_key not in MODELS:
        available = ", ".join(MODELS.keys())
        raise ValueError(f"Model '{model_key}' not found. Available: {available}")

    return MODELS[model_key]


def list_available_models() -> list[str]:
    """Return list of available model keys."""
    return list(MODELS.keys())
