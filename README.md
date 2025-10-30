```markdown
# 💼 Gerador de Recibos em PDF (Python)

Um utilitário simples e direto para gerar **recibos de pagamento em PDF** — ideal 
para profissionais autônomos ou prestadores de serviço.  
Desenvolvido em **Python 3** com a biblioteca [ReportLab](https://www.reportlab.com/opensource/), 
o app pergunta os dados do cliente e gera automaticamente um recibo formatado e salvo em PDF.

---

## 🚀 Funcionalidades

- Gera recibos de pagamento personalizados em formato **PDF**.  
- Detecta e formata automaticamente **CPF** ou **CNPJ**.  
- Permite escolher a **forma de pagamento** (PIX, dinheiro, cartão, transferência, outro).  
- Permite definir **serviço prestado**, **data do pagamento** e **emissor**.  
- Salva o arquivo com nome automático no formato:
```

Recibo - NOME_DO_CLIENTE - DD-MM-AAAA.pdf

````

---

## 🖼️ Exemplo de uso

```bash
=== GERADOR DE RECIBO DE PAGAMENTO ===

Nome do cliente: João da Silva
CNPJ/CPF do cliente: 12345678901
Serviço prestado: Manutenção de notebook
Valor (ex: 150 ou 150.50): 200
=== Escolha a forma de pagamento ===
1 = PIX
2 = Dinheiro
3 = Cartão
4 = Transferência
5 = Outro
Digite o número da opção: 1
Data do pagamento (dd/mm/aaaa) [pressione Enter para hoje]: 
Nome do emissor [padrão: André Oliveira - Serviços de Informática]:
````

✅ Resultado:

```
Recibo - João da Silva - 30-10-2025.pdf
```

---

## 📦 Instalação

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/andreopo32/gerar-recibo.git
cd gerar-recibo
```

### 2️⃣ Criar ambiente virtual e instalar dependências

```bash
python3 -m venv venv
source venv/bin/activate
pip install reportlab
```

### 3️⃣ Executar o programa

```bash
python3 gerar_recibo.py
```

---

## ⚙️ Tornar o script um comando do sistema (opcional)

Se quiser rodar o programa como um app (sem digitar `python3`):

```bash
chmod +x gerar_recibo.py
sudo ln -s $(pwd)/gerar_recibo.py /usr/local/bin/gerar-recibo
```

Agora você pode rodar:

```bash
gerar-recibo
```

---

## 🧰 Compilar para executável (opcional)

Para gerar um binário único que não depende do Python:

```bash
pip install pyinstaller
pyinstaller --onefile gerar_recibo.py
```

O executável final estará em:

```
dist/gerar_recibo
```

---

## 📂 Onde os recibos são salvos?

Os PDFs são salvos **na mesma pasta em que o programa é executado**,
com o nome:

```
Recibo - NOME_DO_CLIENTE - DD-MM-AAAA.pdf
```

Exemplo:

```
Recibo - João da Silva - 30-10-2025.pdf
```

---

## 🧑‍💻 Autor

**André Oliveira**
Serviços de Informática 💻
📍 Brasil
📧 *andre.oliveira26@gmail.com*

---

## 🪪 Licença

Este projeto é distribuído sob a licença **MIT** — sinta-se livre para usar, modificar e distribuir.

---

## 🌟 Dica

Se quiser que o app apareça no menu do Debian (modo gráfico), crie o arquivo:

```bash
~/.local/share/applications/gerar-recibo.desktop
```

Conteúdo:

```ini
[Desktop Entry]
Name=Gerador de Recibo
Comment=Gera recibos de pagamento em PDF
Exec=/usr/local/bin/gerar-recibo
Icon=document-new
Terminal=true
Type=Application
Categories=Office;Finance;
```

Depois disso, ele aparecerá no menu como um app normal.
