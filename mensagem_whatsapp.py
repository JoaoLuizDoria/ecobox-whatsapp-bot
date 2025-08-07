# Script: mensagem_whatsapp.py
# Gera mensagens personalizadas com base no nome, cidade e status do lead


def gerar_mensagem(nome, cidade, status):
    if status == "proposta enviada":
        return f"Olá {nome}, tudo bem? Aqui é da Ecobox de Londrina. Vimos que você recebeu nossa proposta para instalação solar em {cidade}. Tem alguma dúvida ou podemos agendar uma visita técnica?"
    elif status == "aguardando resposta":
        return f"Oi {nome}, tudo certo? Só passando pra lembrar da proposta de energia solar que enviamos. Podemos conversar sobre ela ainda essa semana?"
    elif status == "fechado":
        return f"Parabéns {nome}! Sua economia com energia solar em {cidade} já está a caminho! A equipe da Ecobox está preparando tudo com carinho."
    else:
        return f"Olá {nome}, somos da Ecobox. Você gostaria de saber mais sobre como reduzir sua conta de luz com energia solar?"


# Exemplo de teste
print(gerar_mensagem("Carlos", "Cambé", "proposta enviada"))
