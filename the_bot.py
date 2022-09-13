from telethon import TelegramClient
from telethon import TelegramClient, events
import text_extractor 


API_ID = input('Enter your API id, please: ')
API_HASH = input('Enter your API hash, please: ')


# Create the client and connect
client = TelegramClient('Text_extractor_bot', API_ID, API_HASH)
SENDER_GROUP = None
RECEIVING_GROUPS = []

def get_data():
    global SENDER_GROUP
    SENDER_GROUP = input('Enter the group ID which will send the images: (should start with - sign) ')
    n = input('How many groups would you like to send the extracted text? (Please enter a number): ')
    global RECEIVING_GROUPS
    for i in range(int(n)):
        RECEIVING_GROUPS.append(input(f"Enter group {i+1} id: (shouldn't start with - sign) "))

def main():
    get_data()
    client.start()
    client.run_until_disconnected()

@client.on(events.NewMessage)
async def new_message_sent(event):
    # check if it is the group we are interested in 
    if str(event.chat_id) == str(SENDER_GROUP):
        try:
            if event.media.photo:
                path = await event.download_media()
                text = text_extractor.get_text(path)
                if text != "No related coins detected":
                    print('sending to groups')
                    for group in RECEIVING_GROUPS:
                        await client.send_message(int(group), text)
                    print('done')
                else:
                    print("No related coins detected")
        except:
            print("texted entered, not a photo")

if __name__ == '__main__':
    main()

