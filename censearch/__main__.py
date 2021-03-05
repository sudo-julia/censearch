from __future__ import annotations
import argparse
import sys
from TwitterAPI import TwitterAPI, TwitterResponse
from censearch import consumer_key, consumer_secret
from censearch.censearch_args import parse_args


def get_variations(search_term: str) -> list[str]:
    """rotate a term through every iteration of
    a letter being censored by an asterisk.
    the first and last letters are skipped, as those usually aren't censored
    """
    total: int = len(search_term) - 1
    variations: list[str] = []
    for _ in range(1, total):
        variations.append(search_term.replace(search_term[_], "*", 1))
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


def display_tweets(tweet_list: list, words: list[str]):
    """display the collected tweets"""
    block_num: int = 0
    for block in tweet_list:
        block = block["statuses"]
        num_tweets: int = len(block)
        print("-" * 80)
        print(f"\nSearch phrase: '{words[block_num]}'")
        for tweet in range(num_tweets):
            author: str = block[tweet]["user"]["screen_name"]
            tweet_id: str = block[tweet]["id_str"]
            url: str = f"https://twitter.com/{author}/status/{tweet_id}"
            print(f"\nTweet {tweet + 1}:\n{block[tweet]['text']} - @{author}")
            print(f"{url}")
        block_num += 1
    print("-" * 80)


def main():
    """:"""
    args: argparse.Namespace = parse_args()
    search_term: str = args.search
    underline: int = 0

    censored_words: list[str] = get_variations(search_term)
    startup_msg: str = "Grabbing tweets with search terms:"
    print(startup_msg, *censored_words)
    # get the number of characters in startup_msg + list items to format an underline
    for word in censored_words:
        underline += len(word) + 1
    underline += len(startup_msg)
    print("=" * underline)
    del startup_msg, underline
    tweet_list: list = get_tweets(censored_words)
    display_tweets(tweet_list, censored_words)


if __name__ == "__main__":
    main()
    sys.exit(0)
