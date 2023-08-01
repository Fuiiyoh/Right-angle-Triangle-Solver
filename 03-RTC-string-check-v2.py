#from testing import *
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
      response = int(input(question))
      return response

    except ValueError:
      print("Please enter an integer.")

# checks that users enter a valid response (eg. yes / no) based on a list of options
def string_checker(question, num_responses, valid_responses):

  if num_responses == 2:
    error = "Please choose {} or {}".format(valid_responses[0],
                                            valid_responses[1])
  else:
    error = "Please choose {} or {} or {}".format(valid_responses[0],
                                                  valid_responses[1],
                                                  valid_responses[2])

  short_version = 1 # if num_letters == 1 else 2

  while True:
    response = (input(question).lower()).strip()
    

    for item in valid_responses:
      if response == item[:short_version] or response == item:
        return item

    print(error)


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
  choose_values = string_checker(
    '''TS - two sides
SA - side and angle
(enter “end” to quit session)

Are you given two sides or a side and angle? (TS/SA): ''', 2, given_values_list)

  # values
  if choose_values == "end" or choose_values =="x":
    break
  elif choose_values == "ts":
    choose_ts = string_checker(
      "What is the first side? (A/B/C): ", 3, sides_list)
    continue
  else:
    choose_sa = string_checker(
      "What is the side? (A/B/C): ", 3, sides_list)
    continue

print("Session ended")
  