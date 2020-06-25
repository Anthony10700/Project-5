"""Class for categories products in data base"""
# !/usr/bin/python3
# -*- coding: Utf-8 -*


class Categories:
    """Class for categories products in data base"""
    def __init__(self):
        self.id_categories = 0
        self.completed_name = ""
        self.url = ""
        self.nb_of_products = 0
        self.categories_in_list = []

    def load_one_categories(self, categories):
        """
        load a categories from a tuple database sql
        :type categories: categories 1 list in 4 element
        """
        categories = list(categories)
        self.categories_in_list.append(categories)
        self.id_categories = categories[0]
        self.completed_name = categories[1]
        self.url = categories[2]
        self.nb_of_products = categories[3]

    def load_categories_in_list(self, categories_list):
        """
        load a categories from a  list tuple database sql
        :type categories_list: list of categories [x][4]
        """
        for one_categories in categories_list:
            categories = list(one_categories)
            self.categories_in_list.append(one_categories)
            self.id_categories = categories[0]
            self.completed_name = categories[1]
            self.url = categories[2]
            self.nb_of_products = categories[3]

    @property
    def get_id_categories(self):
        """
        get id from categories select
        :rtype: int
        """
        return self.id_categories

    @property
    def get_completed_name(self):
        """
        get completed from categories select
        :rtype: str
        """
        return self.completed_name

    @property
    def get_url(self):
        """
        get url from categories select
        :rtype: str
        """
        return self.url

    @property
    def get_nb_of_products(self):
        """
        get number of product from categories select
        :rtype: int
        """
        return self.nb_of_products

    @get_id_categories.setter
    def set_id_categories(self, value):
        """
        set id categories from categories select
        :type value: int > id categories
        """
        self.id_categories = value

    @get_completed_name.setter
    def set_completed_name(self, value):
        """
        set complete name of categories
        :type value: string value > complet name of categories
        """
        self.completed_name = value

    @get_url.setter
    def set_url(self, value):
        """
        set url of categories
        :type value: string value > complet url of categorie
        """
        self.url = value

    @get_nb_of_products.setter
    def set_nb_of_products(self, value):
        """
        set number of products in categories
        :type value: int value > number of categories
        """
        self.nb_of_products = value
