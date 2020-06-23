"""The script for import api open food facts data with data base mysql"""
# !/usr/bin/python3
# -*- coding: Utf-8 -*
import json
import requests
import mysql.connector
ST_OF_CATEGORIES = 0
NB_OF_CATEGORIES = 6  # the number of categories in data base
NB_OF_PAGE_DL = 20  # 1 page = 20 products


def main():
    """This function import api open food facts data and make new DATA BASE myslq and
    table """
    my_db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="aqwXSZedcVFR"
    )
    my_cursor = my_db.cursor()

    url = "https://fr.openfoodfacts.org/categories.json"

    payload = {}
    headers = {}
    data_all = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    test = json.loads(response.text.encode('utf8'))

    test = test["tags"][ST_OF_CATEGORIES:ST_OF_CATEGORIES+NB_OF_CATEGORIES]

    # create DATABASE and drop if exist
    my_cursor.execute("DROP DATABASE IF EXISTS openfoodfacts")

    my_cursor.execute("CREATE DATABASE openfoodfacts")

    my_cursor.execute(
        "CREATE TABLE IF NOT EXISTS `openfoodfacts`.`categories` ("
        "  `idcategories` INT NOT NULL AUTO_INCREMENT,"
        "  `completed_name` LONGTEXT NOT NULL,"
        "  `URL` TEXT NOT NULL,"
        "  `nb_of_products` BIGINT NOT NULL,"
        "  PRIMARY KEY (`idcategories`))"
        "ENGINE = InnoDB;"
    )

    for product_ in test:
        sql = "INSERT INTO `openfoodfacts`.`categories` (completed_name, URL, nb_of_products)" \
              " VALUES (%s, %s, %s)"
        val = (str(product_["name"]).replace("'", " ").replace("\n", ""), product_["url"],
               product_["products"])
        my_cursor.execute(sql, val)

    my_db.commit()

    for product_ in test:
        list_temp = []
        for i in range(1, NB_OF_PAGE_DL):
            print(product_["url"] + "/" + str(i) + ".json")
            url_in = product_["url"] + "/" + str(i) + ".json"
            response = requests.request("GET", url_in, headers=headers, data=payload)
            data = json.loads(response.text.encode('utf8'))
            data = data["products"]
            data_temp = []
            for d_var in data:
                if str(d_var['categories_lc']) == "fr":
                    data_temp.append(d_var)
            list_temp.extend(data_temp)
        data_all.update({str(product_["name"]).replace("'", " ").replace("\n", ""): list_temp})

    my_cursor.execute(
        "CREATE TABLE IF NOT EXISTS `openfoodfacts`.`products` ("
        "  `idproducts` INT NOT NULL AUTO_INCREMENT,"
        "  `completed_name` TEXT NOT NULL,"
        "  `countries` TEXT NOT NULL,"
        "  `id_openfoodfacts` TEXT NOT NULL,"
        "  `url` TEXT NOT NULL,"
        "  `image_url` TEXT NULL,"
        "  `store` TEXT NULL,"
        "  `categories_str` TEXT NOT NULL,"
        "  `nutriscore_grade` VARCHAR(45) NOT NULL,"
        "  `categories_idcategories` INT NOT NULL,"
        "  PRIMARY KEY (`idproducts`, `categories_idcategories`),"
        "  INDEX `fk_products_categories_idx` (`categories_idcategories` ASC) VISIBLE,"
        "  CONSTRAINT `fk_products_categories`"
        "   FOREIGN KEY (`categories_idcategories`)"
        "   REFERENCES `openfoodfacts`.`categories` (`idcategories`)"
        "     ON DELETE NO ACTION"
        "   ON UPDATE NO ACTION)"
        "ENGINE = InnoDB"
    )

    my_cursor.execute(
        "CREATE TABLE IF NOT EXISTS `openfoodfacts`.`products_save` ("
        "  `idproducts` INT NOT NULL AUTO_INCREMENT,"
        "  `completed_name` TEXT NOT NULL,"
        "  `countries` TEXT NOT NULL,"
        "  `id_openfoodfacts` TEXT NOT NULL,"
        "  `url` TEXT NOT NULL,"
        "  `image_url` TEXT NULL,"
        "  `store` MEDIUMTEXT NULL,"
        "  `categories_str` TEXT NOT NULL,"
        "  `nutriscore_grade` VARCHAR(45) NOT NULL,"
        "  `categories_idcategories` INT NOT NULL,"
        "  `ancien_produits_sub` INT NOT NULL,"
        "  PRIMARY KEY (`idproducts`, `categories_idcategories`, `ancien_produits_sub`),"
        "  INDEX `fk_products_categories_idx` (`categories_idcategories` ASC) VISIBLE,"
        "  CONSTRAINT `fk_products_categories0`"
        "    FOREIGN KEY (`categories_idcategories`)"
        "    REFERENCES `openfoodfacts`.`categories` (`idcategories`)"
        "    ON DELETE NO ACTION"
        "    ON UPDATE NO ACTION,"
        "  CONSTRAINT `fk_products_sub`"
        "    FOREIGN KEY (`idproducts`)"
        "    REFERENCES `openfoodfacts`.`products` (`idproducts`)"
        "    ON DELETE NO ACTION"
        "    ON UPDATE NO ACTION)"
        "ENGINE = InnoDB"
    )

    for product_ in data_all:
        print(product_)
        sql_in = "SELECT idcategories FROM `openfoodfacts`.`categories` WHERE " \
              "`openfoodfacts`.`categories`.`completed_name` =\'{0}\'".format(str(product_).replace("'", " ").
                                                                              replace("\n", ""))
        my_cursor.execute(sql_in)
        my_result = my_cursor.fetchall()
        for unique_product in data_all[product_]:
            sql = 'INSERT INTO `openfoodfacts`.`products` (completed_name, countries, ' \
                  'id_openfoodfacts, ' \
                  'url, image_url, store, categories_str,nutriscore_grade , ' \
                  'categories_idcategories) ' \
                  'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'

            val = ()
            for value in range(0, 8):
                list_of_key = ["product_name", "countries", "id", "url", "image_url",
                               "stores", "categories", "nutriscore_grade"]
                if unique_product.get(list_of_key[value], "") == "":
                    val = val + ("No_" + list_of_key[value],)
                else:
                    val = val + (unique_product[list_of_key[value]],)
            val = val + (my_result[0][0], )

            my_cursor.execute(sql, val)
        my_db.commit()


if __name__ == "__main__":
    main()
