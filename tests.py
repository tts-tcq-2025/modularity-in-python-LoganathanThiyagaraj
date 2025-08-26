
from color_translator import get_color_from_pair_number, get_pair_number_from_color, color_pair_to_string

def test_number_to_pair(pair_number, expected_major_color, expected_minor_color):
  """
  Tests the get_color_from_pair_number function.
  """
  major_color, minor_color = get_color_from_pair_number(pair_number)
  assert(major_color == expected_major_color), f"Expected major {expected_major_color}, Got {major_color} for pair {pair_number}"
  assert(minor_color == expected_minor_color), f"Expected minor {expected_minor_color}, Got {minor_color} for pair {pair_number}"
  print(f"✅ {pair_number}: {color_pair_to_string(major_color, minor_color)} (OK)")


def test_pair_to_number(major_color, minor_color, expected_pair_number):
  """
  Tests the get_pair_number_from_color function.
  """
  pair_number = get_pair_number_from_color(major_color, minor_color)
  assert(pair_number == expected_pair_number), f"Expected pair {expected_pair_number}, Got {pair_number} for {major_color} {minor_color}"
  print(f"✅ {major_color} {minor_color}: {pair_number} (OK)")

def run_all_tests():
  """
  Executes all defined tests for the color code translation.
  """
  print("--- Running Translation Tests ---")
  test_number_to_pair(4, 'White', 'Brown')
  test_number_to_pair(5, 'White', 'Slate')
  test_pair_to_number('Black', 'Orange', 12)
  test_pair_to_number('Violet', 'Slate', 25)
  test_pair_to_number('Red', 'Orange', 7)
  print('Translation Tests Done :)')

# Optional: You can run tests directly from this file for quick checks
if __name__ == "__main__":
    run_all_tests()
