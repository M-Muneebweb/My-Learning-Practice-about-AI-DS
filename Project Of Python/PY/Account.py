detail_dict = {}
i = 0
while True:
  print("""



          <<<<<<<--------Make account-------->>>>>>>""")
  while True:
    i += 1
    b=f"Name{i}"
    c=f"Address{i}"
    d=f"Phone{i}"
    e=f"Email{i}"
    f=f"Password{i}"
    g=f"Age{i}"
    h=f"Gender{i}"
    j=f"Qualification{i}"
    k=f"Country{i}"
    l=f"City{i}"


    choice = input("""

  1.Signup.
  2.Login.
  3.Exit.

  Choose: 1,2,3  :   """)
    if choice == "1":
      print("""



                <<<<<<----------SIGNUP---------->>>>>>""")
      email = input("Enter your email: ").lower()
      password = input("Enter your Password: ")
      name = input("Enter your name: ").capitalize()
      address = input("Enter your address: ")
      phone = input("Enter your phone number: ")
      age = input("Enter your age: ")
      gender = input("Enter your gender: ")
      qualification = input("Enter your qualification: ")
      country = input("Enter your country: ")
      city = input("Enter your city: ")
      detail_dict[b] = name
      detail_dict[c] = address
      detail_dict[d] = phone
      detail_dict[e] = email
      detail_dict[f] = password
      detail_dict[g] = age
      detail_dict[h] = gender
      detail_dict[j] = qualification
      detail_dict[k] = country
      detail_dict[l] = city
    elif choice == "2":
      print("""


                <<<<<<--------Login now-------->>>>>>

      """)
      user_email = input("Enter Email: ").lower()
      user_pass = input("Enter Password: ")
      if user_email in detail_dict.values():
        for num in range(1,i+1):
          em = f"Email{num}"
          pd = f"Password{num}"
          if em in detail_dict.keys():
            if user_email == detail_dict[em]:
              if user_pass == detail_dict[pd]:
                print("""



                    <<<<<-----WELCOME IN PROFILE---->>>>>

                    """)
                print(f"""  Name            :    {detail_dict[f"Name{num}"]}""")
                print(f"""  Address         :    {detail_dict[f"Address{num}"]}""")
                print(f"""  Phone           :    {detail_dict[f"Phone{num}"]}""")
                print(f"""  Email           :    {detail_dict[f"Email{num}"]}""")
                print(f"""  Password        :    {detail_dict[f"Password{num}"]}""")
                print(f"""  Age             :    {detail_dict[f"Age{num}"]}""")
                print(f"""  Gender          :    {detail_dict[f"Gender{num}"]}""")
                print(f"""  Qualification   :    {detail_dict[f"Qualification{num}"]}""")
                print(f"""  Country         :    {detail_dict[f"Country{num}"]}""")
                print(f"""  City            :    {detail_dict[f"City{num}"]}""")
                break
              else:
                print("Incorrect Password")
          else:
            continue
      else:
        print("""

            Sorry, looks like that’s the wrong email or password.

                    Please Signup""")
    elif choice == "3":
      print("""



             <<<<<<----------Thanks.---------->>>>>>""")
      break
    else:
      print("Invalid Input")
  break