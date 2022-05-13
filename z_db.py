#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   z_db.py
@Time    :   2021/02/10
@Author  :   HDUZN
@Version :   1.1
@Contact :   hduzn@vip.qq.com
@License :   (C)Copyright 2021-2022
@Desc    :   操作数据库
'''

# here put the import lib
import sqlite3
import douban_config

# 清空 table_name表中数据，并且将自增量变为0
def delete_table(db_file, table_name):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    table_name_seq = douban_config.table_name_seq

    # 清空 table_name 表中数据
    sql1 = 'delete from ' + table_name
    cursor.execute(sql1)
    # 把 table_name 表的自增列序号变为0
    sql2 = 'update ' + table_name_seq + ' set seq = 0 where name = ' + "'" + table_name + "'"
    # sql2 = update sqlite_sequence set seq = 0 where name = 'hushen_300'
    cursor.execute(sql2)

    cursor.close()
    conn.commit()
    conn.close()

# 创建表
def create_table(db_file, sql):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute(sql)

    cursor.close()
    conn.commit()
    conn.close()

# 获取表的字段名
def get_colum_names_from_table(db_file, table_name):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    sql = 'pragma table_info({})'.format(table_name)
    cursor.execute(sql)
    results = cursor.fetchall()

    col_names = []
    for col in results:
        col_names.append(col[1])

    cursor.close()
    conn.commit()
    conn.close()
    return col_names

# 获取 insert sql语句 e.g insert into funds_dict (code, name, site) values (?, ?, ?)
def get_insert_sql_by_colum_names(table_name, col_name_list):
    sql1 = ' ('
    sql2 = ' ('
    for col in col_name_list:
        sql1 = sql1 + col
        if(col_name_list.index(col) == (len(col_name_list)-1)): # 判断col_name_list列表最后一个元素
            sql1 = sql1 + ') '
            sql2 = sql2 + '?)'
            break
        else:
            sql1 = sql1 + ', '
            sql2 = sql2 + '?, '
    # print(sql1) # e.g  (code, name, site)
    # print(sql2) # e.g (?, ?, ?)
    sql = 'insert into ' + table_name + sql1 + 'values' + sql2 # e.g insert into test (code, name, site) values (?, ?, ?)

    return sql

# insert list into table e.g data_list = ['1','a']
def insert_list_into_db(db_file, table_name, sql, data_list):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute(sql, tuple(data_list))

    cursor.close()
    conn.commit()
    conn.close()

# insert list into table e.g data_list = [['1','a'], ['2','b']]
def insert_into_db(db_file, table_name, sql, data_list):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    for data_line in data_list:
        cursor.execute(sql, tuple(data_line))

    cursor.close()
    conn.commit()
    conn.close()

# insert tuple list into table e.g data_tuple = [('1','a'), ('2','b')]
def insert_into_db_from_tuple(db_file, table_name, sql, data_tuple):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    for data_line in data_tuple:
        cursor.execute(sql, data_line)

    cursor.close()
    conn.commit()
    conn.close()

# 获取 select sql语句 e.g select code, site from data_index_dict
def get_select_sql_by_colum_names(table_name, col_name_list):
    sql1 = ''
    for col in col_name_list:
        sql1 = sql1 + col
        if(col_name_list.index(col) == (len(col_name_list)-1)): # 判断col_name_list列表最后一个元素
            break
        else:
            sql1 = sql1 + ', '
    sql = 'select ' + sql1 + ' from ' + table_name
    return sql

# 用select获取2个字段的记录，组成 Dictionary
def get_value_dict_from_table(db_file, table_name, col_names):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    sql = get_select_sql_by_colum_names(table_name, col_names)
    cursor.execute(sql)

    values = cursor.fetchall()
    # print(values)
    cursor.close()
    conn.close()

    # change values type to dictionary
    dict_data = dict(values)
    return dict_data

# 用select获取选定字段的记录
def get_values_by_colums_from_table(db_file, table_name, col_names):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    sql = get_select_sql_by_colum_names(table_name, col_names)
    cursor.execute(sql)
    values = cursor.fetchall()

    cursor.close()
    conn.close()
    return values

# 用select获取整个table表的内容
def get_values_from_table(db_file, table_name):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    sql = 'select * from ' + table_name
    cursor.execute(sql)
    values = cursor.fetchall()

    cursor.close()
    conn.close()
    return values

# 用select获取单个字段(唯一）的记录值 sql e.g select site from funds_dict where code = '310358'
def get_value_by_column_from_table(db_file, sql):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    cursor.execute(sql)
    value = cursor.fetchall()

    cursor.close()
    conn.close()
    return value[0][0]

def get_values(db_file, sql):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    cursor.execute(sql)
    values = cursor.fetchall()

    cursor.close()
    conn.close()
    return values

# main
def main():
    # table_col_names = get_colum_names_from_table(db_file, table_name)
    col_name_list = ['code', 'name', 'site']
    sql = get_insert_sql_by_colum_names('test', col_name_list)
    print(sql)
    
# main()
