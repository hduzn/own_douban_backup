#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   main.py
@Time    :   2022/05/12
@Author  :   HDUZN
@Version :   2.0
@Contact :   hduzn@vip.qq.com
@License :   (C)Copyright 2022-2023
@Desc    :  将Douban 读过的书记录保存到douban.xlsx 文件和数据库（sqlite）中
            更新于2022/05/12，采用selenium4版本，跳过selenium的webdriver检测（登录时需要手动划验证图片，但可以提前登录）
'''

# here put the import lib
import books, douban_config, z_db

# 创建数据库中表
def init_create_table():
    db_file = douban_config.db_file
    create_book_sql = '''
                        CREATE TABLE "books" (
                            "id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                            "name"	TEXT NOT NULL,
                            "site"	TEXT,
                            "author"	TEXT,
                            "tags"	TEXT,
                            "date"	TEXT,
                            "comments"	TEXT,
                            "rating_num"	INTEGER,
                            "rating"	TEXT,
                            "pic"	TEXT
                        );'''

    z_db.create_table(db_file, create_book_sql)
    print('------------books表创建完成')

# 初始化，创建数据库中表
init_create_table()

# 备份看过的书
#books.main()

