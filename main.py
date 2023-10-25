# This is a case conversion tool, made by Beavermon 2023.
  print(
      "\nThis is a customizable tool to convert whatever text you want into either upper or lower case. "
  )
  var1 = "lower"
  var2 = "upper"
  var3 = 0
  var4 = int(input("\nHow many pieces of text do you want to convert?: "))
  
  while var3 < var4:
    user_text = input(
        "\nThis is a tool to convert your text into either upper or lowercase.\n\nPaste your text here: "
    )
    type_of_case = input(
        "\nTo select which case you want to convert your text to, please type,\n\nlower or upper: "
    )
    if type_of_case == var1:
      print(user_text.lower())
    elif type_of_case == var2:
      print(user_text.upper())
    elif type_of_case != var1 or var2:
      print("Problem detected, please try again!")
    var3 += 1
    break
  print("\nThanks for using this tool!")
