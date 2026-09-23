from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-5",
    input="Explain software testing in simple English."
)

print(response.output_text)