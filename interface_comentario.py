import tkinter as tk
from tkinter import ttk
import bancos
from interface_Finalizar import tabelas
import Conexao

def interface_comentario(root, mainRoot):
# funções
    def coluna_selecionada(event):
        if cbx_coluna.current() ==-1:
            lbl_campo_selecionado.grid_forget()
            txt_valor.grid_forget()
        else: 
            lbl_campo_selecionado.grid(row=3,column=0,sticky='w',padx=5)
            lbl_campo_selecionado['text'] = cbx_coluna.get()
            txt_valor.grid(row=3,column=1,sticky='w', padx=5)

        
    
    def update_estado():
        dict_banco = bancos.find_dict(cbx_banco.get())
        dict_banco['col_change'] = [cbx_coluna.get()]
        
        dicionario = {}
        if txt_valor.get()=='':
            dicionario[cbx_coluna.get()] = None
        else:
            if cbx_coluna.get()=='Previsao':
                from datetime import datetime as dt
                dicionario[cbx_coluna.get()] = dt.strptime(txt_valor.get(),"%d-%m-%Y").date()
            else:
                dicionario[cbx_coluna.get()] = txt_valor.get()
        if txt_item.get()!='':
            dicionario['item'] = txt_item.get()
            dict_banco['col_validacao'] = Conexao.atualiza_banco('select',dict_banco,dicionario['item'])['retorno'][0]
        print(Conexao.atualiza_banco('select',dict_banco,dicionario['item'])['retorno'][0])
        Conexao.validacao_update(dict_banco,dicionario)


    def update_alterar():
        update_estado()
        
        

#Recursos Janela
    root.columnconfigure(0, weight=1)
    lblTitulo = ttk.Label(root, text='Adicionar ou atualizar uma informação', style='Section.TLabel')
    tblFrame = ttk.Frame(root, style='Card.TFrame', padding=22)
    tblBotoes = ttk.Frame(root)
    lblTabela = ttk.Label(tblFrame, text='Banco / tabela', style='Card.TLabel')
    lblColuna = ttk.Label(tblFrame, text='Campo para atualizar', style='Card.TLabel')
    lbl_item = ttk.Label(tblFrame, text='Número da OP ou ID', style='Card.TLabel')
    lbl_campo_selecionado = ttk.Label(tblFrame,text='Novo valor', style='Card.TLabel')
    lbl_info = ttk.Label(tblFrame,text="Para datas, use o formato DD-MM-AAAA", style='Card.TLabel')
    cbx_banco = ttk.Combobox(tblFrame, width=30, values=tabelas(bancos.dict_tabelas()), state='readonly')
    cbx_coluna = ttk.Combobox(tblFrame, width=30, values=['Previsao','Complemento'], state='readonly')
    txt_item = ttk.Entry(tblFrame, width=32)
    txt_valor = ttk.Entry(tblFrame, width=32)

    btnEstado = ttk.Button(tblBotoes, text='Salvar alteração', command=update_alterar)
    
#Layout da Janela
    lblTitulo.grid(row=0, column=0, sticky='w', pady=(0, 12))
    tblFrame.grid(row=1, column=0, sticky='ew')
    tblFrame.columnconfigure(1, weight=1)
    for r, (label, widget) in enumerate(((lblTabela, cbx_banco), (lblColuna, cbx_coluna), (lbl_item, txt_item))):
        label.grid(row=r, column=0, sticky='w', padx=(0, 18), pady=10)
        widget.grid(row=r, column=1, sticky='ew', pady=10)
    tblBotoes.grid(row=2, column=0, sticky='w', pady=14)
    btnEstado.grid(row=0, column=0)
    lbl_info.grid(row=3, column=0, columnspan=2, sticky='w', pady=(0, 5))

    cbx_coluna.bind("<<ComboboxSelected>>",coluna_selecionada)
'''
janela = tk.Tk()
interface_comentario(janela,janela)
janela.mainloop()'''
