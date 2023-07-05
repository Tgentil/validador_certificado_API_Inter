
 # Validador de Certificado da API do Banco Inter

<img align="left" src="https://raw.githubusercontent.com/khoa083/khoa/main/Khoa_ne/img/Rainbow.gif" width="100%">  

<br />

[![GitHub](https://img.shields.io/badge/Visit-My%20Profile-0891B2?style=flat-square&logo=github)](https://github.com/Tgentil)

Este script permite validar certificados da API do Banco Inter e executar o comando OpenSSL para gerar arquivos PFX.

## Pré-requisitos

Certifique-se de ter os seguintes requisitos antes de executar o script:

- Python  instalado
- Biblioteca Tkinter instalada (`pip install tkinter`)
- OpenSSL instalado e configurado corretamente no sistema

## Instalar Openssl no windowns

Para instalar o OpenSSL no Windows, siga os passos abaixo:

1. Abra o PowerShell como administrador.

2. Execute o seguinte comando para permitir a execução de scripts no seu sistema e para instalar o Chocolatey, um gerenciador de pacote:
   ```powershell
   Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
   ```

3. Em seguida, execute o comando abaixo para instalar o Openssl pelo chocolatey:

   ```powershell
   choco install openssl
   ```

Isso irá baixar e instalar o OpenSSL no seu sistema.

## Utilização

1. Clone o repositório ou faça o download dos arquivos.

2. Abra um terminal ou prompt de comando e navegue até o diretório do script.

3. Execute o seguinte comando para iniciar o script:

   ```shell
   python validador.py
   ```

4. Será aberta uma interface gráfica onde você poderá preencher as informações necessárias.

5. Clique no botão "Selecionar" ao lado de "Caminho dos Arquivos" para escolher o diretório onde estão localizados os arquivos do certificado.

6. Preencha o "Nome da Empresa" e o "Número da Conta".

7. Clique no botão "Executar" para gerar o arquivo PFX utilizando o comando OpenSSL.

   > Certifique-se de que o OpenSSL esteja instalado e configurado corretamente no seu sistema.

8. Após a conclusão do processo, uma mensagem de confirmação será exibida.

---

> 9. Alternativamente, você pode usar o executável gerado em [dist/validador.exe](./dist/validador.exe). Basta executar o arquivo `validador.exe` e preencher as informações necessárias na interface gráfica.

> Certifique-se de ter o arquivo `Inter_API_Chave.key` e `Inter_API_Certificado.crt` no mesmo diretório que o executável `validador.exe`.

---

## Exemplo de Saída:
```
Diretório de trabalho atual: c:\codes\validador_certificado_API_Inter
Comando OpenSSL: openssl pkcs12 -export -out Teste_1234.pfx -inkey Inter_API_Chave.key -in Inter_API_Certificado.crt -password pass:SUASENHA
Novo diretório de trabalho: C:\codes\validador_certificado_API_Inter\docs
```

## Notas

- O script utiliza a biblioteca Tkinter para criar a interface gráfica.
- Certifique-se de fornecer a senha correta no código-fonte (`SENHA = "SUASENHA"`).
- Este script foi desenvolvido para a validação de certificados da API do Banco Inter.
- Este script foi testado apenas utilizando o windowns 11.



## AUTOR
* Thiago da Silveira Gentil

---

Esse script é fornecido "como está" e sem garantias. Sinta-se à vontade para adaptá-lo e modificá-lo conforme necessário para atender às suas necessidades.
