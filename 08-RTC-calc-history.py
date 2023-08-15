#from testing2 import *
import math

#### FUNCTIONS ####


# instructions
def show_instructions():
  print('''
------------------------- Instructions --------------------------
- Choose two given values- either two sides or a side and an angle
- Side c cannot be less than sides a and b
- Angle must be inbetween 0 and 90 degrees

note: two angles cannot solve the sides of the triangle

visual graph shown below:
- a, b, c are sides
- A, B are angles (in degrees)

   A
    |⟍
    |  ⟍
  b |    ⟍ c 
    |      ⟍
    |┐_ _ _ _⟍
        a      B
----------------------------------------------------------------
  ''')


# checks if user entered an integer to a given question
def num_check(question, rule):
  while True:
    try:
      response = float(input(question))
      if rule == 0:
        if response > 0:
          pass
        else:
          print("Please enter an number greater than 0")
          continue
      else:
        if 0 < response < 90:
          pass
        else:
          print("Angle must be between 0 and 90 degrees")
          continue
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


#### MAIN ROUNTINE ####

# lists
yes_no_list = ["yes", "no"]
select_list = ["1", "2", "end", "x"]
sides_list = ["a", "b", "c"]
angles_list = ["a", "b"]

# sides and angles
a = 0
b = 0
c = 0
angle_A = 0
angle_B = 0

history = []

# ts stands for two sides, sa stands for side and angle

want_instructions = string_checker(
    "Do you want to read the instructions (y/n)? ", 2, yes_no_list)

if want_instructions == "yes":
  show_instructions()

# beginning of session
while True:
  chosen_values = string_checker(
      ''' 
[1] - two sides
[2] - a side and an angle
(enter “end” to quit session)

What do you want to solve using? (1/2): ''', 2,
      select_list)

  # values
  if chosen_values == "end" or chosen_values == "x":
    break

  # Given two sides
  elif chosen_values == "ts":
    missing_side = string_checker("What side are you missing? (A/B/C): ", 3,
                                  sides_list)

    if missing_side == "a":
      b = num_check("Give side b: ", 0)
      
      # loop side c until given a value greater than b
      while True:
        c = num_check("Give side c: ", 0)
        if b < c:
          break
        else:
          print("Side c must be greater than side b")
          continue

      a = math.sqrt(c**2 - b**2)
      angle_A = math.degrees(math.asin(b / c))

    elif missing_side == "b":
      a = num_check("Give side a: ", 0)
      
      # loop side c until given a value greater than a
      while True:
        c = num_check("Give side c: ", 0)
        if a < c:
          break
        else:
          print("Side c must be greater than side a")
      
      b = math.sqrt(c**2 - a**2)
      angle_A = math.degrees(math.acos(a / c))

    else:
      a = num_check("Give side a: ", 0)
      b = num_check("Give side b: ", 0)
      
      c = math.sqrt(a**2 + b**2)
      angle_A = math.degrees(math.atan(a / b))

    angle_B = 90 - angle_A

  # Given a side and an angle
  else:
    known_side = string_checker("What side do you have? (A/B/C): ", 3,
                                sides_list)
    side = num_check(f"Give side {known_side}: ", 0)

    known_angle = string_checker("What angle do you have? (A/B): ", 2,
                                 angles_list)
    angle = num_check(f"Give angle {known_angle.upper()}: ", 1)

    if 0 < angle < 90:
      pass
    else:
      print(f"Angle {known_angle.upper()} must be between 0 and 90 degrees")
      continue

    # angle A calculations
    if known_angle == "a":
      if known_side == "a":
        a = side
        b = side / math.tan(math.radians(angle))
        c = side / math.sin(math.radians(angle))

      elif known_side == "b":
        a = side * math.tan(math.radians(angle))
        b = side
        c = side / math.cos(math.radians(angle))

      else:
        a = side * math.sin(math.radians(angle))
        b = side * math.cos(math.radians(angle))
        c = side
        
      angle_A = angle
      angle_B = 90 - angle

    # angle B calculations
    else:
      if known_side == "a":
        a = side
        b = side * math.tan(math.radians(angle))
        c = side / math.cos(math.radians(angle))

      elif known_side == "b":
        a = side / math.tan(math.radians(angle))
        b = side
        c = side / math.sin(math.radians(angle))

      else:
        a = side * math.cos(math.radians(angle))
        b = side * math.sin(math.radians(angle))
        c = side

      angle_A = 90 - angle
      angle_B = angle

  # Store calculation history
  history.append((a, b, c, angle_A, angle_B))

  # Print results
  print("------------- RESULTS -------------")
  print(f"Side a: {round(a, 2)}")
  print(f"Side b: {round(b, 2)}")
  print(f"Side c: {round(c, 2)}")
  print(f"Angle A: {round(angle_A, 2)}")
  print(f"Angle B: {round(angle_B, 2)}")

print("Session ended")
for index, entry in enumerate(history, start = 1):
  print(f"{index}. {entry}")
