import asyncio
from pyrogram import Client

# Configuration
api_id = '22093899'  # Your Telegram API ID
api_hash = '562dc52e18df1a5912bd82598c1cfc4f'  # Your Telegram API hash
source_channel = 'porn626'  # The username or ID of the source channel
history_file = 'video_history.txt'  # File to store video history

# Initialize the client
app = Client("my_account", api_id=api_id, api_hash=api_hash)

# Function to fetch and save video history
async def fetch_and_save_video_history():
    async with app:
        # Open the history file in write mode
        with open(history_file, 'w') as file:
            # Fetch all messages from the source channel
            async for message in app.get_chat_history(source_channel):
                # Check if the message contains a video
                if message.video:
                    # Write video details to the file (file_id and caption)
                    file.write(f"{message.video.file_id},{message.caption}\n")
                    # Print a log
                    print(f"Saved video {message.video.file_id} to {history_file}")

# Run the function
if __name__ == "__main__":
    asyncio.run(fetch_and_save_video_history())
