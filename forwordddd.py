import asyncio
from pyrogram import Client

# Configuration
api_id = '22093899'  # Your Telegram API ID
api_hash = '562dc52e18df1a5912bd82598c1cfc4f'  # Your Telegram API hash
destination_channel = 'shdjdjdyzr'  # The ID of your destination channel
history_file = 'video_history.txt'  # File containing saved video history

# Initialize the client
app = Client("my_account", api_id=api_id, api_hash=api_hash)

# Function to forward videos based on saved history
async def forward_saved_videos():
    async with app:
        # Open the history file in read mode
        with open(history_file, 'r') as file:
            # Read each line (each line is in the format file_id,caption)
            for line in file:
                # Split the line to extract file_id and caption
                file_id, caption = line.strip().split(',')
                # Forward the video to the destination channel
                await app.send_video(
                    chat_id=destination_channel,
                    video=file_id,
                    caption=caption if caption != "None" else None
                )
                # Print a log
                print(f"Forwarded video {file_id} to {destination_channel}")
                # Optionally add a delay between each forwarded video
                await asyncio.sleep(3)  # Adjust delay as needed

# Run the function
if __name__ == "__main__":
    asyncio.run(forward_saved_videos())