#### FUNCTIONS ####

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
given_values_list = ["ts", "sa", "xxx"]

# beginning of session
while True:
  given_values = string_checker(
    '''TS - two sides
SA - side and angle
xxx - quit session

Choose the given values (TS/SA): ''', 1, given_values_list)

  # values
  if given_values == "xxx":
    break
  elif given_values == "ts":
    print("ts")
    continue
  else:
    print("sa")
    continue

print("Exited")
  