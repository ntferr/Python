import psycopg2



conn = psycopg2.connect(port= 5433, host="localhost", database="banco", user="postgres", password="abc,12345678")
cur = conn.cursor()
cur.execute("SELECT * FROM public.funcionarios;")
obj = cur.fetchall()
cur.execute('''
            INSERT INTO funcionarios (name, idade)
            VALUES (%s, %s) '''
            ,('JJ', 45)) 
conn.commit()
print(obj)



cur.close()
conn.close()
