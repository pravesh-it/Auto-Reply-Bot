import pyautogui
import time
import pyperclip
from openai import OpenAI

# OpenAi Support.
client = OpenAI(
  api_key="<Your Key Here>",
)


def is_last_message_from_sender(chat_log, sender_name="Tarun Verma GU"):
    # Split the chat log into individual messages
    messages = chat_log.strip().split("/2025] ")[-1]
    if sender_name in messages:
        return True 
    return False

# S1: Click on the whatsapp icon at coordinates (1209, 1049)
pyautogui.click(1209, 1049)
time.sleep(1) # Wait for 1 second to ensure that the click is registered.

while True:
    time.sleep(5)

    # S2: Drag the mouse form (679, 194) to (1877, 925) to select the text.
    pyautogui.moveTo(679, 194)
    pyautogui.dragTo(1877, 925, duration=2.0, button='left') # Drag for 1 second

    # S3: Copy the selected text to the clipboard.
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2) # Wait for 1 second to ensure the copy command is completed
    pyautogui.click(1277, 525)

    # S4: Retrieve the text from the clipboard and store it in a variable.
    chat_History = pyperclip.paste()

    # Print the copied text to verify.
    print(chat_History)
    print(is_last_message_from_sender(chat_History))
    if is_last_message_from_sender(chat_History):
        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a person named pravesh who speaks hindi as well as english. You are from india and you are a coder. You analyze chat history and respond like a pravesh. Output should be the next chat response (text message only"},
            {"role": "system", "content": "Do not start like this [11:02, 1/8/2025] Tarun Verma GU: "},
            {"role": "user", "content": chat_History}
            ]
            )

        response = completion.choices[0].message.content
        pyperclip.copy(response)

        # S5: Click at coordinates (1184, 974)
        pyautogui.click(1184, 974)
        time.sleep(1) # Wait for 1 second to ensure the click is registered

        # S6: Paste the text on chatbox.
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1) # Wait for 1 second to ensure the paste command is completed

        # S7: Press Enter
        pyautogui.press('enter')