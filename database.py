"""class for data base mysql management"""
# !/usr/bin/python3
# -*- coding: Utf-8 -*
import mysql.connector


class DataBase:
    """For database management (connection , select, insert etc.)"""

    def __init__(self):
        self.my_cursor = object
        self.my_db = object
        self.host = "localhost"
        self.user = "root"
        self.password = "aqwXSZedcVFR"
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
        self.my_db.commit()  # TEST IF RETURN ERROR BD EX: INSERT in babsdqsd.table

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
        """        :param categories_id: id of the categorie product
        :param categories_str:  categorie list string for the product"""

        result = self.select_to_db("SELECT * FROM `openfoodfacts`.`products` WHERE `openfoodfacts"
                                   "`.`products`.`categories_idcategories` = "
                                   "{0}".format(str(int(categories_id) + 1)))
        list_of_return_value = []
        for i in range(0, len(result)):
            list_of_categories = str(result[i][7]).replace("\'", " ").strip().split(",")
            list_of_select_categories = categories_str.replace("\'", " ").strip().split(",")

            for element in reversed(list_of_categories):
                for element_in in reversed(list_of_select_categories):
                    element_as_bytes = str.encode(element)
                    element_in_as_bytess = str.encode(element_in)
                    if element_as_bytes == element_in_as_bytess:
                        list_of_return_value.append(result[i])
                        break
                else:
                    continue
                break

        var_i = 0
        while var_i < len(list_of_return_value) - 1:
            car_one = list_of_return_value[var_i][8]
            car_two = list_of_return_value[var_i + 1][8]
            if car_one > car_two:
                tmp = list_of_return_value[var_i]
                list_of_return_value[var_i] = list_of_return_value[var_i + 1]
                list_of_return_value[var_i + 1] = tmp
                var_i = 0
            var_i += 1
        var_i = 0
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
        for i in range(0, len(result)):
            list_of_return_value.append(result[i])

        return list_of_return_value
