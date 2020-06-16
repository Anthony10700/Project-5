# !/usr/bin/python3
# -*- coding: Utf-8 -*
import database
import env
import random


def main():
	db = database.DataBase()
	db.connect_to_db()
	my_env = env.Environment()

	my_env.write_text_for_user("1 - Quel aliment souhaitez-vous remplacer ?\n"
							   "2 - Retrouver mes aliments substitués     ?", ["1", "2"])

	my_env.input_user_verification()

	if my_env.choice == "1":
		my_env.write_text_for_user("Sélectionnez la catégorie : \n")
		my_env.list_of_choice = []
		my_result = db.select_all_categories()
		for i in range(0, len(my_result)):
			tp = my_result[i]
			my_env.list_of_choice.append(str(i))
			my_env.list_of_result.append(str(tp[1]))
			my_env.print_element_array_categories(tp, i)
		my_env.input_user_verification()

		if my_env.choice in my_env.list_of_choice:
			my_env.categories_id = my_env.choice
			my_env.write_text_for_user("Vous avez choisi : " + my_env.list_of_result[int(my_env.choice)] +
									   "\n")
			my_result = db.select_all_products(int(my_env.choice) + 1)
			my_env.write_text_for_user("Sélectionnez le produit : \n" +
									   "ID".ljust(3) + " :                           DESCRIPTION                         "
													   "                   : ID IN DATABASE : NUTRI SCORE")
			my_env.list_of_result = []

			for i in range(0, 140):
				tp = my_result[random.randint(0, len(my_result) - 1)]
				my_env.list_of_choice.append(str(i))
				my_env.list_of_result.append(tp)
				my_env.print_element_array_product(tp, i)
			my_env.input_user_verification()

			my_env.write_text_for_user(
				"Vous avez choisi        : " + str(my_env.list_of_result[int(my_env.choice)][1]) +
				"\nLe nutri score est      : " + str(my_env.list_of_result[int(my_env.choice)][8]).upper() +
				"\nLes magasins sont       : " + str(my_env.list_of_result[int(my_env.choice)][6]) +
				"\nUrl openfoodfacts est : " + str(my_env.list_of_result[int(my_env.choice)][4]) +
				"\n\n")
			my_env.write_text_for_user("Voici les substituts : ")
			my_env.print_substitute_result_products(
				db.select_all_substitute_product(
					my_env.list_of_result[int(my_env.choice)][7], my_env.categories_id),
				my_env.list_of_result[int(my_env.choice)][0],
				my_env.list_of_result[int(my_env.choice)][8])

			if len(my_env.history_result) > 0:
				my_env.write_text_for_user("\nSélectionner votre substitue : ")
				my_env.input_user_verification()

				if my_env.choice in my_env.list_of_choice:
					my_env.my_product_select = my_env.history_result[int(my_env.choice)-1]
					my_env.write_text_for_user(
						"Vous avez choisi comme substitue       : " + str(
							my_env.my_product_select[1]) +
						"\nLe nutri score est                     : " + str(
							my_env.my_product_select[8]).upper() +
						"\nLes magasins sont                      : " + str(
							my_env.my_product_select[6]) +
						"\nUrl openfoodfacts est                  : " + str(
							my_env.my_product_select[4]) +
						"\n\n")

			my_env.write_text_for_user("\n\n"
									   "Souhaitez-vous enregistrer votre résultat dans la base de données ?\n" +
									   "1 - oui \n"
									   "2 - non \n"
									   , ["1", "2"])

			my_env.input_user_verification()
			if my_env.choice in my_env.list_of_choice:
				if my_env.choice == "1":
					db.insert_product_for_save(my_env.my_product_select, my_env.categories_id)
				elif my_env.choice == "2":
					print("Bye bye")

	elif my_env.choice == "2":
		products_list = db.select_all_product_save()
		i = 0
		my_env.write_text_for_user("Liste des produits sauvegardés : \n" +
								   "ID".ljust(3) +
								   " :                           DESCRIPTION                         "
								   "                   : ID IN DATABASE : NUTRI SCORE\n")
		for product in products_list:
			i += 1
			my_env.print_element_array_product(product, i)


if __name__ == "__main__":
	main()
