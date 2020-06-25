"""class for data base mysql management"""
# !/usr/bin/python3
# -*- coding: Utf-8 -*
import mysql.connector


class DataBase:
    """For database management (connection , select, insert etc.)"""

    def __init__(self, host="localhost", user="root", password="qsdfghjklm"):
        self.my_cursor = object
        self.my_db = object
        self.host = host
        self.user = user
        self.password = password
        self.list_of_products = []

    def connect_to_db(self):
        """Function for connect to data base mysql"""
        self.my_db = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password)
        self.my_cursor = self.my_db.cursor()

    def select_to_db(self, sql_str):
        """For the selection in data base :parameter sql_str = the sql select cmd"""
        self.my_cursor.execute(sql_str)
        return self.my_cursor.fetchall()

    def insert_to_db(self, sql_insert_str, sql_value):
        """For the insert in data base :parameter
        sql_insert_str = the sql insert cmd
        sql_value = the value for the cmd line"""
        self.my_cursor.execute(sql_insert_str, sql_value)
        self.my_db.commit()

    def select_a_product(self, id_of_product):
        """Select a product to a database"""
        return self.select_to_db("SELECT * FROM `openfoodfacts`.`products` WHERE `openfoodfacts`."
                                 "`products`.`idproducts` = {0}".format(str(id_of_product)))

    def select_all_categories(self):
        """Functione with select all categories in mysql data base"""
        return self.select_to_db("SELECT * FROM `openfoodfacts`.`categories`")

    def select_all_products(self, categories_id):
        """:parameter categories_id = the id in data base categories"""
        return self.select_to_db(
            "SELECT * FROM `openfoodfacts`.`products` WHERE "
            "`openfoodfacts`.`products`.`categories_idcategories` = {0}".format(str(categories_id)))

    def select_all_substitute_product(self, categories_str, categories_id):
        """
        :param categories_id: id of the categorie product
        :param categories_str:  categorie list string for the product
        :return list of subtitle product in order ascending of nutrition grade
        """

        result = self.select_to_db("SELECT * FROM `openfoodfacts`.`products` WHERE `openfoodfacts"
                                   "`.`products`.`categories_idcategories` = "
                                   "{0}".format(str(int(categories_id) + 1)))
        list_of_return_value = []
        for i, item in enumerate(result):
            list_of_categories = str(item[7]).replace("\'", " ").strip().split(",")
            list_of_select_categories = categories_str.replace("\'", " ").strip().split(",")

            for element in reversed(list_of_categories):
                for element_in in reversed(list_of_select_categories):
                    element_as_bytes = str.encode(element)
                    element_in_as_bytes = str.encode(element_in)
                    if element_as_bytes == element_in_as_bytes:
                        list_of_return_value.append(item)
                        break
                else:
                    continue
                break

        list_of_return_value = sorted(list_of_return_value, key=lambda test: test[8])

        if len(list_of_return_value) == 0:
            list_of_return_value.append(["NOTHING"] * 10)

        return list_of_return_value

    def insert_product_for_save(self, product, id_product_select):
        """
        :param id_product_select:
        :rtype: nothink
        :param product: the product to insert , the format is list 9 element
        """
        product = list(product.products_in_list)
        product.pop(0)
        sql = "INSERT INTO `openfoodfacts`.`products_save` (completed_name, countries, " \
              "id_openfoodfacts, url, image_url, store, categories_str, nutriscore_grade , " \
              "categories_idcategories, ancien_produits_sub) VALUES (%s, %s, %s, %s, %s, %s, %s," \
              " %s, %s, %s)"

        self.my_cursor.execute(sql, tuple(product) + (id_product_select,))
        self.my_db.commit()

    @property
    def select_all_product_save(self):
        """:return all product saved in data base table products_save"""
        result = self.select_to_db("SELECT * FROM `openfoodfacts`.`products_save`")
        list_of_return_value = []
        for i, item in enumerate(result):
            list_of_return_value.append(item)

        return list_of_return_value
