import tkinter as tk
from tkinter import ttk
import interface_Finalizar as iff
import interface_estado as ife
import interface_comentario as ifc

PALETTE = {
    "navy": "#123b63", "blue": "#1769aa", "light": "#eef4f8",
    "surface": "#ffffff", "ink": "#183247", "muted": "#617789",
    "border": "#d5e0e8", "green": "#16834a", "red": "#c93636",
}

janela = tk.Tk()
janela.title("Atualizador de Produção")
janela.geometry("1000x720")
janela.minsize(780, 580)
janela.configure(bg=PALETTE["light"])

style = ttk.Style(janela)
style.theme_use("clam")
style.configure("TFrame", background=PALETTE["light"])
style.configure("Card.TFrame", background=PALETTE["surface"])
style.configure("TLabel", background=PALETTE["light"], foreground=PALETTE["ink"], font=("Segoe UI", 10))
style.configure("Card.TLabel", background=PALETTE["surface"], foreground=PALETTE["ink"], font=("Segoe UI", 10))
style.configure("Title.TLabel", background=PALETTE["navy"], foreground="white", font=("Segoe UI", 20, "bold"))
style.configure("Subtitle.TLabel", background=PALETTE["navy"], foreground="#d6e7f4", font=("Segoe UI", 10))
style.configure("Section.TLabel", background=PALETTE["surface"], foreground=PALETTE["navy"], font=("Segoe UI", 12, "bold"))
style.configure("TButton", font=("Segoe UI", 10, "bold"), padding=(14, 8), background=PALETTE["blue"], foreground="white", borderwidth=0)
style.map("TButton", background=[("active", "#10578e")])
style.configure("Success.TButton", background=PALETTE["green"])
style.map("Success.TButton", background=[("active", "#106b3c")])
style.configure("Danger.TButton", background=PALETTE["red"])
style.map("Danger.TButton", background=[("active", "#a92929")])
style.configure("TEntry", padding=8, fieldbackground="white")
style.configure("TCombobox", padding=7, fieldbackground="white")
style.configure("TNotebook", background=PALETTE["light"], borderwidth=0)
style.configure("TNotebook.Tab", padding=(22, 11), font=("Segoe UI", 10, "bold"), background="#dfe9f0", foreground=PALETTE["ink"])
style.map("TNotebook.Tab", background=[("selected", "white")], foreground=[("selected", PALETTE["blue"])])
style.configure("Treeview", font=("Segoe UI", 9), rowheight=30, background="white", fieldbackground="white", foreground=PALETTE["ink"])
style.configure("Treeview.Heading", font=("Segoe UI", 9, "bold"), background="#e4edf4", foreground=PALETTE["navy"], padding=8)

header = tk.Frame(janela, bg=PALETTE["navy"], padx=28, pady=20)
header.pack(fill="x")
header.grid_columnconfigure(0, weight=1)
ttk.Label(header, text="Atualizador de Produção", style="Title.TLabel").grid(row=0, column=0, sticky="w")
ttk.Label(header, text="Operações simples, rastreáveis e conectadas ao Metabase", style="Subtitle.TLabel").grid(row=1, column=0, sticky="w", pady=(4, 0))
benefits = tk.Frame(header, bg=PALETTE["navy"])
benefits.grid(row=0, column=1, rowspan=2, sticky="e", padx=(24, 0))
tk.Label(benefits, text="●  Atualização direta no banco de dados\n●  Registro das operações por usuário\n●  Integração com o Metabase", justify="left", bg=PALETTE["navy"], fg="#d6e7f4", font=("Segoe UI", 9), padx=16).pack()

content = ttk.Frame(janela, padding=(22, 18, 22, 16))
content.pack(fill="both", expand=True)
aba_notebook = ttk.Notebook(content)
aba_notebook.pack(fill="both", expand=True)
aba1, aba2, aba3 = (ttk.Frame(aba_notebook, padding=18) for _ in range(3))
aba_notebook.add(aba1, text="  Finalizar  ")
aba_notebook.add(aba2, text="  Estado  ")
aba_notebook.add(aba3, text="  Comentários  ")
iff.interface_finalizar(aba1, janela)
ife.interface_estado(aba2, janela)
ifc.interface_comentario(aba3, janela)
footer = tk.Frame(janela, bg="white", padx=24, pady=9, highlightthickness=1, highlightbackground=PALETTE["border"])
footer.pack(fill="x", side="bottom")
tk.Label(footer, text="Atualizador de Produção  •  v1.0.0", bg="white", fg=PALETTE["muted"], font=("Segoe UI", 9)).pack(side="left")
tk.Label(footer, text="Sistema de operações", bg="white", fg=PALETTE["muted"], font=("Segoe UI", 9)).pack(side="right")
janela.mainloop()
