#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   douban_config.py
@Time    :   2021/02/18
@Author  :   HDUZN
@Version :   1.1
@Contact :   hduzn@vip.qq.com
@License :   (C)Copyright 2021-2022
@Desc    :   config file update:2022/05/13
'''

douban_id = '[豆瓣登录id(邮箱名)]'
douban_pwd = '[豆瓣登录密码]'

books_site = 'https://book.douban.com'
movies_site = 'https://movie.douban.com'

# windows
# proj_path = r'G:\Python\douban'
db_file = r'.\db\douban.db'
ex_file = r'.\ex\douban.xlsx'

table_name_seq = 'sqlite_sequence'

# books.py
books_table_name = 'books'

book_sheet_name = 'books2022'
rating_dict = {
    '5': '★★★★★ 力荐',
    '4': '★★★★☆ 推荐',
    '3': '★★★☆☆ 还行',
    '2': '★★☆☆☆ 较差',
    '1': '★☆☆☆☆ 很差'
}
