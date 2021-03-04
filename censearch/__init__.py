from censearch.censearch_config import get_config

# keys[0] is public, key[1] is secret
keys = get_config("config.ini")
consumer_key: str = keys[0]
consumer_secret: str = keys[1]
del keys  # free up memory from keys, it's no longer needed

VERSION: str = "0.2.0"
