import asyncio
from pyrogram import Client


# Configuration
api_id = '22093899'  # Your Telegram API ID
api_hash = '562dc52e18df1a5912bd82598c1cfc4f'  # Your Telegram API hash
source_channel = 'porn626'  # The username or ID of the source channel


# Initialize the client
app = Client("my_account", api_id=api_id, api_hash=api_hash)

async def get_file_id():
    async with app:
        try:
            async for message in app.search_messages(source_channel, filter="video"):
                if message.video:
                    file_id = message.video.file_id
                    return file_id
            print(f"No video found in {source_channel}")
            return None
        except Exception as e:
            print(f"Error fetching messages: {e}")
            return None

async def main():
    try:
        file_id = await get_file_id()
        if file_id:
            print(f"File ID of the video in {source_channel}: {file_id}")
            # Save file_id to a file named 'video.file_id'
            with open('video.file_id', 'w') as file:
                file.write(file_id)
        else:
            print(f"No video found in {source_channel}")
    finally:
        await app.stop()

if __name__ == "__main__":
    asyncio.run(main())