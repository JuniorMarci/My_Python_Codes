import tkinter as tk
from tkinter import ttk
from threading import Thread
import subprocess
import os

def run_command(command, cwd=None):
    result = subprocess.run(command, shell=True, capture_output=True, text=True, encoding='latin1', errors='ignore', cwd=cwd)
    return result.stdout

# Caminhos para os intérpretes Python
Py1 = r"C:\...\Py\Portable Python-3.10.5 x64\Python-Launcher.exe"
Py2 = r"C:\...\Py2\Portable Python-3.10.5 x64\Python-Launcher.exe"
Py3 = r"C:\...\Py3\Portable Python-3.10.5 x64\Python-Launcher.exe"

# Caminhos para os editores PyScripter
SPy1 = r"C:\...\Py\Portable Python-3.10.5 x64\PyScripter-Launcher"
SPy2 = r"C:\...\Py2\Portable Python-3.10.5 x64\PyScripter-Launcher"
SPy3 = r"C:\...\Py3\Portable Python-3.10.5 x64\PyScripter-Launcher"

tag_counter = 0

def append_to_terminal(text, color='white'):
    global tag_counter
    terminal_text.configure(state=tk.NORMAL)
    tag_name = f'tag{tag_counter}'
    terminal_text.tag_config(tag_name, foreground=color)
    terminal_text.insert(tk.END, text + '\n', tag_name)
    terminal_text.yview(tk.END)
    terminal_text.configure(state=tk.DISABLED)
    tag_counter += 1

def run_command_with_status(command, status_label, cwd=None):
    status_label.config(text="Executando...", fg='orange')
    root.update_idletasks()
    result = run_command(command, cwd=cwd)
    status_label.config(text="Pronto", fg='green')
    return result

def run_function(func):
    Thread(target=func).start()

class PythonScriptRunner:
    def __init__(self, script_path, folder_path):
        self.script_path = script_path
        self.folder_path = folder_path

    def run_with_interpreter(self, interpreter, interpreter_name, status_label):
        append_to_terminal(f"{interpreter_name} iniciando execução do script: {self.script_path}")
        try:
            script_dir = os.path.dirname(self.script_path)
            run_command_with_status([interpreter, self.script_path], status_label, cwd=script_dir)
            append_to_terminal(f"{interpreter_name} finalizou execução do script: {self.script_path}", 'light green')
        except:
            append_to_terminal(f"{interpreter_name} falhou na execução do script: {self.script_path}", 'red')

    def run_with_py1(self):
        self.run_with_interpreter(Py1, "Python 1", status_py1)

    def run_with_py2(self):
        self.run_with_interpreter(Py2, "Python 2", status_py2)

    def run_with_py3(self):
        self.run_with_interpreter(Py3, "Python 3", status_py3)

    def edit_with_spy1(self):
        append_to_terminal(f"Editando script com SPy1: {self.script_path}")
        try:
            run_command([SPy1, self.script_path])
            append_to_terminal(f"SPy1 finalizou edição do script: {self.script_path}", 'light green')
        except:
            append_to_terminal(f"SPy1 falhou na edição do script: {self.script_path}", 'red')

    def edit_with_spy2(self):
        append_to_terminal(f"Editando script com SPy2: {self.script_path}")
        try:
            run_command([SPy2, self.script_path])
            append_to_terminal(f"SPy2 finalizou edição do script: {self.script_path}", 'light green')
        except:
            append_to_terminal(f"SPy2 falhou na edição do script: {self.script_path}", 'red')

    def edit_with_spy3(self):
        append_to_terminal(f"Editando script com SPy3: {self.script_path}")
        try:
            run_command([SPy3, self.script_path])
            append_to_terminal(f"SPy3 finalizou edição do script: {self.script_path}", 'light green')
        except:
            append_to_terminal(f"SPy3 falhou na edição do script: {self.script_path}", 'red')

    def open_folder(self):
        append_to_terminal(f"Abrindo pasta: {self.folder_path}")
        try:
            run_command(['start', '', self.folder_path])
            append_to_terminal(f"Pasta {self.folder_path} aberta com sucesso.", 'light green')
        except:
            append_to_terminal(f"Falha ao abrir a pasta: {self.folder_path}", 'red')

# Definindo categorias e scripts
categorias = {
    'TITULO 1': [
        PythonScriptRunner("C:/.../_Base.py", "C:/...(PASTA)"),
        PythonScriptRunner("C:/.../Juntar.py", "C:/...(PASTA)"),
    ],
    'TITULO 2': [
        PythonScriptRunner("C:/.../_Base.py", "C:/...(PASTA)"),
        PythonScriptRunner("C:/.../Juntar.py", "C:/...(PASTA)"),
        PythonScriptRunner("C:/.../Analisar.py", "C:/...(PASTA)"),
    ]


}

def update_display(selected_category):
    for widget in table_frame.winfo_children():
        widget.destroy()

    if selected_category in categorias:
        scripts = categorias[selected_category]
        row = 0  # Começa a partir da linha 0 para a categoria selecionada
        for script_runner in scripts:
            script_name = os.path.basename(script_runner.script_path)

            # Adiciona os botões para cada script
            btn_open = tk.Button(table_frame, text=f"Abrir Pasta", command=script_runner.open_folder)
            btn_py1 = tk.Button(table_frame, text=f"Py1: {script_name}", command=lambda sr=script_runner: run_function(sr.run_with_py1))
            btn_py2 = tk.Button(table_frame, text=f"Py2: {script_name}", command=lambda sr=script_runner: run_function(sr.run_with_py2))
            btn_py3 = tk.Button(table_frame, text=f"Py3: {script_name}", command=lambda sr=script_runner: run_function(sr.run_with_py3))
            btn_spy1 = tk.Button(table_frame, text=f"SPy1: {script_name}", command=lambda sr=script_runner: run_function(sr.edit_with_spy1))
            btn_spy2 = tk.Button(table_frame, text=f"SPy2: {script_name}", command=lambda sr=script_runner: run_function(sr.edit_with_spy2))
            btn_spy3 = tk.Button(table_frame, text=f"SPy3: {script_name}", command=lambda sr=script_runner: run_function(sr.edit_with_spy3))

            btn_open.grid(row=row, column=0, padx=5, pady=5, sticky="ew")
            btn_py1.grid(row=row, column=1, padx=5, pady=5)
            btn_py2.grid(row=row, column=2, padx=5, pady=5)
            btn_py3.grid(row=row, column=3, padx=5, pady=5)
            btn_spy1.grid(row=row, column=4, padx=5, pady=5)
            btn_spy2.grid(row=row, column=5, padx=5, pady=5)
            btn_spy3.grid(row=row, column=6, padx=5, pady=5)
            row += 1

def on_category_selected(event):
    selected_category = category_combobox.get()
    update_display(selected_category)

root = tk.Tk()
root.title("Controle de Scripts")

# Combobox para seleção de categorias
category_combobox = ttk.Combobox(root, values=list(categorias.keys()), state="readonly")
category_combobox.pack(padx=10, pady=5)
category_combobox.bind("<<ComboboxSelected>>", on_category_selected)

# Cria o painel de exibição dos botões
table_frame = tk.Frame(root)
table_frame.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

# Terminal
terminal_frame = tk.Frame(root)
terminal_frame.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

terminal_text = tk.Text(terminal_frame, height=15, width=100, bg='black', fg='white', wrap=tk.WORD)
terminal_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Barra de rolagem para o terminal
scrollbar = tk.Scrollbar(terminal_frame, command=terminal_text.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
terminal_text.config(yscrollcommand=scrollbar.set)

# Status dos botões
status_frame = tk.Frame(root)
status_frame.pack(padx=10, pady=5, fill=tk.X)

status_py1 = tk.Label(status_frame, text="Pronto", fg="green")
status_py1.pack(side=tk.LEFT, padx=5)

status_py2 = tk.Label(status_frame, text="Pronto", fg="green")
status_py2.pack(side=tk.LEFT, padx=5)

status_py3 = tk.Label(status_frame, text="Pronto", fg="green")
status_py3.pack(side=tk.LEFT, padx=5)

root.mainloop()
