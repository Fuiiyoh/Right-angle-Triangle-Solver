import math

#### FUNCTIONS ####

# text styles
bold = '\033[1m'
italic = '\033[3m'
end = '\033[0m'  # aka normalize

# text colour
red = '\033[31m'

# instructions
def show_instructions():
  print(f'''
{bold + "---------------------- Instructions ------------------------" + end}
- Select either two sides or a side and an angle

{italic + "For two sides:" + end} 
- Give the missing side 
- Give the known sides values

{italic + "For a side and an angle:" + end}
- Give the known side and it's value
- Give the known angle and it's value

{italic + "NOTE:" + end}
- Two angles cannot solve the sides of the triangle
- Side c cannot be less than sides a and b
- Decimals are rounded to 2 decimal places
- Angles must be inbetween 0 and 90 degrees

{italic + "Visual graph shown below:" + end}
- a, b, c are sides
- A, B are angles (in degrees)

   A
    |⟍
    |  ⟍
  b |    ⟍ c 
    |      ⟍
    |┐_ _ _ _⟍
        a      B
{bold + "-------------------------------------------------------------" + end}'''
        )


# checks if user entered an integer to a given question
def num_check(question, rule):
  while True:
    try:
      response = round(float(input(question)), 2)
      # this rule is to deny inputs 0 and less
      if rule == 0:
        if response > 0:
          pass
        # error message
        else:
          print(red + "Please enter an number greater than 0" + end)
          continue
      # this rule is specifically for the angles (they must be kept inbetween 0 and 90)
      else:
        if 0 < response < 90:
          pass
        # error message
        else:
          print(red + "Angle must be between 0 and 90 degrees" + end)
          continue
      return response

    except ValueError:
      print(red + "Please enter an number" + end)


# checks that users enter a valid response (eg. yes / no) based on a list of options
def string_checker(question, num_responses, valid_responses):

  # to include more responses in the errors
  if num_responses == 2:
    error = "Please choose {} or {}".format(valid_responses[0],
                                            valid_responses[1])
  else:
    error = "Please choose {} or {} or {}".format(valid_responses[0],
                                                  valid_responses[1],
                                                  valid_responses[2])

  short_version = 1

  while True:
    response = (input(question).lower()).strip()

    for item in valid_responses:
      if response == item[:short_version] or response == item:
        return item

    print(red + error + end)


#### MAIN ROUNTINE ####

# lists
yes_no_list = ["yes", "no"]
select_list = ["1", "2", "end"]
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

# ask for instructions
want_instructions = string_checker(
    "Do you want to read the instructions (y/n)? ", 2, yes_no_list)

if want_instructions == "yes":
  show_instructions()

# beginning of session
while True:
  chosen_values = string_checker(
      f''' 
[1] - two sides
[2] - a side and an angle
{italic + "(enter “end” to quit session)" + end}

What do you want to solve with? (1/2): ''', 2, select_list)

  # exit code to conclude session
  if chosen_values == "end":
    break

  #### GIVEN TWO SIDES ####
  elif chosen_values == "1":
    missing_side = string_checker("What side are you missing? (A/B/C): ", 3,
                                  sides_list)

    # missing side a
    if missing_side == "a":
      b = num_check("Give side b: ", 0)
      # loop side c until given a value greater than b
      while True:
        c = num_check("Give side c: ", 0)
        if b < c:
          break
        else:
          print(red + "Side c must be greater than side b" + end)
          continue
      # calculations
      a = round(math.sqrt(c**2 - b**2), 2)
      angle_A = round(math.degrees(math.asin(b / c)), 2)

    # missing side b
    elif missing_side == "b":
      a = num_check("Give side a: ", 0)
      # loop side c until given a value greater than a
      while True:
        c = num_check("Give side c: ", 0)
        if a < c:
          break
        else:
          print(red + "Side c must be greater than side a" + end)
      # calculations
      b = round(math.sqrt(c**2 - a**2), 2)
      angle_A = round(math.degrees(math.acos(a / c)), 2)

    # missing side c
    else:
      a = num_check("Give side a: ", 0)
      b = num_check("Give side b: ", 0)
      # calculations
      c = round(math.sqrt(a**2 + b**2), 2)
      angle_A = round(math.degrees(math.atan(a / b)), 2)

    # calculation for angle B
    angle_B = round(90 - angle_A, 2)

  #### GIVEN A SIDE AND AN ANGLE ####
  else:
    known_side = string_checker("What side do you have? (A/B/C): ", 3,
                                sides_list)
    side = num_check(f"Give side {known_side}: ", 0)

    known_angle = string_checker("What angle do you have? (A/B): ", 2,
                                 angles_list)
    angle = num_check(f"Give angle {known_angle.upper()}: ", 1)

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
        c = round(side / math.cos(math.radians(angle)), 2)

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
  history.append((f'''
   Side a:  {a}
   Side b:  {b}
   Side c:  {c}
   Angle A: {angle_A}
   Angle B: {angle_B}
  '''))

  # Print results
  print(f'''
{bold + "----- RESULTS -----" + end}
Side a:  {a}
Side b:  {b}
Side c:  {c}
Angle A: {angle_A}
Angle B: {angle_B}
{bold + "-------------------" + end}''')

print(bold + "\n---- CALCULATION HISTORY ----" + end)
for index, entry in enumerate(history, start=1):
  print(f"{index}) {entry}")
print(bold + "------ END OF SESSION -------" + end)