from __future__ import annotations
import argparse
import sys
from TwitterAPI import TwitterAPI, TwitterResponse
from censearch import consumer_key, consumer_secret


def get_variations(search_term: str) -> list[str]:
    """rotate a term through every iteration of
    a letter being censored by an asterisk
    """
    total: int = len(search_term)
    variations: list[str] = []
    for _ in range(total):
        variations.append(search_term.replace(search_term[_], "*"))
    return variations


def get_tweets(word_list: list[str]) -> list:
    """find tweets matching all terms in a list"""
    api: TwitterAPI = TwitterAPI(consumer_key, consumer_secret, auth_type="oAuth2")
    tweet_list: list = []
    for word in word_list:
        search: TwitterResponse = api.request("search/tweets", {"q": f"{word}"})
        if search and search.status_code == 200:
            tweet_list.append(search.json())
    return tweet_list


def parse_args() -> argparse.Namespace:
    """:"""
    parser = argparse.ArgumentParser()
    main_args = parser.add_argument_group()

    main_args.add_argument(
        "-s", "--search", help="phrase to search", type=str, required=True
    )
    # main_args.add_argument("-u", "--user", help="username to search", type=str)
    return parser.parse_args()


def main():
    """:"""
    args: argparse.Namespace = parse_args()
    search_term: str = args.search
    censored_words: list[str] = get_variations(search_term)
    tweet_list: list = get_tweets(censored_words)
    for block in tweet_list:
        num_tweets: int = len(block["statuses"])
        block = block["statuses"]
        for tweet in range(num_tweets):
            print(f"Tweet:\n{block[tweet]['text']}\n")


if __name__ == "__main__":
    main()
    sys.exit(0)
