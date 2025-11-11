#Get Output For User.
maxmarks = int(input("Enter Max Marks: "))
passmarks =  int(input("Enter Passing Marks Criteria: "))
maths = int(input("Enter your Maths marks: "))
computer = int(input("Enter your Computer marks: "))
english = int(input("Enter your English marks: "))
islamiat = int(input("Enter your Islamiat marks: "))
urdu = int(input("Enter your Urdu marks: "))
science = int(input("Enter your Science marks: "))
sst = int(input("Enter your S.ST marks: "))
total = maths+english+islamiat+urdu+science+sst+computer
Result = None
Grade = None
per = None



#Result Calculate
if maths > passmarks:
    if english > passmarks:
        if islamiat > passmarks:
            if urdu > passmarks:
                if science > passmarks:
                    if sst > passmarks:
                        if computer > passmarks:
                          Result = "Pass"
                        else:
                          Result = "Fail"
                    else:
                        Result = "Fail"
                else:
                    Result = "Fail"
            else:
                Result = "Fail"
        else:
            Result = "Fail"
    else:
        Result = "Fail"
else:
  Result = "Fail"


#percentage Calculate.
per =(total/(maxmarks*7))*100


#grade Calculate.
if per >= 90:
  Grade = "A"
elif per >= 80:
  Grade = "B"
elif per >= 70:
  Grade = "C"
elif per >= 60:
  Grade = "D"
elif per >= 50:
  Grade = "E"
elif per < 50:
  Grade = "F"


#Seperate Result Calculate all Subject.
engresult = None
computerresult = None
islamresult = None
mathresult = None
sciresult = None
sstresult = None
urduresult = None
if maths >= passmarks:
    mathresult = "Pass"
else:
    mathresult = "Fail"
if english >= passmarks:
    engresult = "Pass"
else:
    engresult = "Fail"
if islamiat >= passmarks:
    islamresult = "Pass"
else:
    islamresult = "Fail"
if science >= passmarks:
    sciresult = "Pass"
else:
    sciresult = "Fail"
if urdu >= passmarks:
    urduresult = "Pass"
else:
    urduresult = "Fail"
if sst >= passmarks:
    sstresult = "Pass"
else:
    sstresult = "Fail"
if computer >= passmarks:
    computerresult = "Pass"
else:
    computerresult = "Fail"

#Error Handling.
if maths <= maxmarks:
    if english <= maxmarks:
        if islamiat <= maxmarks:
            if urdu <= maxmarks:
                if science <= maxmarks:
                    if sst <= maxmarks:
                      if computer <= maxmarks:
                        print(f"""

--------------------------------------------------------------------------------------


                                Your Result
                          ------------------------
                          Total Marks:  {maxmarks*6}
                          Obt Marks  :  {total}
                          Percentage :  {per:.2f}%
                          Grade      :  {Grade}
                          Result     :  {Result}
                          _______________________
                          Subjects   :  Pass/Fail
                            |              |
                            v              v
                          -----------------------
                          English    :  {engresult}
                          Islamiat   :  {islamresult}
                          Math       :  {mathresult}
                          Science    :  {sciresult}
                          S.ST       :  {sstresult}
                          Urdu       :  {urduresult}""")
                      else:
                        print("Your Entered marks is greater than max Marks. Please enter correct Marks.")
                    else:
                        print("Your Entered marks is greater than max Marks. Please enter correct Marks.")
                else:
                    print("Your Entered marks is greater than max Marks. Please enter correct Marks.")
            else:
                print("Your Entered marks is greater than max Marks. Please enter correct Marks.")
        else:
            print("Your Entered marks is greater than max Marks. Please enter correct Marks.")
    else:
        print("Your Entered marks is greater than max Marks. Please enter correct Marks.")
else:
  print("Your Entered marks is greater than max Marks. Please enter correct Marks.")
