#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 10:53:06 2020

@author: Z. H

Reference:
https://www.runoob.com/sqlite/sqlite-delete.htmls
"""

import sqlite3

dbname = 'Knowledge.db'

def CreateDatabase(dbname='Knowledge.db'):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    c.execute('''CREATE TABLE KNOWLEDGE (ID TEXT PRIMARY KEY NOT NULL, DESCRIPTION TEXT NOT NULL, LINK TEXT NOT NULL, OTHER TEXT NOT NULL);''')
    conn.commit()
    print ("Table created successfully")
    conn.close()
    return

def insert(ID,description, link,other='-',dbname='Knowledge.db'):
    conn = sqlite3.connect(dbname)
    #print('**   ',"INSERT INTO KNOWLEDGE (ID,DESCRIPTION,LINK,OTHER) \VALUES('"+ID+"','"+description+"','"+link+"','"+other+"')")
    c = conn.cursor()
    c.execute("INSERT INTO KNOWLEDGE (ID,DESCRIPTION,LINK,OTHER) \
              VALUES('"+ID+"','"+description+"','"+link+"','"+other+"')")
    conn.commit() 
    #print ("Records created successfully")
    conn.close()
    
    IDfile=open('ID.txt','a')
    IDfile.write(ID+'\n')
    IDfile.close()
    return

def select_all(dbname='Knowledge.db'):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    cursor = c.execute("SELECT id, description, link, other from KNOWLEDGE")
    for row in cursor:
        print("ID         : ",row[0])
        print("Description: ",row[1])
        print("Link       : ",row[2])
        print("Other      : ",row[3])
        print('\n')
    conn.close()
    return


def update(ID, upcol,upcontent,dbname='Knowledge.db'):
    """
    Which ID, which upcol to update. upcontent is the replaced content.
    """
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    c.execute("UPDATE KNOWLEDGE set "+upcol+" = '"+upcontent+"' where ID='"+ID+"'")
    conn.commit()
    conn.close()
    return

def delete(ID,dbname='Knowledge.db'):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    c.execute("DELETE from KNOWLEDGE where ID='"+ID+"';")
    conn.commit()
    conn.close()
    return

def like(keyword,dbname='Knowledge.db'):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    cursor = c.execute("SELECT * FROM KNOWLEDGE WHERE ID LIKE '%"+keyword+"%';")
    #print("SELECT * FROM KNOWLEDGE WHERE ID LIKE '%"+keyword+"%'")
    for row in cursor:
        print("ID         : ",row[0])
        print("Description: ",row[1])
        print("Link       : ",row[2])
        print("other      : ",row[3])
        print('\n')
    conn.close()
    return


    















