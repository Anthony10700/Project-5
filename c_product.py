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
        self.nutrition_score_grade = ""
        self.categories_id_categories = 0
        self.products_in_list = []
        self.product_id_sub = 0

    def load_product(self, product):
        """
        For load a product :type product: list of 10 elements ,
        if number of element = 11 > it's saved products on db(product.save)

        """
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
        self.nutrition_score_grade = product[8].replace("\n", "")
        self.categories_id_categories = product[9]

        if len(product) == 11:
            self.product_id_sub = product[10]

    def return_product_in_list(self):
        """
        :rtype: list of product contain 10 elements,
        if return 11 element its saved product
        """
        return self.products_in_list

    @property
    def get_id_products(self):
        """
        get id of product
        :rtype: int
        """
        return self.id_products

    @property
    def get_completed_name(self):
        """
        det completed name of product
        :rtype: string
        """
        return str(self.completed_name)

    @property
    def get_countries(self):
        """
        get countries of product
        :rtype: string
        """
        return self.countries

    @property
    def get_id_openfoodfacts(self):
        """
        get id openfoodfacts of product
        :rtype: int
        """
        return self.id_openfoodfacts

    @property
    def get_url(self):
        """
        get url of product
        :rtype: string
        """
        return self.url

    @property
    def get_image_url(self):
        """
        get image url of product
        :rtype: string
        """
        return self.image_url

    @property
    def get_store(self):
        """
        get store of product
        :rtype: string
        """
        return self.store

    @property
    def get_categories_str(self):
        """
        get all categories in sting line separate per a ',' of product
        :rtype: string
        """
        return self.categories_str

    @property
    def get_nutrition_score_grade(self):
        """
        get nutrition score grade of product
        :rtype: string
        """
        return self.nutrition_score_grade

    @property
    def get_categories_idcategories(self):
        """
        get categories id of product
        :rtype: int
        """
        return self.categories_id_categories

    @get_id_products.setter
    def set_id_products(self, value):
        """

        :type value: int > id of product
        """
        self.id_products = value

    @get_completed_name.setter
    def set_completed_name(self, value):
        """

        :type value: string > name of product
        """
        self.completed_name = value

    @get_countries.setter
    def set_countries(self, value):
        """

        :type value: string > countries of product
        """
        self.countries = value

    @get_id_openfoodfacts.setter
    def set_id_openfoodfacts(self, value):
        """

        :type value: long > id openfoodfacts of product
        """
        self.id_openfoodfacts = value

    @get_url.setter
    def set_url(self, value):
        """

        :type value: string > url of product
        """
        self.url = value

    @get_image_url.setter
    def set_image_url(self, value):
        """

        :type value: string > image url of product
        """
        self.image_url = value

    @get_store.setter
    def set_store(self, value):
        """

        :type value: string > store of product
        """
        self.store = value

    @get_categories_str.setter
    def set_categories_str(self, value):
        """

        :type value: string > set all categories in string line separate per a ',' of product
        """
        self.categories_str = value

    @get_nutrition_score_grade.setter
    def set_nutrition_score_grade(self, value):
        """

        :type value: char > nutrition score grade
        """
        self.nutrition_score_grade = value

    @get_categories_idcategories.setter
    def set_categories_id_categories(self, value):
        """

        :type value: int > set categories id of product
        """
        self.categories_id_categories = value
