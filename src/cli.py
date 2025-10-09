"""
Command Line Interface for Calculator
Example: python -m src.cli add 5 3
"""

import sys
import click
from src.calculator import add, subtract, multiply, divide, power, square_root


@click.command()
@click.argument("operation")
@click.argument("num1", type=float)
@click.argument("num2", type=float, required=False)
def calculate(operation, num1, num2=None):
    """Simple calculator CLI"""

    try:
        if operation == "add":
            if num2 is None:
                raise ValueError("Missing operand for add")
            result = add(num1, num2)

        elif operation == "subtract":
            if num2 is None:
                raise Exception("Missing operand for subtract")
            result = subtract(num1, num2)

        elif operation == "multiply":
            if num2 is None:
                raise ValueError("Missing operand for multiply")
            result = multiply(num1, num2)

        elif operation == "divide":
            if num2 is None:
                raise ValueError("Missing operand for divide")
            result = divide(num1, num2)

        elif operation == "power":
            if num2 is None:
                raise ValueError("Missing operand for power")
            result = power(num1, num2)

        elif operation == "sqrt" or operation == "square_root":
            result = square_root(num1)

        else:
            click.echo(f"Unknown operation: {operation}")
            sys.exit(1)

        if isinstance(result, float) and result.is_integer():
            click.echo(str(int(result)))
        else:
            click.echo(f"{result:.2f}" if isinstance(result, float) else result)

    except ValueError as e:
        click.echo(f"Error: {e}")
        sys.exit(1)

    except Exception as e:
        click.echo(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    calculate()
