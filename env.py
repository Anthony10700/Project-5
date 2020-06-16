# !/usr/bin/python3
# -*- coding: Utf-8 -*


class Environment:
	def __init__(self):
		self.choice = ""
		self.history_choice = []
		self.history_result = []
		self.last_question = ""
		self.list_of_choice = []
		self.list_of_result = []
		self.categories_id = 0
		self.my_product_select = []

	def choice_check_numeric(self):
		value = str(self.choice)
		return value.isnumeric()

	def write_text_for_user(self, text, list_of_choices=[]):
		if len(list_of_choices) > 0:
			self.list_of_choice = list_of_choices
		self.last_question = text
		print(text)

	def print_last_phrase(self):
		print(self.last_question)

	def get_input_user(self):
		self.choice = input()
		print(self.choice)

	def input_user_verification(self):
		self.get_input_user()
		while self.choice not in self.list_of_choice:
			self.print_last_phrase()
			self.get_input_user()

	def print_element_array_product(self, temp_val, value_loop_for_incrementation):
		print(str(value_loop_for_incrementation).ljust(3) + " : " + str(temp_val[1]).strip().ljust(80) + " : " +
			  str(temp_val[0]).ljust(14) + " : " + str(temp_val[8]).upper())
		self.last_question = self.last_question + "\n" + (str(value_loop_for_incrementation).ljust(3) +
							" : " + str(temp_val[1]).ljust(80) + " : " + str(temp_val[0]).ljust(14) +
														  " : " + str(temp_val[8]).upper())

	def print_substitute_result_products(self, list_of_product_substitute, nb_of_selected_id, nts_select_id):
		i = 0
		print("ID".ljust(3) + " :                           DESCRIPTION                         "
													   "                   : ID IN DATABASE : NUTRI SCORE")
		self.list_of_choice = []
		self.history_result = []
		for one_result in list_of_product_substitute:
			if str(nb_of_selected_id) != str(one_result[0]) and \
				str(nts_select_id).lower() > str(one_result[8]).lower():
				i += 1
				print(str(i).ljust(3) + " : " + str(one_result[1]).ljust(80) + " : " + str(one_result[0]).ljust(14) + " : "
				  + str(one_result[8]).upper())
				self.list_of_choice.append(str(i))
				self.history_result.append(one_result)
			elif i == 0 and str(nts_select_id).lower() > str(one_result[8]).lower():
				print("PAS DE RESULTAT")
		if len(self.history_result)==0:
			print("Désoler il n'y a pas d'autre produit avec un nutri score moins élevé \n")

	@staticmethod
	def print_element_array_categories(temp_val, value_loop_for_incrementation):
		print(str(value_loop_for_incrementation).ljust(3) + " :   " +
			  str(temp_val[1]).ljust(60) +
			  " :  pour un total de  " + str(temp_val[3]).ljust(7) + "products")
