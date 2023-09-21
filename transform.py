from extract import users
import openai

openai.api_key = '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'
model = 'gpt-3.5-turbo'

def generate_ai_news(user):
    completion = openai.ChatCompletion.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": "Você é um especialista em markting bancário."
            },
            {
                "role": "user",
                "content": f"Crie uma mensagem para {user['name']} sobre a importância dos investimentos (máximo de 100 caracteres)"
            }
        ]
    )
    return completion.choices[0].message.content.strip('\"')
def generate_ai_win_pix(user):
    completion = openai.ChatCompletion.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": "Você é um especialista em markting bancário."
            },
            {
                "role": "user",
                "content": f"Crie uma mensagem para {user['name']} sobre premio em pix de 100 reais que o cliente ganhou e como investir o dinheiro (máximo de 100 caracteres)"
            }
        ]
    )
    return completion.choices[0].message.content.strip('\"')
def transform():
    for user in users:
        news = generate_ai_news(user)
        pix = generate_ai_win_pix(user)
        print(news)
        print(pix)
        user['features'].append({
            "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/pix.svg",
            "description": pix
        })
        user['news'].append({
            "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
            "description": news
        })
    print(users)