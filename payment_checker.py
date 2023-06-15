# functions go here
def cash_credit(question):

  while True:
    response = input(question).lower()

    if response == "cash" or response == "ca":
      return "cash"

    elif response == "credit" or response == "cr":
      return "credit"

    else:
      print("Sorry that is not a valid payment method, please choose either cash (ca) or credit (cr).")
    
  