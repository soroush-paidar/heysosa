import os
upgradeq = input("Would you like to check pip and openai versions? If yes, input 'Y'. If not, input 'N'.")
if upgradeq.strip() == "Y":
  os.system("pip install --upgrade pip")
  os.system("pip install openai")
  os.system("pip install openai==0.28")
else:
  print("loading program")
import openai
from gtts import gTTS

openai.api_key = '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'

model_id = 'gpt-3.5-turbo'

def ChatGPT_conversation(conversation):
  response = openai.ChatCompletion.create(
    model=model_id,
    messages=conversation
  )

  conversation.append({'role': response.choices[0].message.role, 'content': response.choices[0].message.content})
  return conversation

conversation = []
conversation.append({'role': 'system', 'content': "You are an AI assistant."})
conversation = ChatGPT_conversation(conversation)
response = ('{0}: {1}\n'.format(conversation[-1]['role'].strip(), conversation[-1]['content'].strip()))
initial = (response.replace('assistant: ', ''))
print("Hey, I'm your personal assistant! What's up?")
tts = gTTS(text="Hey, I'm your personal assistant! What's up?", lang='en', tld='co.za')
tts.save("greeting.mp3")
os.system("start greeting.mp3")


while True:
  prompt = input("You: ")
  if prompt.strip() == "Print conversation.":
    print(conversation)
  elif prompt.strip() == "Release summary.":
    prompt = "Summarize what i've said in point form."
    conversation.append({'role': 'user', 'content': prompt})
    response = ('{0}: {1}\n'.format(conversation[-1]['role'].strip(), conversation[-1][prompt].strip()))
    final = (response.replace('assistant: ', ''))
    print(final)
  elif prompt.strip() == "Start thought synthesizer.":
    conversation.append({'role': 'user', 'content': 'I will type out my thoughts and I want you to memorize them. Do not respond with anything, just say "Noted." to show that you have acknowledged it. If you are ready, say "Ready."'})
  else:
    conversation.append({'role': 'user', 'content': prompt})
    conversation = ChatGPT_conversation(conversation)
    response = ('{0}: {1}\n'.format(conversation[-1]['role'].strip(), conversation[-1]['content'].strip()))
    final = (response.replace('assistant: ', ''))
    print(final)
    tts = gTTS(text=final, lang='en', tld='co.za')
    tts.save("response.mp3")
# to start the file from python
    os.system("start response.mp3")