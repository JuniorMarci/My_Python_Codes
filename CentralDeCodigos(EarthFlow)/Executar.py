import tkinter as tk
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

class PythonScriptRunner:
    def __init__(self, script_path, folder_path):
        self.script_path = script_path
        self.folder_path = folder_path
        self.script_name = os.path.basename(script_path)

    def run_with_interpreter(self, interpreter, interpreter_name):
        append_to_terminal(f"{interpreter_name} iniciando execução do script: {self.script_path}")
        try:
            script_dir = os.path.dirname(self.script_path)
            run_command([interpreter, self.script_path], cwd=script_dir)
            append_to_terminal(f"{interpreter_name} finalizou execução do script: {self.script_path}", 'light green')
        except:
            append_to_terminal(f"{interpreter_name} falhou na execução do script: {self.script_path}", 'red')

    def run_with_py1(self):
        self.run_with_interpreter(Py1, "Executar com Py1")

    def run_with_py2(self):
        self.run_with_interpreter(Py2, "Executar com Py2")

    def run_with_py3(self):
        self.run_with_interpreter(Py3, "Executar com Py3")

    def edit_with_spy1(self):
        append_to_terminal(f"Editando {self.script_name} com SPy1")
        try:
            run_command([SPy1, self.script_path])
            append_to_terminal(f"SPy1 finalizou edição de {self.script_name}", 'light green')
        except:
            append_to_terminal(f"SPy1 falhou na edição de {self.script_name}", 'red')

    def edit_with_spy2(self):
        append_to_terminal(f"Editando {self.script_name} com SPy2")
        try:
            run_command([SPy2, self.script_path])
            append_to_terminal(f"SPy2 finalizou edição de {self.script_name}", 'light green')
        except:
            append_to_terminal(f"SPy2 falhou na edição de {self.script_name}", 'red')

    def edit_with_spy3(self):
        append_to_terminal(f"Editando {self.script_name} com SPy3")
        try:
            run_command([SPy3, self.script_path])
            append_to_terminal(f"SPy3 finalizou edição de {self.script_name}", 'light green')
        except:
            append_to_terminal(f"SPy3 falhou na edição de {self.script_name}", 'red')

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

def update_scripts(categoria):
    for widget in table_frame.winfo_children():
        widget.destroy()

    if categoria in categorias:
        scripts = categorias[categoria]
        row = 1
        for script_runner in scripts:
            btn_open = tk.Button(table_frame, text=f'Abrir Pasta', command=lambda sr=script_runner: run_function(sr.open_folder))
            btn_py1 = tk.Button(table_frame, text=f'Executar {script_runner.script_name} Py1', command=lambda sr=script_runner: run_function(sr.run_with_py1))
            btn_py2 = tk.Button(table_frame, text=f'Executar {script_runner.script_name} Py2', command=lambda sr=script_runner: run_function(sr.run_with_py2))
            btn_py3 = tk.Button(table_frame, text=f'Executar {script_runner.script_name} Py3', command=lambda sr=script_runner: run_function(sr.run_with_py3))
            btn_spy1 = tk.Button(table_frame, text=f'Editar {script_runner.script_name} SPy1', command=lambda sr=script_runner: run_function(sr.edit_with_spy1))
            btn_spy2 = tk.Button(table_frame, text=f'Editar {script_runner.script_name} SPy2', command=lambda sr=script_runner: run_function(sr.edit_with_spy2))
            btn_spy3 = tk.Button(table_frame, text=f'Editar {script_runner.script_name} SPy3', command=lambda sr=script_runner: run_function(sr.edit_with_spy3))

            btn_open.grid(row=row, column=0)
            btn_py1.grid(row=row, column=1)
            btn_py2.grid(row=row, column=2)
            btn_py3.grid(row=row, column=3)
            btn_spy1.grid(row=row, column=4)
            btn_spy2.grid(row=row, column=5)
            btn_spy3.grid(row=row, column=6)
            row += 1

def run_function(func):
    thread = Thread(target=func)
    thread.start()

def append_to_terminal(text, color='black'):
    terminal.insert(tk.END, text + '\n')
    terminal.tag_configure('red', foreground='red')
    terminal.tag_configure('green', foreground='green')
    terminal.tag_configure('light green', foreground='light green')
    terminal.tag_configure('yellow', foreground='yellow')
    terminal.insert(tk.END, text + '\n', color)
    terminal.yview(tk.END)

root = tk.Tk()
root.title("Script Runner")

menu_frame = tk.Frame(root)
menu_frame.pack(side=tk.TOP, fill=tk.X)

category_var = tk.StringVar(root)
category_var.set('Selecione uma Categoria')  # valor padrão

category_menu = tk.OptionMenu(menu_frame, category_var, *categorias.keys(), command=update_scripts)
category_menu.pack(side=tk.LEFT, padx=10, pady=5)

table_frame = tk.Frame(root)
table_frame.pack(fill=tk.BOTH, expand=True)

terminal = tk.Text(root, height=10, width=100, wrap='word')
terminal.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

root.mainloop()
