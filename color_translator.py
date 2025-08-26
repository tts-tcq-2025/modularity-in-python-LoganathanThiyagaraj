# color_translator.py

# CORRECTED IMPORT: No 'color_coder' prefix needed when in the same directory
from constants import MAJOR_COLORS, MINOR_COLORS

def color_pair_to_string(major_color, minor_color):
  """
  Formats a major and minor color into a string.
  """
  return f'{major_color} {minor_color}'


def get_color_from_pair_number(pair_number):
  """
  Translates a pair number (1-25) to its corresponding major and minor color names.
  Raises an Exception if the pair number results in an out-of-range index.
  """
  zero_based_pair_number = pair_number - 1
  major_index = zero_based_pair_number // len(MINOR_COLORS)
  if major_index >= len(MAJOR_COLORS):
    raise Exception(f'Major index {major_index} out of range for pair number {pair_number}')
  
  minor_index = zero_based_pair_number % len(MINOR_COLORS)
  if minor_index >= len(MINOR_COLORS): # This check is technically redundant if major_index is valid and MINOR_COLORS is fixed
    raise Exception(f'Minor index {minor_index} out of range for pair number {pair_number}')
  
  return MAJOR_COLORS[major_index], MINOR_COLORS[minor_index]


def get_pair_number_from_color(major_color, minor_color):
  """
  Translates a major and minor color name to its corresponding pair number.
  Raises an Exception if the color name is not found.
  """
  try:
    major_index = MAJOR_COLORS.index(major_color)
  except ValueError:
    raise Exception(f'Major color "{major_color}" not found in list.')
  
  try:
    minor_index = MINOR_COLORS.index(minor_color)
  except ValueError:
    raise Exception(f'Minor color "{minor_color}" not found in list.')
  
  return major_index * len(MINOR_COLORS) + minor_index + 1
