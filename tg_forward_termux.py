import asyncio
from pyrogram import Client

# Configuration
api_id = '22093899'  # Your Telegram API ID
api_hash = '562dc52e18df1a5912bd82598c1cfc4f'  # Your Telegram API hash
source_channel = 'porn626'  # The username or ID of the source channel
destination_channel = 'shdjdjdyzr'  # The ID of your destination channel
delay_seconds = 3  # Delay between each forwarded post in seconds

# Initialize the client
app = Client("my_account", api_id=api_id, api_hash=api_hash)

# Function to forward posts with links from source to destination
async def forward_posts_with_links():
    async with app:
        # Fetch all messages from the source channel
        async for message in app.get_chat_history(source_channel):
            # Check if the message contains text (assuming the link is within the text)
            if message.text:
                # Check if the text contains a link (you can improve this check based on your specific case)
                if "http" in message.text:
                    # Forward the post with the link to the destination channel
                    await app.send_message(
                        chat_id=destination_channel,
                        text=message.text,
                        disable_notification=True  # Optional: disable notifications
                    )
                    # Print a log
                    print(f"Forwarded post with link from {source_channel} to {destination_channel}")
                    # Wait for the specified delay
                    await asyncio.sleep(delay_seconds)

# Run the function
if __name__ == "__main__":
    asyncio.run(forward_posts_with_links())