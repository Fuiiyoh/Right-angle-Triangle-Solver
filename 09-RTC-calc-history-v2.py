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
      response = round(float(input(question)), 2)
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

# list to hold calculation history
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
  elif chosen_values == "1":
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

      a = round(math.sqrt(c**2 - b**2), 2)
      angle_A = round(math.degrees(math.asin(b / c)), 2)

    elif missing_side == "b":
      a = num_check("Give side a: ", 0)
      
      # loop side c until given a value greater than a
      while True:
        c = num_check("Give side c: ", 0)
        if a < c:
          break
        else:
          print("Side c must be greater than side a")
      
      b = round(math.sqrt(c**2 - a**2), 2)
      angle_A = round(math.degrees(math.acos(a / c)), 2)

    else:
      a = num_check("Give side a: ", 0)
      b = num_check("Give side b: ", 0)
      
      c = round(math.sqrt(a**2 + b**2), 2)
      angle_A = round(math.degrees(math.atan(a / b)), 2)

    angle_B = round(90 - angle_A, 2)

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
        b = round(side / math.tan(math.radians(angle)), 2)
        c = round(side / math.sin(math.radians(angle)), 2)

      elif known_side == "b":
        a = round(side * math.tan(math.radians(angle)), 2)
        b = side
        c = round(side / math.cos(math.radians(angle)), 2)

      else:
        a = round(side * math.sin(math.radians(angle)), 2)
        b = round(side * math.cos(math.radians(angle)), 2)
        c = side
        
      angle_A = angle
      angle_B = round(90 - angle, 2)

    # angle B calculations
    else:
      if known_side == "a":
        a = side
        b = round(side * math.tan(math.radians(angle)), 2)
        c = side / math.cos(math.radians(angle))

      elif known_side == "b":
        a = round(side / math.tan(math.radians(angle)), 2)
        b = side
        c = round(side / math.sin(math.radians(angle)), 2)

      else:
        a = round(side * math.cos(math.radians(angle)), 2)
        b = round(side * math.sin(math.radians(angle)), 2)
        c = side

      angle_A = round(90 - angle, 2)
      angle_B = angle

  # Store calculation history
  history.append((f'''side a: {a}
   Side b: {b}
   Side c: {c}
   Angle A: {angle_A}
   Angle B: {angle_B}
  '''))

  # Print results
  print("------------- RESULTS -------------")
  print(f"Side a: {a}")
  print(f"Side b: {b}")
  print(f"Side c: {c}")
  print(f"Angle A: {angle_A}")
  print(f"Angle B: {angle_B}")

print("\n------------- CALCULATION HISTORY -------------\n")
for index, entry in enumerate(history, start = 1):
  print(f"{index}) {entry}")

