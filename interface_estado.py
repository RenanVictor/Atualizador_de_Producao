import tkinter as tk
from tkinter import ttk
import bancos
from interface_Finalizar import tabelas
import Conexao

def interface_estado(root, mainRoot):
# funções
    def estados_cbx(event):
        dict_banco = bancos.find_dict(cbx_banco.get())
        valores = Conexao.select_status(dict_banco['banco'])
        cbx_estado['values'] =valores
        return valores
    
    def update_estado():
        dict_banco = bancos.find_dict(cbx_banco.get())
        dict_banco['col_change'] = ['status']
        
        dicionario = {}
        dicionario['status'] = cbx_estado.get()
        if txtInfo.get()!='':
            dicionario['item'] = txtInfo.get()
            dict_banco['col_validacao'] = Conexao.atualiza_banco('select',dict_banco,dicionario['item'])['retorno'][0]
        print(Conexao.atualiza_banco('select',dict_banco,dicionario['item'])['retorno'][0])
        Conexao.validacao_update(dict_banco,dicionario)


    def update_alterar():
        update_estado()
        
        

#Recursos Janela
    root.columnconfigure(0, weight=1)
    lblTitulo = ttk.Label(root, text='Alterar estado de produção', style='Section.TLabel')
    tblFrame = ttk.Frame(root, style='Card.TFrame', padding=22)
    tblBotoes = ttk.Frame(root)
    lblTabela = ttk.Label(tblFrame, text='Banco / tabela', style='Card.TLabel')
    lblEstado = ttk.Label(tblFrame, text='Novo estado', style='Card.TLabel')
    lblinfo = ttk.Label(tblFrame, text='Número da OP ou ID', style='Card.TLabel')
    cbx_banco = ttk.Combobox(tblFrame, width=30, values=tabelas(bancos.dict_tabelas()), state='readonly')
    cbx_estado = ttk.Combobox(tblFrame, width=30, state='readonly')
    txtInfo = ttk.Entry(tblFrame, width=32)
    btnEstado = ttk.Button(tblBotoes, text='Aplicar alteração', command=update_alterar)
    
#Layout da Janela
    lblTitulo.grid(row=0, column=0, sticky='w', pady=(0, 12))
    tblFrame.grid(row=1, column=0, sticky='ew')
    tblFrame.columnconfigure(1, weight=1)
    for r, (label, widget) in enumerate(((lblTabela, cbx_banco), (lblEstado, cbx_estado), (lblinfo, txtInfo))):
        label.grid(row=r, column=0, sticky='w', padx=(0, 18), pady=10)
        widget.grid(row=r, column=1, sticky='ew', pady=10)
    tblBotoes.grid(row=2, column=0, sticky='w', pady=14)
    btnEstado.grid(row=0, column=0)

    cbx_banco.bind("<<ComboboxSelected>>",estados_cbx)

'''janela = tk.Tk()
interface_estado(janela,janela)
janela.mainloop()'''
