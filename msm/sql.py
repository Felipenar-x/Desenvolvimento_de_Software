import sqlite3
import pegar_lista
banco = sqlite3.connect('Monstros.db')

cursor = banco.cursor()
#cursor.execute("CREATE TABLE monstros(nome text,monstros_necessarios text)")
cursor.execute("INSERT INTO monstros (nome) VALUES ('kayna')")
#for i in range(len(pegar_lista.total)):
#   cursor.execute("INSERT INTO monstros (monstros_necessarios) VALUES(?)",(pegar_lista.total[i]) )


banco.commit()

