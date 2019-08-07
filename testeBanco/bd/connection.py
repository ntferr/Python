#!/usr/bin/python
import psycopg2

class Connection():
    _con = None
    
    def __init__(self):
        self._conn = psycopg2.connect(host='localhost', port=5433, database='banco', user='postgres', password='abc,12345678')
        
    def inserir(self, pessoa):
        try:    
            self.cur = self._conn.cursor()
            self.cur.execute('''
                       INSERT INTO funcionarios (name, idade)
                       VALUES (%s, %s)'''
                        ,(pessoa.nome, pessoa.idade))
            self._conn.commit()
            self.cur.close()
            self._conn.close()
        except:
            self.cur.close()
            self._conn.close()
            
    def consultar(self):
        try:
            self.cur = self._conn.cursor()
            self.cur.execute('SELECT * FROM public.funcionarios;')
            obj = self.cur.fetchall()
            self.cur.close()
            self._conn.close()
            
            return obj
        except:
            self.cur.close()
            self._conn.close()
            
            