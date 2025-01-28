import requests
import time

# Constants
DOWNLOAD_SPEED = 200 * 1024  # 200 KB/s in bytes
CHUNK_SIZE = 1024  # 1 KB
URL = "https://dw.uptodown.net/dwn/flMXRx1RGw7FStwwbT5tU2WgJ0n-1eh-qzSC0MIYyE7fA2yE3h27I1CSu7-azHJv5TCedYntPnbYI9oFM3vZg6bDdQ2y-MDIZfJcYVsisJ1AIitqqYSxIW2qHqSnu2T5/0upFEa2-uAzq_1rTZRt4s7-lMpX4ammxzYA8iYoczpdi26gZfAhVrfwJSMOIF9S2VGEBoPOFlBgWXdNCa21toxVe111l39YAe2FQ1vsHQCSc4GVBePoXGPrW-iTS32f6/0sdd1vdyU482KT7-VDSaeAHAeAMzpn-mjfT2IfIb32xfs2VFWmq1vdXlbn8_Bpj_8gtk9lt_-WmMGORCnt3iIw==/pubg-mobile-3-5-0.apk"

def simulate_download():
    try:
        print(f"Simulating download at 200 KB/s...")
        with requests.get(URL, stream=True) as r:
            r.raise_for_status()
            total_downloaded = 0
            start_time = time.time()

            for chunk in r.iter_content(chunk_size=CHUNK_SIZE):
                if chunk:
                    total_downloaded += len(chunk)
                    elapsed_time = time.time() - start_time
                    expected_time = total_downloaded / DOWNLOAD_SPEED

                    if elapsed_time < expected_time:
                        # Sleep to throttle the download speed
                        time.sleep(expected_time - elapsed_time)

                    # Discard the chunk (do not save it)
                    del chunk

                    # Print progress
                    print(f"Downloaded: {total_downloaded / 1024:.2f} KB", end="\r")
    except KeyboardInterrupt:
        print("\nDownload simulation stopped.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    simulate_download()