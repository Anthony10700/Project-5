# !/usr/bin/python3
# -*- coding: Utf-8 -*
import requests
import json
import mysql.connector


class DataBase:
	def __init__(self):
		self.my_cursor = object
		self.my_db = object
		self.host = "localhost",
		self.user = "root",
		self.password = "aqwXSZedcVFR"
		self.list_of_products = []

	def connect_to_db(self):
		self.my_db = mysql.connector.connect(
		host="localhost",
		user="root",
		password="aqwXSZedcVFR"
	)
		self.my_cursor = self.my_db.cursor()

	def select_to_db(self, sql_str):
		self.my_cursor.execute(sql_str)
		return self.my_cursor.fetchall()

	def insert_to_db(self, sql_insert_str, sql_value):
		self.my_cursor.execute(sql_insert_str, sql_value)
		self.my_db.commit()  # TEST IF RETURN ERROR BD EX: INSERT in babsdqsd.table

	def select_all_categories(self):
		return self.select_to_db("SELECT * FROM `openfoodfacts`.`categories`")

	def select_all_products(self, categories_id):
		return self.select_to_db("SELECT * FROM `openfoodfacts`.`products` WHERE "
								 "`openfoodfacts`.`products`.`categories_idcategories` = " + str(categories_id))

	def select_all_substitute_product(self, categories_str, categories_id):
		result = self.select_to_db("SELECT * FROM `openfoodfacts`.`products` WHERE "
								 "`openfoodfacts`.`products`.`categories_idcategories` = " + str(int(categories_id) + 1))
		list_of_return_value = []
		for i in range(0, len(result)):
			list_of_categories = str(result[i][7]).strip().split(",")
			list_of_select_categories = categories_str.strip().split(",")
			if list_of_categories[len(list_of_categories) - 1] == list_of_select_categories[len(list_of_select_categories) - 1]:
				list_of_return_value.append(result[i])

		if len(list_of_return_value) == 0:
			list_of_return_value.append(["NOTHING"]*10)

		return list_of_return_value

	def insert_product_for_save(self, product, categories_id):
		product = list(product)
		product.pop(0)
		sql = "INSERT INTO `openfoodfacts`.`products_save` (completed_name, countries, id_openfoodfacts, " \
				  "url, image_url, store, categories_str, nutriscore_grade , categories_idcategories) " \
				  "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

		self.my_cursor.execute(sql, tuple(product))
		self.my_db.commit()

	def select_all_product_save(self):
		result = self.select_to_db("SELECT * FROM `openfoodfacts`.`products_save`")
		list_of_return_value = []
		for i in range(0, len(result)):
			list_of_return_value.append(result[i])

		return list_of_return_value





