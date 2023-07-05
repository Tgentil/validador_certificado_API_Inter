
## Validador de Certificado da API do Banco Inter

<img align="left" src="https://raw.githubusercontent.com/khoa083/khoa/main/Khoa_ne/img/Rainbow.gif" width="100%">  

<br />

[![GitHub](https://img.shields.io/badge/Visit-My%20Profile-0891B2?style=flat-square&logo=github)](https://github.com/Tgentil)

Este script permite validar certificados da API do Banco Inter e executar o comando OpenSSL para gerar arquivos PFX.

## Pré-requisitos

Certifique-se de ter os seguintes requisitos antes de executar o script:

- Python  instalado
- Biblioteca Tkinter instalada (`pip install tkinter`)
- OpenSSL instalado e configurado corretamente no sistema

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
- Antes de executar o script, verifique se você possui permissão para executar comandos OpenSSL no seu sistema.
- Este script foi testado apenas utilizando o windowns 11.



## AUTOR
* Thiago da Silveira Gentil

---

Esse script é fornecido "como está" e sem garantias. Sinta-se à vontade para adaptá-lo e modificá-lo conforme necessário para atender às suas necessidades.