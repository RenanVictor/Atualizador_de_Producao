import tkinter as tk
from tkinter import ttk
from datetime import date
import Mensagens
import log_usuario 
import bancos
import Conexao



# Variaveis
hoje = date.today().strftime("%d/%m/%Y")
dict_banco = {}
list_valores = {}

def tabelas(registros):
    list_tabela=[]
    for registro in registros:
        list_tabela.append(registro['nome'])
    return list_tabela

# Funções
def interface_finalizar(root, mainRoot):
    

    def valor_cbx(event):
        global dict_banco
        dict_banco = bancos.find_dict(cbxBanco.get())
        if cbxBanco.get() == "Pedidos":
            lblStatus['text'] = "Status = 'Pronto'"
            lblOrdens['text'] = 'Favor informar a OP:'
            lbl_maquina.grid_forget()
            cbx_maquina.grid_forget()
            dict_banco['status'] = 'Pronto'
            dict_banco['cancelar'] = 'Montagem'
        elif cbxBanco.get() == "Comp.":
            lblStatus['text'] = "Status = 'Reportada'"
            lblOrdens['text'] = 'Favor informar o ID:'
            lbl_maquina.grid_forget()
            cbx_maquina.grid_forget()
            dict_banco['status'] = 'Reportada'
            dict_banco['cancelar'] = 'Primários'
        else:
            lbl_maquina.grid(row=3, column=0, sticky='w', padx=5, pady=5)
            lblStatus['text'] = "Status = 'Finalizado'"
            lblOrdens['text'] = 'Favor informar o ID:'
            lbl_maquina.grid(row=4, column=0, sticky='w', padx=5, pady=5)
            cbx_maquina.grid(row=4, column=1, sticky='w', padx=5, pady=5)
            dict_banco['status'] = 'Finalizado'
            dict_banco['cancelar'] = 'Programado'

    def update_finalizar():    
        global dict_banco
        dicionario = {}
        dicionario['status'] = dict_banco['status']
        dicionario['termino'] = date.today()
        dicionario['complemento'] = txtComplemento.get()
        dicionario['maquina'] = cbx_maquina.get()
        dicionario['item'] = txtOrdens.get()
        return dicionario
        
    def update_cancelar():    
        global dict_banco
        dicionario = {}
        dicionario['status'] = dict_banco['cancelar']
        dicionario['Termino'] = ''
        dicionario['maquina'] = cbx_maquina.get()
        dicionario['item'] = txtOrdens.get()
        return dicionario

    def btn_finalizar():
        global dict_banco
        log = log_usuario.usuario(dict_banco,update_finalizar())
        upgrade_register()
        Conexao.validacao_update(dict_banco,update_finalizar())
        log.insert_usuario()
    
        
    def sql_Cancelar():
        return

    def upgrade_register():
        registros = log_usuario.return_last_register()
        linhas = []
        for banco, item, data_log in registros:
            data_formatada = data_log.strftime('%d/%m/%Y') if isinstance(data_log, date) else str(data_log)
            linhas.append((str(banco), str(item), data_formatada))

        cabecalhos = ('BANCO', 'ITEM / OP', 'DATA')
        larguras = tuple(
            max(len(cabecalho), max((len(linha[indice]) for linha in linhas), default=0))
            for indice, cabecalho in enumerate(cabecalhos)
        )
        formato = f'{{:<{larguras[0]}}} | {{:<{larguras[1]}}} | {{:>{larguras[2]}}}'

        txtFinalizados.configure(state='normal')
        txtFinalizados.delete('1.0', tk.END)
        txtFinalizados.insert(tk.END, formato.format(*cabecalhos) + '\n', 'header')
        txtFinalizados.insert(tk.END, '-+-'.join('-' * largura for largura in larguras) + '\n')
        for linha in linhas:
            txtFinalizados.insert(tk.END, formato.format(*linha) + '\n')
        txtFinalizados.configure(state='disabled')


# Recursos da Janela
    root.columnconfigure(0, weight=1)
    root.rowconfigure(3, weight=1)
    
    #janela = tk.Tk()
    #janela.title('Finalizar processos')
    lblBanco = ttk.Label(root, text='Atualize o andamento de um item de produção', style='Section.TLabel')
    tblFrame = ttk.Frame(root, style='Card.TFrame', padding=18)
    tblBotoes = ttk.Frame(tblFrame, style='Card.TFrame')
    lblTabela = ttk.Label(tblFrame, text='Banco / tabela', style='Card.TLabel')
    lblStatus = ttk.Label(tblFrame, text='Status de destino', style='Card.TLabel')
    lblData = ttk.Label(tblFrame, text='Data: '+hoje, style='Card.TLabel')
    lblOrdens = ttk.Label(tblFrame, text='Número da OP ou ID', style='Card.TLabel')
    cbxBanco = ttk.Combobox(tblFrame, width=28, values=tabelas(bancos.dict_tabelas()), state='readonly')
    txtOrdens = ttk.Entry(tblFrame, width=32)
    btnFinalizar = ttk.Button(tblBotoes, text='✓  Finalizar', command=btn_finalizar, style='Success.TButton')
    btnCancelar = ttk.Button(tblBotoes, text='Cancelar', command=sql_Cancelar, style='Danger.TButton')
    txtFinalizados = tk.Text(root, height=10, font=('Consolas', 9), bg='white', fg='#183247', relief='flat', padx=12, pady=10, wrap='none')
    scrollFinalizados = ttk.Scrollbar(root, orient='horizontal', command=txtFinalizados.xview)
    txtFinalizados.configure(xscrollcommand=scrollFinalizados.set)
    txtFinalizados.tag_configure('header', font=('Consolas', 9, 'bold'), foreground='#126b62')
    lbl_maquina = ttk.Label(tblFrame, text='Máquina', style='Card.TLabel')
    cbx_maquina = ttk.Combobox(tblFrame, width=28, values=[
                            'DOBRA-1','DOBRA-2','LASER-1', 'LASER-2', 'LASER-3', 'PLASMA','PRENSA','PUNC.','TUBE'])
    lblComplemento = ttk.Label(tblFrame,text='Complemento (opcional)', style='Card.TLabel')
    txtComplemento = ttk.Entry(tblFrame, width=32)

    # layout da janela
    lblBanco.grid(row=0, column=0, sticky='w', pady=(0, 12))
    tblFrame.grid(row=1, column=0, sticky='ew', pady=(0, 16))
    tblFrame.columnconfigure(1, weight=1)
    for r, (label, widget) in enumerate(((lblTabela, cbxBanco), (lblStatus, lblData), (lblOrdens, txtOrdens), (lblComplemento, txtComplemento), (lbl_maquina, cbx_maquina))):
        label.grid(row=r, column=0, sticky='w', padx=(0, 16), pady=7)
        widget.grid(row=r, column=1, sticky='ew', pady=7)
    tblBotoes.grid(row=5, column=0, columnspan=2, sticky='w', pady=(12, 0))
    btnFinalizar.grid(row=0, column=0, padx=(0, 10))
    btnCancelar.grid(row=0, column=1)
    ttk.Label(root, text='Atividades recentes', style='Section.TLabel').grid(row=2, column=0, sticky='w', pady=(0, 8))
    txtFinalizados.grid(row=3, column=0, sticky='nsew')
    scrollFinalizados.grid(row=4, column=0, sticky='ew')
    

    cbxBanco.bind("<<ComboboxSelected>>", valor_cbx)
    upgrade_register()


'''janela = tk.Tk()
interface_finalizar(janela,janela)
janela.mainloop()'''
