#from testing2 import *
import math

#### FUNCTIONS ####


# instructions
def show_instructions():
  print('''
------------------------- Instructions --------------------------
Choose two given values- either two sides or a side and an angle
note: two angles cannot solve the sides of the triangle

visual graph shown below:
- a, b, c are sides
- A, B are angles (in degrees)

   B
    |⟍
    |  ⟍
  b |    ⟍ c 
    |      ⟍
    |┐_ _ _ _⟍
        a      A
----------------------------------------------------------------
  ''')


# checks if user entered an integer to a given question
def num_check(question):
  while True:
    try:
      response = float(input(question))
      return response

    except ValueError:
      print("Please enter an number")


# checks that users enter a valid response (eg. yes / no) based on a list of options
def string_checker(question, num_responses, valid_responses):

  if num_responses == 2:
    error = "Please choose {} or {}".format(valid_responses[0],
                                            valid_responses[1])
  else:
    error = "Please choose {} or {} or {}".format(valid_responses[0],
                                                  valid_responses[1],
                                                  valid_responses[2])

  short_version = 1  # if num_letters == 1 else 2

  while True:
    response = (input(question).lower()).strip()

    for item in valid_responses:
      if response == item[:short_version] or response == item:
        return item

    print(error)

# 
def calculate_sides_angles(value):
 print(value)
    
  

#### MAIN ROUNTINE ####

# lists
yes_no_list = ["yes", "no"]
given_values_list = ["ts", "sa", "end", "x"]
sides_list = ["a", "b", "c"]
angles_list = ["a", "b"]
# ts stands for two sides, sa stands for side and angle

want_instructions = string_checker(
    "Do you want to read the instructions (y/n)? ", 2, yes_no_list)

if want_instructions == "yes":
  show_instructions()

# beginning of session
while True:
  chosen_values = string_checker(
      '''TS - two sides
SA - side and angle

(enter “end” to quit session)
Are you given two sides or a side and angle? (TS/SA): ''', 2,
      given_values_list)

  # values
  if chosen_values == "end" or chosen_values == "x":
    break

  # Given two sides
  elif chosen_values == "ts":
    missing_side = string_checker(
      "What side are you missing? (A/B/C): ", 3, sides_list)

    if missing_side == "a":
      b = num_check("Give side b: ")
      c = num_check("Give side c: ")
      a = math.sqrt(c ** 2 - b ** 2)
      angle_B = math.degrees(math.asin(b / c))
      angle_A = 90 - angle_B
      print(a)
      print(angle_A)
      print(angle_B)
      
    elif missing_side == "b":
      a = num_check("Give side a: ")
      c = num_check("Give side c: ")
      b = math.sqrt(c ** 2 - a ** 2)
      angle_B = math.degrees(math.acos(a / c))
      angle_A = 90 - angle_B
      print(b)
      print(angle_A)
      print(angle_B)
    
    else:
      a = num_check("Give side a: ")
      b = num_check("Give side b: ")
      c = math.sqrt(a ** 2 + b ** 2)
      angle_A = math.degrees(math.atan(a / b))
      angle_B = 90 - angle_A
      print(c)
      print(angle_A)
      print(angle_B)

  # Given a side and an angle
  else:
    known_side = string_checker(
      "What side do you have? (A/B/C): ", 3, sides_list)
    side = num_check(f"Give side {known_side}: ")

    known_angle = string_checker(
      "What angle do you have? (A/B): ", 2, angles_list)
    angle = num_check(f"Give angle {known_angle}: ")



print("Session ended")
