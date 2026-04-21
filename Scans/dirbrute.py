import sys

import requests

def brute(url, wordlist):
    for word in wordlist:
        try:
            url_final = f"{url}/{word}".strip()
            response = requests.get(url_final)
            if response.status_code != 404:

                print(f"{url_final} -- {response.status_code}")
        except KeyboardInterrupt:
            sys.exit(0)
        except:
            pass

if __name__ == "__main__":
    url = sys.argv[1]
    wordlist = sys.argv[2]

    with open(wordlist, "r") as file:
        wordlist = file.readlines()

    brute(url, wordlist)