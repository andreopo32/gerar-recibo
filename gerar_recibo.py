#!/usr/bin/env python3
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from datetime import datetime
import re


def formatar_cpf_cnpj(documento):
    """Detecta se é CPF ou CNPJ e formata automaticamente."""
    numeros = re.sub(r'\D', '', documento)
    if len(numeros) == 11:
        return f"CPF: {numeros[:3]}.{numeros[3:6]}.{numeros[6:9]}-{numeros[9:]}"
    elif len(numeros) == 14:
        return f"CNPJ: {numeros[:2]}.{numeros[2:5]}.{numeros[5:8]}/{numeros[8:12]}-{numeros[12:]}"
    else:
        return f"CNPJ/CPF: {documento}"


def gerar_recibo(nome_cliente, doc_cliente, servico, valor, forma_pagamento, data_pagamento=None, emissor="André Oliveira - Serviços de Informática"):
    if data_pagamento is None:
        data_pagamento = datetime.now().strftime("%d/%m/%Y")

    nome_arquivo = f"Recibo - {nome_cliente} - {data_pagamento.replace('/', '-')}.pdf"
    doc = SimpleDocTemplate(nome_arquivo, pagesize=A4, rightMargin=30, leftMargin=30, topMargin=30, bottomMargin=30)

    estilos = getSampleStyleSheet()
    estilo_negrito = ParagraphStyle(name="Negrito", parent=estilos["Normal"], fontName="Helvetica-Bold")

    conteudo = []

    # Cabeçalho
    titulo = Paragraph("RECIBO DE PAGAMENTO", estilos["Title"])
    conteudo.append(titulo)
    conteudo.append(Spacer(1, 12))

    # Tabela de dados
    dados = [
        ["Recebemos de", nome_cliente],
        ["Documento", doc_cliente],
        ["Referente a", servico],
        ["Valor", f"R$ {valor:.2f}".replace('.', ',')],
        ["Forma de pagamento", forma_pagamento],
        ["Data do pagamento", data_pagamento]
    ]

    tabela = Table(dados, colWidths=[60*mm, 110*mm])
    tabela.setStyle(TableStyle([
        ('BOX', (0, 0), (-1, -1), 1, colors.black),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('BACKGROUND', (0, 0), (-1, 0), colors.whitesmoke),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ]))
    conteudo.append(tabela)
    conteudo.append(Spacer(1, 20))

    # Texto final
    texto_final = (
        f"Declaramos para os devidos fins que recebemos de. <b>{nome_cliente}</b> "
        f"({doc_cliente}) o valor de <b>R$ {valor:.2f}</b> "
        f"({forma_pagamento.lower()}) referente a <b>{servico}</b>.<br/><br/>"
        "Local e data: _______________________________<br/><br/>"
        "Assinatura: _______________________________<br/><br/>"
        f"<b>{emissor}</b>"
    )
    conteudo.append(Paragraph(texto_final, estilos["BodyText"]))

    doc.build(conteudo)
    print(f"\n✅ Recibo gerado com sucesso: {nome_arquivo}\n")


def escolher_forma_pagamento():
    """Menu numérico para escolher forma de pagamento."""
    opcoes = {
        "1": "PIX",
        "2": "Dinheiro",
        "3": "Cartão",
        "4": "Transferência",
        "5": "Outro"
    }

    print("\n=== Escolha a forma de pagamento ===")
    for k, v in opcoes.items():
        print(f"{k} = {v}")

    while True:
        escolha = input("Digite o número da opção: ").strip()
        if escolha in opcoes:
            if escolha == "5":
                return input("Digite a forma de pagamento personalizada: ").strip()
            return opcoes[escolha]
        print("❌ Opção inválida. Escolha um número entre 1 e 5.")


def main():
    print("=== GERADOR DE RECIBO DE PAGAMENTO ===\n")

    nome_cliente = input("Nome do cliente: ").strip()
    documento_raw = input("CNPJ/CPF do cliente (pode digitar só números): ").strip()
    doc_cliente = formatar_cpf_cnpj(documento_raw)

    servico = input("Serviço prestado: ").strip()

    while True:
        try:
            valor = float(input("Valor (ex: 150 ou 150.50): ").replace(',', '.'))
            break
        except ValueError:
            print("❌ Valor inválido. Tente novamente.")

    forma_pagamento = escolher_forma_pagamento()

    data_pagamento = input("Data do pagamento (dd/mm/aaaa) [pressione Enter para hoje]: ").strip()
    if not data_pagamento:
        data_pagamento = datetime.now().strftime("%d/%m/%Y")

    emissor = input("Nome do emissor [padrão: André Oliveira - Serviços de Informática]: ").strip()
    if not emissor:
        emissor = "André Oliveira - Serviços de Informática"

    gerar_recibo(nome_cliente, doc_cliente, servico, valor, forma_pagamento, data_pagamento, emissor)


if __name__ == "__main__":
    main()
