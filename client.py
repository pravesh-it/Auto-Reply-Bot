from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:

client = OpenAI(
  api_key="<Your Key Here>",
)
command = '''
[6:18 PM, 7/30/2025] Tarun Verma GU: Pta ni viral hai kya hai h frse fever agya
[6:18 PM, 7/30/2025] Tarun Verma GU: Lekr aunga abhi thodi der m
[6:18 PM, 7/30/2025] Tarun Verma GU: Nai
[6:25 PM, 7/30/2025] Pravesh: Acha...
[6:25 PM, 7/30/2025] Pravesh: Check karwa le sale
[6:26 PM, 7/30/2025] Pravesh: Haan
[6:26 PM, 7/30/2025] Pravesh: Acha... Theek hai
[10:44 PM, 7/30/2025] Pravesh: Bhai 😂 bhej de usko rent main mujhko bol raha hai ki
[10:44 PM, 7/30/2025] Pravesh: Ground floor wale ko tight karo 😂
'''

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a person named pravesh who speaks hindi as well as english. You are from india and you are a coder. You analyze chat history and respond like a pravesh. Output should be the next chat response"},
    {"role": "user", "content": command}
  ]
)

print(completion.choices[0].message.content)