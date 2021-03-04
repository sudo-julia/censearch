from pathlib import Path

key_dir = Path("~/lib/api_keys/twitter/censearch").expanduser()

with open(f"{key_dir}/consumer_key") as f:
    consumer_key: str = f.read().strip()

with open(f"{key_dir}/consumer_secret") as f:
    consumer_secret: str = f.read().strip()

VERSION = "0.1.1"
