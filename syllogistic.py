# sentences

premise_1 = "Some humans are not mammals"
premise_2 = "No mammal is a reptile"

#to lower case
premise_1 = premise_1.lower()
premise_2 = premise_2.lower()

#split into a list
premise_1 = premise_1.split()
premise_2 = premise_2.split()

premise_1_first_element = premise_1[0]
premise_2_first_element = premise_2[0]

#check the type of a first sentence

def check_the_type_of_a_first_premise():
	if premise_1_first_element == "all": return "PaS"
	elif premise_1_first_element == "no" or premise_1_first_element == "any": return "PeS"
	elif premise_1_first_element == "some" and not_in_the_sentence() == False: return "PiS"
	elif premise_1_first_element == "some" and not_in_the_sentence() == True: return "PoS"
	else: return "The first premise does not have a correct form"

def not_in_the_sentence():
	if "not" in premise_1:
		return True
	else: return False


#check the type of a second sentence

def check_the_type_of_a_second_premise():
	if premise_2_first_element == "all": return "PaS"
	elif premise_2_first_element == "no" or premise_2_first_element == "any": return "PeS"
	elif premise_2_first_element == "some" and not_in_the_sentence() == False: return "PiS"
	elif premise_2_first_element == "some" and not_in_the_sentence() == True: return "PoS"
	else: return "The first premise does not have a correct form"

def not_in_the_sentence():
	if "not" in premise_2:
		return True
	else: return False


print(check_the_type_of_a_first_premise())
print(check_the_type_of_a_second_premise())

"""
#checking conditions
def check_conditions():
  if check_a_type() == "SoP" and check_b_type() == "SoP": return False 
  if check_a_type() == "SoP" and check_b_type() == "SiP": return False 
  if check_a_type() == "SiP" and check_b_type() == "SiP": return False 
  if check_a_type() == "SiP" and check_b_type() == "SoP": return False
  else: return True
print(check_conditions())



#conditions
def inform_about_condition():
  if check_conditions() == False: print("the condition is not met")
  else: check_the_figure()
inform_about_condition()
  
# 
def check_the_figure():
  pass

  """