import time
import asyncio
from pyrogram import Client

# Configuration
api_id = '22093899'  # Your Telegram API ID
api_hash = '562dc52e18df1a5912bd82598c1cfc4f'  # Your Telegram API hash
source_channel = 'porn626'  # The username or ID of the source channel
destination_channel = 'shdjdjdyzr'  # The ID of your destination channel
delay_seconds = 3  # Delay between each forwarded video in seconds

# Initialize the client
app = Client("my_account", api_id=api_id, api_hash=api_hash)

# Function to forward videos from source to destination
async def forward_videos():
    async with app:
        # List to store all messages
        all_messages = []
        
        # Fetch all messages from the source channel
        async for message in app.get_chat_history(source_channel):
            all_messages.append(message)
        
        # Process messages in reverse order (from first to last)
        for message in reversed(all_messages):
            # Check if the message contains a video
            if message.video:
                # Forward the video to the destination channel without sender's name
                await app.send_video(
                    chat_id=destination_channel,
                    video=message.video.file_id,
                    caption=message.caption  # Forward the caption if any
                )
                # Print a log
                print(f"Forwarded video {message.video.file_id} to {destination_channel}")
                # Wait for the specified delay
                await asyncio.sleep(delay_seconds)

# Run the function
if __name__ == "__main__":
    asyncio.run(forward_videos())