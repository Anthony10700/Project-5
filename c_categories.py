"""Class for categories products in data base"""
# !/usr/bin/python3
# -*- coding: Utf-8 -*


class Categories:
    """Class for categories products in data base"""
    def __init__(self):
        self.idcategories = 0
        self.completed_name = ""
        self.url = ""
        self.nb_of_products = 0
        self.categories_in_list = []

    def load_one_catagorie(self, categories):
        """

        :type categories: categories 1 list in 4 element
        """
        categories = list(categories)
        self.categories_in_list.append(categories)
        self.idcategories = categories[0]
        self.completed_name = categories[1]
        self.url = categories[2]
        self.nb_of_products = categories[3]

    def load_catagories_in_list(self, categories_list):
        """

        :type categories_list: list of categories [x][4]
        """
        for one_categories in categories_list:
            categories = list(one_categories)
            self.categories_in_list.append(one_categories)
            self.idcategories = categories[0]
            self.completed_name = categories[1]
            self.url = categories[2]
            self.nb_of_products = categories[3]

    @property
    def get_idcategories(self):
        """

        :rtype: int
        """
        return self.idcategories

    @property
    def get_completed_name(self):
        """

        :rtype: str
        """
        return self.completed_name

    @property
    def get_url(self):
        """

        :rtype: str
        """
        return self.url

    @property
    def get_nb_of_products(self):
        """

        :rtype: int
        """
        return self.nb_of_products

    @get_idcategories.setter
    def set_idcategories(self, value):
        self.idcategories = value

    @get_completed_name.setter
    def set_completed_name(self, value):
        self.completed_name = value

    @get_url.setter
    def set_url(self, value):
        self.url = value

    @get_nb_of_products.setter
    def set_nb_of_products(self, value):
        self.nb_of_products = value
