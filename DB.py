import sqlite3 

class DB():
    def __init__(self):
        self.conexao = sqlite3.connect('./database.db')
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()
        c.execute("""create table if not exists alunos (
                    id integer primary key autoincrement ,
                    nome text,
                    materia text,
                    AV1 double null,
                    AV2 double null,
                    AVD double null)""")
        self.conexao.commit()
        c.close()