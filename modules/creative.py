import openai
import os

class ContentAI:
    def __init__(self):
        self.client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def generate_plan(self, niche):
        prompt = f"Создай контент-план на 30 дней для ниши: {niche}. Верни в формате JSON."
        response = self.client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

    def generate_article(self, topic):
        prompt = f"Напиши SEO-статью на 1200 слов на тему: {topic}. Используй H1, H2, списки и таблицы."
        response = self.client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
