#### FUNCTIONS ####

def show_instructions():
  print('''
------------------------ Instructions -------------------------


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
  -------------------------------------------------------------
  ''')

def string_checker(question, num_letters, valid_responses):

  error = "Please choose {} or {}".format(valid_responses[0],
                                          valid_responses[1])

  short_version = 1 if num_letters == 1 else 2

  while True:
    response = input(question).lower()

    for item in valid_responses:
      if response == item[:short_version] or response == item:
        return item

    print(error)

#### MAIN ROUNTINE ####

# lists
yes_no_list = ["yes", "no"]

want_instructions = string_checker(
  "Do you want to read the instructions (y/n)? ", 1, yes_no_list)

if want_instructions == "yes":
  show_instructions()