import requests

print("📱 Ligando o aplicativo...")

# 1. O Celular faz o login para pegar a "pulseira" (Token)
url_login = "http://127.0.0.1:8000/api/token/"
dados_login = {
    "username": "Juliana",
    "password": "123456" #
}
resposta_login = requests.post(url_login, json=dados_login)
pulseira = resposta_login.json().get("access")

# 2. O Celular envia a resposta para o servidor
url_jogo = "http://127.0.0.1:8000/api/questions/1/answer/"
cabecalhos = {
    "Authorization": f"Bearer {pulseira}" # Mostrando a pulseira na portaria
}

# Na sua imagem anterior, vimos que o ID 3 era a resposta certa (R$ 100.000,00)
dados_resposta = {
    "choice_id": 3
}

print("Enviando a resposta para o servidor...\n")
resposta_jogo = requests.post(url_jogo, json=dados_resposta, headers=cabecalhos)

# 3. O Celular recebe o resultado e mostra na tela!
print("🎮 RESPOSTA DO SERVIDOR:")
import json
print(json.dumps(resposta_jogo.json(), indent=4, ensure_ascii=False))