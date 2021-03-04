from __future__ import annotations
import configparser
import os


def get_config() -> list[str]:
    """get options from config file"""
    config = configparser.ConfigParser()
    config.read("config.ini")

    api_keys: list[str] = []
    api_keys.append(config["KEYS"]["ConsumerKey"])
    api_keys.append(config["KEYS"]["ConsumerSecret"])

    # expand tilde to home path
    for key in api_keys:
        if key[0] == "~":
            api_keys[api_keys.index(key)] = os.path.expanduser(key)

    return api_keys


def read_keys(location: str) -> str:
    """get key values from locations"""
    with open(location) as file:
        value: str = file.read().strip()
    return value


# unload the keys to variable names for readability in main module
keys = get_config()
consumer_key: str = read_keys(keys[0])
consumer_secret: str = read_keys(keys[1])
del keys  # free up memory from keys, as values are unpacked

VERSION: str = "0.1.1"
