"""Class for a one product description"""
# !/usr/bin/python3
# -*- coding: Utf-8 -*


class Product:
    """Class for a one product description"""
    def __init__(self):
        self.id_products = 0
        self.completed_name = ""
        self.countries = ""
        self.id_openfoodfacts = 0
        self.url = ""
        self.image_url = ""
        self.store = ""
        self.categories_str = ""
        self.nutriscore_grade = ""
        self.categories_idcategories = 0
        self.products_in_list = []
        self.product_id_sub = 0

    def load_product(self, product):
        """ For load a product :type product: list of 10 elements """
        product = list(product)
        self.products_in_list = product
        self.id_products = product[0]
        self.completed_name = product[1].replace("\n", "")
        self.countries = product[2].replace("\n", "")
        self.id_openfoodfacts = product[3]
        self.url = product[4].replace("\n", "")
        self.image_url = product[5].replace("\n", "")
        self.store = product[6].replace("\n", "")
        self.categories_str = product[7].replace("\n", "")
        self.nutriscore_grade = product[8].replace("\n", "")
        self.categories_idcategories = product[9]
        if len(product) == 11:
            self.product_id_sub = product[10]

    def return_product_in_list(self):
        """
        :rtype: list of product contain 10 elements
        """
        return self.products_in_list

    @property
    def get_id_products(self):
        """

        :rtype: int
        """
        return self.id_products

    @property
    def get_completed_name(self):
        """

        :rtype: string
        """
        return str(self.completed_name)

    @property
    def get_countries(self):
        """

        :rtype: string
        """
        return self.countries

    @property
    def get_id_openfoodfacts(self):
        """

        :rtype: int
        """
        return self.id_openfoodfacts

    @property
    def get_url(self):
        """

        :rtype: string
        """
        return self.url

    @property
    def get_image_url(self):
        """

        :rtype: string
        """
        return self.image_url

    @property
    def get_store(self):
        """

        :rtype: string
        """
        return self.store

    @property
    def get_categories_str(self):
        """
        :rtype: string
        """
        return self.categories_str

    @property
    def get_nutriscore_grade(self):
        """
        :rtype: string
        """
        return self.nutriscore_grade

    @property
    def get_categories_idcategories(self):
        """
        :rtype: int
        """
        return self.categories_idcategories

    @get_id_products.setter
    def set_id_products(self, value):
        self.id_products = value

    @get_completed_name.setter
    def set_completed_name(self, value):
        self.completed_name = value

    @get_countries.setter
    def set_countries(self, value):
        self.countries = value

    @get_id_openfoodfacts.setter
    def set_id_openfoodfacts(self, value):
        self.id_openfoodfacts = value

    @get_url.setter
    def set_url(self, value):
        self.url = value

    @get_image_url.setter
    def set_image_url(self, value):
        self.image_url = value

    @get_store.setter
    def set_store(self, value):
        self.store = value

    @get_categories_str.setter
    def set_categories_str(self, value):
        self.categories_str = value

    @get_nutriscore_grade.setter
    def set_nutriscore_grade(self, value):
        self.nutriscore_grade = value

    @get_categories_idcategories.setter
    def set_categories_idcategories(self, value):
        self.categories_idcategories = value
