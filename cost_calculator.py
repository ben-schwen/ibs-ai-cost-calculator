"""
AI Prompt Cost Calculator

Calculate API costs for different LLM providers.
"""

import argparse
import tiktoken
from models import get_model_info, list_available_models
from export import export_to_csv


def count_tokens(text: str, model: str = "gpt-4") -> int:
    """
    Count tokens in a text string using tiktoken.

    Args:
        text: Input text to count tokens
        model: Model name for tokenizer (default: gpt-4)

    Returns:
        Number of tokens in the text as integer
    """
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        # Fallback to cl100k_base for Claude and unknown models
        encoding = tiktoken.get_encoding("cl100k_base")

    return len(encoding.encode(text))


def calculate_cost(model_key: str, input_tokens: int, output_tokens: int) -> dict:
    """
    Calculate the cost for a given model and token counts.

    Args:
        model_key: Model identifier (e.g., 'gpt4', 'claude-sonnet', etc.)
        input_tokens: Number of input tokens
        output_tokens: Number of output tokens

    Returns:
        Dictionary with cost breakdown
    """
    model_info = get_model_info(model_key)

    # Calculate costs (prices are per 1,000 tokens)
    input_cost = (input_tokens / 1000) * model_info["input_price"]
    output_cost = (output_tokens / 1000) * model_info["output_price"]
    total_cost = input_cost + output_cost

    return {
        "model": model_info["name"],
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "total_tokens": input_tokens + output_tokens,
        "input_cost": round(input_cost, 6),
        "output_cost": round(output_cost, 6),
        "total_cost": round(total_cost, 6),
    }


def format_result(result: dict) -> str:
    """Format calculation result as a readable string."""
    return f"""
{'='*50}
Model: {result['model']}
{'='*50}
Input tokens:  {result['input_tokens']:,} (${result['input_cost']:.6f})
Output tokens: {result['output_tokens']:,} (${result['output_cost']:.6f})
Total tokens:  {result['total_tokens']:,}
{'='*50}
TOTAL COST: ${result['total_cost']:.6f}
{'='*50}
"""


def main():
    """Main CLI interface."""
    parser = argparse.ArgumentParser(
        description="Calculate AI API costs for different models"
    )
    parser.add_argument(
        "--model",
        required=True,
        choices=list_available_models(),
        help="AI model to calculate costs for",
    )
    parser.add_argument("--input-tokens", type=int, help="Number of input tokens")
    parser.add_argument("--output-tokens", type=int, help="Number of output tokens")
    parser.add_argument(
        "--input-text", type=str, help="Text to count input tokens from"
    )
    parser.add_argument(
        "--output-text", type=str, help="Text to count output tokens from"
    )
    parser.add_argument("--export", type=str, help="Export results to CSV file")

    args = parser.parse_args()

    # Determine token counts
    if args.input_text:
        input_tokens = count_tokens(args.input_text)
    elif args.input_tokens:
        input_tokens = args.input_tokens
    else:
        parser.error("Either --input-tokens or --input-text must be provided")

    if args.output_text:
        output_tokens = count_tokens(args.output_text)
    elif args.output_tokens:
        output_tokens = args.output_tokens
    else:
        parser.error("Either --output-tokens or --output-text must be provided")

    # Calculate costs
    result = calculate_cost(args.model, input_tokens, output_tokens)

    # Display results
    print(format_result(result))

    # Export if requested
    if args.export:
        export_to_csv([result], args.export)
        print(f"✅ Results exported to {args.export}")


if __name__ == "__main__":
    main()
