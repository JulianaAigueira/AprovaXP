import requests
import json

print("📱 Ligando o aplicativo...")

# 1. O Celular faz o login para pegar a "pulseira" (Token)
url_login = "http://127.0.0.1:8000/api/token/"
dados_login = {
    "username": "Juliana",
    "password": "123456"
}
resposta_login = requests.post(url_login, json=dados_login)
pulseira = resposta_login.json().get("access")

# 2. O Celular pede a lista do Ranking
url_ranking = "http://127.0.0.1:8000/api/leaderboard/"
cabecalhos = {
    "Authorization": f"Bearer {pulseira}"
}

print("Buscando o Top 10...\n")
# Usamos GET aqui, pois queremos apenas LER a lista, não enviar nada
resposta_ranking = requests.get(url_ranking, headers=cabecalhos)

# 3. O Celular recebe o resultado e mostra o pódio na tela!
print("🏆 RANKING DOS JOGADORES:")
print(json.dumps(resposta_ranking.json(), indent=4, ensure_ascii=False))