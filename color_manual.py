
from color_translator import get_color_from_pair_number

def generate_color_code_manual_text():
    """
    Generates a formatted string representing the 25-pair color code manual.
    """
    manual_lines = ["25-Pair Color Code Reference Manual\n"]
    manual_lines.append("{:<5} {:<15} {:<15}".format("Pair #", "Major Color", "Minor Color"))
    manual_lines.append("-" * 35)

    for pair_number in range(1, 26):
        try:
            major_color, minor_color = get_color_from_pair_number(pair_number)
            manual_lines.append("{:<5} {:<15} {:<15}".format(pair_number, major_color, minor_color))
        except Exception as e:
            manual_lines.append(f"{pair_number:<5} Error: {e}")

    return "\n".join(manual_lines)

def print_color_code_manual():
    """
    Prints the 25-pair color code manual to the console.
    """
    print(generate_color_code_manual_text())

# Self-test block (can be removed if not needed for direct execution of this file)
if __name__ == "__main__":
    print("--- Generating and Printing Color Code Manual (from color_manual.py) ---")
    print_color_code_manual()
