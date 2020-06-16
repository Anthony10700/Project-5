"""Class for user environment"""
# !/usr/bin/python3
# -*- coding: Utf-8 -*


class Environment:
    """Class for user environment"""

    def __init__(self):
        self.choice = ""
        self.history_choice = []
        self.history_result = []
        self.last_question = ""
        self.list_of_choice = []
        self.list_of_result = []
        self.categories_id = 0
        self.my_product_select = []

    def write_text_for_user(self, text, list_of_choices=[]):
        """ function for write text for user save in last question et define list of choices
        :param list_of_choices:
        :type text: list of choices ex : ["1","2"] for 1 and 2 choices """
        if len(list_of_choices) > 0:
            self.list_of_choice = list_of_choices
        self.last_question = text
        print(text)

    def print_last_phrase(self):
        """:return last print phrase"""
        print(self.last_question)

    def get_input_user(self):
        """Get input user in the choice variable"""
        self.choice = input()
        # print(self.choice)

    def input_user_verification(self):
        """check the input text user is in the choice list"""
        self.get_input_user()
        while self.choice not in self.list_of_choice:
            self.print_last_phrase()
            self.get_input_user()

    def print_element_array_product(self, temp_val, value_loop_for_incrementation):
        """
        :type value_loop_for_incrementation: incremented value for list id
        :type temp_val: product select list of 9 element
        """
        phrases = "{0} : {1} : {2} : {3}".format(str(value_loop_for_incrementation).ljust(3),
                                                 str(temp_val[1]).strip().ljust(80),
                                                 str(temp_val[0]).ljust(14),
                                                 str(temp_val[8]).upper())
        print(phrases)

        self.last_question = \
            "{0}\n{1}".format(self.last_question, phrases)

    def print_substitute_result_products(self, list_of_product_substitute, nb_of_selected_id,
                                         nts_select_id):
        """
        :param nts_select_id: the nutri score of selected product
        :param nb_of_selected_id: the ID IN DATABASE of selected product
        :type list_of_product_substitute: list returned by database class, is the product substitute
        """
        i = 0
        phrases = "{0} :                           DESCRIPTION                                  " \
                  "          : ID IN DATABASE : NUTRI SCORE".format("ID".ljust(3))
        print(phrases)

        self.list_of_choice = []
        self.history_result = []
        for one_result in list_of_product_substitute:
            if str(nb_of_selected_id) != str(one_result[0]) and \
                    str(nts_select_id).lower() > str(one_result[8]).lower():
                i += 1
                phrases = "{0} : {1} : {2} : {3}".format(str(i).ljust(3),
                                                         str(one_result[1]).ljust(80),
                                                         str(one_result[0]).ljust(14),
                                                         str(one_result[8]).upper())
                print(phrases)
                self.list_of_choice.append(str(i))
                self.history_result.append(one_result)
            elif i == 0 and str(nts_select_id).lower() > str(one_result[8]).lower():
                print("PAS DE RESULTAT")
        if len(self.history_result) == 0:
            print("Désoler il n'y a pas d'autre produit avec un nutri score moins élevé \n")

    @staticmethod
    def print_element_array_categories(temp_val, value_loop_for_incrementation):
        """
        :param value_loop_for_incrementation: incremented value for list id
        :type temp_val: product select list of 9 element
        """
        phrases = "{0} :   {1} :  pour un total de  {2}products".format(
            str(value_loop_for_incrementation).ljust(3), str(temp_val[1]).ljust(60),
            str(temp_val[3]).ljust(7))
        print(phrases)
