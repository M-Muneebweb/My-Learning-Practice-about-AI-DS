res_dict = {}
Result = None
Grade = None
per = None
main_dict = {}
print("""
              <<<<-----Let calculate result----->>>>


        """)
Sub_tot = eval(input("Please enter Total Subjects range:    "))
maxmarks = int(input("Enter Max Marks of one Subject:   "))
passmarks =  int(input("Enter Passing Marks Criteria:   "))
for i in range(1,int(Sub_tot+1)):
  name_sub = input(f"Enter Subject {i} Name:   ")
  marks_sub = int(input(f"Enter your {name_sub} Marks:   "))
  main_dict[name_sub] = int(marks_sub)


  #Seperate Result Calculate all Subject.
  if marks_sub > passmarks:
    Result = "Pass"
    res_dict[name_sub] = Result
  else:
    Result = "Fail"
    res_dict[name_sub] = Result

  #Result Calculate
  if marks_sub >= passmarks:
    continue
  else:
    Result = "Fail"



total = sum(main_dict.values())


#percentage Calculate.
per =(total/(maxmarks*Sub_tot))*100

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


if Result == "Pass":
  Grade = "Pass"
else:
  Grade = "Fail"
#RESULT PRINT

print(f"""

------------------------------------------------------------------------------------
                                  
                                  YOUR RESULT
                            -----------------------
                            Total Marks:  {maxmarks*Sub_tot}
                            Obt Marks  :  {total}
                            Percentage :  {per:.2f}%
                            Grade      :  {Grade}
                            Result     :  {Result}

                            _______________________
                            Subjects   :  Pass/Fail
                              |              |
                              v              v
                            -----------------------""")

for b in main_dict:
  print(f"""                             {b}     :     {res_dict[b]}""")
print("""
                            _______________________
                            Subjects   :  Marks
                              |              |
                              v              v
                            -----------------------""")
    
for b in main_dict:
  print(f"""                            {b}     :     {main_dict[b]}""")

  