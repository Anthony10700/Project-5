"""The main programme"""
# !/usr/bin/python3
# -*- coding: Utf-8 -*
import random
import database
import env
import c_product
import c_categories


def main():
    """function to the main programme"""
    d_base = database.DataBase()
    d_base.connect_to_db()
    my_env = env.Environment()

    my_env.write_text_for_user("1 - Quel aliment souhaitez-vous remplacer ?\n"
                               "2 - Retrouver mes aliments substitués     ?", ["1", "2"])

    my_env.input_user_verification()

    if my_env.choice == "1":
        my_env.write_text_for_user("Sélectionnez la catégorie : \n")
        my_env.list_of_choice = []
        my_result = d_base.select_all_categories()
        for i in range(0, len(my_result)):
            my_categories = c_categories.Categories()
            my_categories.load_one_catagorie(my_result[i])
            my_env.list_of_choice.append(str(i))
            my_env.list_of_result.append(my_categories)
            my_env.print_element_array_categories(my_categories, i)
        my_env.input_user_verification()

        if my_env.choice in my_env.list_of_choice:
            my_env.categories_id = my_env.choice
            my_env.write_text_for_user(
                "Vous avez choisi : " + my_env.list_of_result[int(my_env.choice)].get_completed_name + "\n")
            my_result = d_base.select_all_products(int(my_env.choice) + 1)
            my_env.write_text_for_user(
                "Sélectionnez le produit : \n{0} :                           DESCRIPTION           "
                "                                 : ID IN DATABASE : NUTRI SCORE".format("ID".ljust(3)))
            my_env.list_of_result = []
            if len(my_result) > 0:
                for i in range(0, 40):
                    prod_list = c_product.Product()
                    prod_list.load_product(my_result[random.randint(0, len(my_result) - 1)])
                    my_env.list_of_choice.append(str(i))
                    my_env.list_of_result.append(prod_list)
                    my_env.print_element_array_product(prod_list, i)
            else:
                print("Longeur de my_result {0} !!!".format(len(my_result)))
                quit()

            my_env.input_user_verification()

            my_env.write_text_for_user(
                "Vous avez choisi        : {0}\nLe nutri score est      : {1}\nLes magasins sont   "
                "    : {2}\nUrl openfoodfacts est : {3}\n\n".format(
                    str(my_env.list_of_result[int(my_env.choice)].get_completed_name),
                    str(my_env.list_of_result[int(my_env.choice)].get_nutriscore_grade).upper(),
                    str(my_env.list_of_result[int(my_env.choice)].get_store),
                    str(my_env.list_of_result[int(my_env.choice)].get_url)))

            my_env.my_product_base = my_env.list_of_result[int(my_env.choice)]
            my_env.write_text_for_user("Voici les substituts : ")
            my_env.print_substitute_result_products(
                d_base.select_all_substitute_product(
                    my_env.list_of_result[int(my_env.choice)].get_categories_str,
                    my_env.categories_id),
                my_env.list_of_result[int(my_env.choice)].get_id_products,
                my_env.list_of_result[int(my_env.choice)].get_nutriscore_grade)

            if len(my_env.history_result) > 0:
                my_env.write_text_for_user("\nSélectionner votre substitue : ")
                my_env.input_user_verification()

                if my_env.choice in my_env.list_of_choice:
                    my_env.my_product_select = my_env.history_result[int(my_env.choice)]
                    my_env.write_text_for_user(
                        "Vous avez choisi comme substitue       : {0}\nLe nutri score est          "
                        "           : {1}\nLes magasins sont                      : {2}\nUrl "
                        "openfoodfacts est                  : {3}\n\n".format(
                            str(my_env.my_product_select.get_completed_name),
                            str(my_env.my_product_select.get_nutriscore_grade),
                            str(my_env.my_product_select.get_store),
                            str(my_env.my_product_select.get_url)))

            my_env.write_text_for_user("\n\n"
                                       "Souhaitez-vous enregistrer votre résultat dans la base de "
                                       "données ?\n" +
                                       "1 - oui \n"
                                       "2 - non \n"
                                       , ["1", "2"])

            my_env.input_user_verification()
            if my_env.choice in my_env.list_of_choice:

                if my_env.choice == "1" and len(my_env.history_result) > 0:
                    d_base.insert_product_for_save(my_env.my_product_select, my_env.my_product_base.get_id_products)
                    my_env.write_text_for_user("Le produit a bien été sauvegardé.")

                my_env.write_text_for_user("\n\n"
                                           "Souhaitez vous recommencer une recherche ?\n" +
                                           "1 - oui \n"
                                           "2 - non \n"
                                           , ["1", "2"])
                my_env.input_user_verification()

                if my_env.choice == "1":
                    main()
                else:
                    print("Au revoir")
                    quit()

    elif my_env.choice == "2":
        products_list = d_base.select_all_product_save
        i = 0
        my_env.write_text_for_user(
            "Liste des produits sauvegardés : \n{0} :                            DESCRIPTION       "
            "                                    : ID IN DATABASE : NUTRI SCORE\n".format("ID".ljust(18)))
        for product in products_list:
            prod_list = c_product.Product()
            prod_list.load_product(product)
            product_base = c_product.Product()
            db_product = d_base.select_a_product(prod_list.product_id_sub)
            product_base.load_product(db_product[0])
            i += 1
            my_env.print_element_saved(prod_list, product_base, i)


if __name__ == "__main__":
    main()
