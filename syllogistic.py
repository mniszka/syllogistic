# sentences

premise_1 = "All woman are mother" #mothers
premise_2 = "All Anna is a woman"

#add: strip()
#to lower case
premise_1 = premise_1.lower()
premise_2 = premise_2.lower()

#split into a list
premise_1 = premise_1.split()
premise_2 = premise_2.split()

premise_1_first_element = premise_1[0]
premise_2_first_element = premise_2[0]

#check the type of a first sentence
#dodać sprawdzanie czy jest is/are
def check_the_type_of_a_first_premise():
	if premise_1_first_element == "all" or premise_1_first_element == "each" and "not" not in premise_1: return "PaS"
	elif premise_1_first_element == "no" or premise_1_first_element == "any": return "PeS"
	elif premise_1_first_element == "some": return "PiS"
	elif premise_1_first_element == "some" and "not" in premise_1: return "PoS"
	else: return "The first premise does not have a correct form"



#check the type of a second sentence
def check_the_type_of_a_second_premise():
	if premise_2_first_element == "all"  or premise_2_first_element == "each" and "not" not in premise_1: return "PaS"
	elif premise_2_first_element == "no" or premise_2_first_element == "any": return "PeS"
	elif premise_2_first_element == "some": return "PiS"
	elif premise_2_first_element == "some" and "not" in premise_2: return "PoS"
	else: return "The second premise does not have a correct form"


print(check_the_type_of_a_first_premise())
print(check_the_type_of_a_second_premise())


#checking conditions
def check_conditions():
  if check_the_type_of_a_first_premise() == "PoS" \
  		and check_the_type_of_a_second_premise() == "PoS": return False 
  if check_the_type_of_a_first_premise() == "PoS" \
  		and check_the_type_of_a_second_premise() == "PiS": return False 
  if check_the_type_of_a_first_premise() == "PiS" \
  		and check_the_type_of_a_second_premise() == "PiS": return False 
  if check_the_type_of_a_first_premise() == "PiS" \
  		and check_the_type_of_a_second_premise() == "PoS": return False
  if check_the_type_of_a_first_premise() == "PeS" \
  		and check_the_type_of_a_second_premise() == "PeS": return False 
  if check_the_type_of_a_first_premise() == "PoS" \
  		and check_the_type_of_a_second_premise() == "PoS": return False 
  if check_the_type_of_a_first_premise() == "PeS" \
  		and check_the_type_of_a_second_premise() == "PoS": return False 
  if check_the_type_of_a_first_premise() == "PoS" \
  		and check_the_type_of_a_second_premise() == "PeS": return False
  else: return True
print(check_conditions())

#checking which of five syllogistic figures is it
def check_the_figure():
  if premise_1[1] == premise_2[-1]: return "figure 1"
  if premise_1[-1] == premise_2[-1]: return "figure 2"
  if premise_1[1] == premise_2[1]: return "figure 3"
  if premise_1[-1] == premise_2[1]: return "figure 4"


#conditions
def inform_about_condition():
  if check_conditions() == False: print("the condition is not met")
  else: print(check_the_figure())

inform_about_condition()

#conclussion
def conclusion():
    if check_the_figure() == "figure 1" and check_the_type_of_a_first_premise() == "PaS" and check_the_type_of_a_second_premise() == "PaS": return "SaP"
    elif check_the_figure() == "figure 1" and check_the_type_of_a_first_premise() == "PeS" and check_the_type_of_a_second_premise() == "PaS": return "SeP"
    elif check_the_figure() == "figure 1" and check_the_type_of_a_first_premise() == "PaS" and check_the_type_of_a_second_premise() == "PiS": return "SiP"
    elif check_the_figure() == "figure 1" and check_the_type_of_a_first_premise() == "PeS" and check_the_type_of_a_second_premise() == "PiS": return "SoP"
    
    elif check_the_figure() == "figure 2" and check_the_type_of_a_first_premise() == "PeS" and check_the_type_of_a_second_premise() == "PaS": return "SeP"
    elif check_the_figure() == "figure 2" and check_the_type_of_a_first_premise() == "PaS" and check_the_type_of_a_second_premise() == "PeS": return "SeP"
    elif check_the_figure() == "figure 2" and check_the_type_of_a_first_premise() == "PeS" and check_the_type_of_a_second_premise() == "PiS": return "SoP"
    elif check_the_figure() == "figure 2" and check_the_type_of_a_first_premise() == "PaS" and check_the_type_of_a_second_premise() == "PoS": return "SoP"
    
    elif check_the_figure() == "figure 3" and check_the_type_of_a_first_premise() == "PaS" and check_the_type_of_a_second_premise() == "PaS": return "SiP"
    elif check_the_figure() == "figure 3" and check_the_type_of_a_first_premise() == "PiS" and check_the_type_of_a_second_premise() == "PaS": return "SiP"
    elif check_the_figure() == "figure 3" and check_the_type_of_a_first_premise() == "PaS" and check_the_type_of_a_second_premise() == "PiS": return "SiP"
    elif check_the_figure() == "figure 3" and check_the_type_of_a_first_premise() == "PeS" and check_the_type_of_a_second_premise() == "PaS": return "SoP"
    elif check_the_figure() == "figure 3" and check_the_type_of_a_first_premise() == "PoS" and check_the_type_of_a_second_premise() == "PaS": return "SoP"
    elif check_the_figure() == "figure 3" and check_the_type_of_a_first_premise() == "PeS" and check_the_type_of_a_second_premise() == "PiS": return "SoP"

    elif check_the_figure() == "figure 4" and check_the_type_of_a_first_premise() == "PaS" and check_the_type_of_a_second_premise() == "PaS": return "SiP"
    elif check_the_figure() == "figure 4" and check_the_type_of_a_first_premise() == "PaS" and check_the_type_of_a_second_premise() == "PeS": return "SeP"
    elif check_the_figure() == "figure 4" and check_the_type_of_a_first_premise() == "PiS" and check_the_type_of_a_second_premise() == "PaS": return "SiP"
    elif check_the_figure() == "figure 4" and check_the_type_of_a_first_premise() == "PeS" and check_the_type_of_a_second_premise() == "PaS": return "SoP"
    elif check_the_figure() == "figure 4" and check_the_type_of_a_first_premise() == "PeS" and check_the_type_of_a_second_premise() == "PiS": return "SoP"
   
print(conclusion())