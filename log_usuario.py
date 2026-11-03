import os
import Conexao
import gerenciamento_sql as gtsql

class usuario:
    def __init__(self,dict_banco,dict_valores):
        self.banco = dict_banco
        self.valores = dict_valores
        
    def list_valores(self):
        from datetime import date
        data_log = date.today()
        usuario = os.getlogin()
        sql = gtsql.gerador_sql(self.banco)
        lista_select = Conexao.atualiza_banco('select',self.banco,str(self.valores['item']))
        list_valores = [self.banco['banco'] ,self.valores['item'],data_log,usuario,lista_select['count_row'],sql.retorna_sql_update()]
        print(list_valores)
        return list_valores

    def insert_usuario(self):
        import bancos
        dict_log = bancos.find_dict('log_usuario')
        Conexao.atualiza_banco('insert',dict_log,self.list_valores())
        print('Log atualizado com sucesso!')
   
def return_last_register():
    usuario = os.getlogin()
    sql = f"select banco,item,data_log from log_usuario where usuario = '{usuario}' order by id DESC limit 8"
    resultado = Conexao.select_log(sql)
    return resultado
