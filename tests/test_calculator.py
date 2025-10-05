"""
Tests for cost calculator functionality.
"""

import pytest
from cost_calculator import calculate_cost, count_tokens, format_result
from models import get_model_info


def test_calculate_cost_gpt4():
    """Test cost calculation for GPT-4."""
    result = calculate_cost("gpt4", input_tokens=1000, output_tokens=500)

    assert result["model"] == "GPT-4"
    assert result["input_tokens"] == 1000
    assert result["output_tokens"] == 500
    assert result["total_tokens"] == 1500
    assert result["input_cost"] == 0.03  # 1000 tokens * $0.03/1K
    assert result["output_cost"] == 0.03  # 500 tokens * $0.06/1K
    assert result["total_cost"] == 0.06


def test_calculate_cost_claude_haiku():
    """Test cost calculation for Claude Haiku (cheapest model)."""
    result = calculate_cost("claude-haiku", input_tokens=2000, output_tokens=1000)

    assert result["model"] == "Claude 3 Haiku"
    assert result["input_cost"] == 0.0005  # 2000 * $0.00025/1K
    assert result["output_cost"] == 0.00125  # 1000 * $0.00125/1K
    assert result["total_cost"] == 0.00175


def test_calculate_cost_invalid_model():
    """Test that invalid model raises ValueError."""
    with pytest.raises(ValueError, match="Model 'invalid' not found"):
        calculate_cost("invalid", 1000, 500)


def test_count_tokens():
    """Test token counting functionality."""
    text = "Hello, how are you doing today?"
    tokens = count_tokens(text)

    # Should return a positive integer
    assert isinstance(tokens, int)
    assert tokens > 0
    # This specific text should be around 8-10 tokens
    assert 5 < tokens < 15


def test_count_tokens_empty():
    """Test token counting with empty string."""
    tokens = count_tokens("")
    assert tokens == 0


def test_format_result():
    """Test result formatting."""
    result = {
        "model": "GPT-4",
        "input_tokens": 1000,
        "output_tokens": 500,
        "total_tokens": 1500,
        "input_cost": 0.03,
        "output_cost": 0.03,
        "total_cost": 0.06,
    }

    formatted = format_result(result)

    assert "GPT-4" in formatted
    assert "1,000" in formatted
    assert "500" in formatted
    assert "$0.060000" in formatted


def test_get_model_info():
    """Test model info retrieval."""
    info = get_model_info("gpt4")

    assert info["name"] == "GPT-4"
    assert info["input_price"] == 0.03
    assert info["output_price"] == 0.06


def test_zero_tokens():
    """Test calculation with zero tokens."""
    result = calculate_cost("gpt35", 0, 0)

    assert result["total_cost"] == 0.0
    assert result["input_cost"] == 0.0
    assert result["output_cost"] == 0.0
