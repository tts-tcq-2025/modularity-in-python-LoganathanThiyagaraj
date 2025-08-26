
from color_translator import get_color_from_pair_number, get_pair_number_from_color, color_pair_to_string
from color_manual import print_color_code_manual
from tests import run_all_tests # Import the function to run tests

def main():
  """
  Main function to demonstrate the color coding functionalities.
  """
  print("Welcome to the 25-Pair Color Coder!\n")

  # Option to run tests if desired, maybe controlled by an argument or flag
  run_all_tests() # Call the function from tests.py

  print("\n--- Generating and Printing Reference Manual ---")
  print_color_code_manual()
  print("\nManual Generation Complete!")

  print("\n--- Demonstrating direct usage ---")
  try:
      major, minor = get_color_from_pair_number(1)
      print(f"Pair 1 is: {color_pair_to_string(major, minor)}")
      pair = get_pair_number_from_color("Yellow", "Green")
      print(f"Yellow Green is pair: {pair}")
  except Exception as e:
      print(f"An error occurred: {e}")


if __name__ == '__main__':
  main()
