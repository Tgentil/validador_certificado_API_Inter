"""validador de certificado da API do Banco Inter """
# pylint: disable= line-too-long

import sys
import os
import stat
import subprocess
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

# Adicionando encoding para evitar erros de caracteres
sys.stdout.reconfigure(encoding='utf-8')

SENHA = "SUASENHA"


def create_window() -> None:
    """Cria a janela e define os widgets"""

    def abrir_arquivos():
        """Abre uma caixa de diálogo para selecionar o caminho dos arquivos"""
        arquivo_path = filedialog.askdirectory()
        entry_arquivo_path.delete(0, tk.END)
        entry_arquivo_path.insert(0, arquivo_path)

    def executar_comando():
        """Executa o comando OpenSSL com base nos valores inseridos na interface gráfica."""
        nome_empresa = entry_nome_empresa.get()
        numero_conta = entry_numero_conta.get()
        arquivo_path = entry_arquivo_path.get()

        # Gerar o nome do arquivo PFX
        nome_arquivo = f"{nome_empresa}_{numero_conta}.pfx"

        # Montar o comando OpenSSL com os valores obtidos
        comando = f"openssl pkcs12 -export -out {nome_arquivo} -inkey Inter_API_Chave.key -in Inter_API_Certificado.crt -password pass:{SENHA}"

        # Debug: Imprimir informações relevantes
        print("Diretório de trabalho atual:", os.getcwd())
        print("Comando OpenSSL:", comando)

        # Alterar para o diretório do arquivo
        os.chdir(arquivo_path)

        # Debug: Imprimir diretório de trabalho atual após a mudança
        print("Novo diretório de trabalho:", os.getcwd())

        # Conceder permissão de leitura a todos os arquivos no diretório
        for nome_arquivo in os.listdir(arquivo_path):
            caminho_arquivo = os.path.join(arquivo_path, nome_arquivo)
            if os.path.isfile(caminho_arquivo):
                os.chmod(caminho_arquivo, stat.S_IRUSR |
                        stat.S_IRGRP | stat.S_IROTH)

        # Executar o comando OpenSSL
        subprocess.run(comando, shell=True, check=True)

        messagebox.showinfo("Concluído", "Comando executado com sucesso!")

    # Criar a janela principal
    window = tk.Tk()
    window.title("Validador de Certificado SSL")
    window.geometry("850x150")  # Definindo as dimensões da janela

    # Adicionar espaçamento extra e centralizar os elementos
    window.grid_columnconfigure(0, weight=1)  # Centralizar elementos

    # Criar os widgets (input, botão, etc.)
    label_arquivo_path = tk.Label(window, text="Caminho dos Arquivos:")
    label_arquivo_path.grid(row=0, column=0, sticky="w", padx=10, pady=10)
    entry_arquivo_path = tk.Entry(window)
    entry_arquivo_path.grid(row=0, column=1, padx=10, pady=10)
    button_selecionar_arquivos = tk.Button(
        window, text="Selecionar", command=abrir_arquivos)
    button_selecionar_arquivos.grid(row=0, column=2, padx=10, pady=10)

    label_nome_empresa = tk.Label(window, text="Nome da Empresa:")
    label_nome_empresa.grid(row=1, column=0, sticky="w", padx=10, pady=10)
    entry_nome_empresa = tk.Entry(window)
    entry_nome_empresa.grid(row=1, column=1, padx=10, pady=10)

    label_numero_conta = tk.Label(window, text="Número da Conta:")
    label_numero_conta.grid(row=1, column=2, sticky="w", padx=10, pady=10)
    entry_numero_conta = tk.Entry(window)
    entry_numero_conta.grid(row=1, column=3, padx=10, pady=10)

    button_executar = tk.Button(
        window, text="Executar", command=executar_comando)
    button_executar.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

    # Iniciar a interface gráfica
    window.mainloop()


if __name__ == "__main__":
    create_window()
