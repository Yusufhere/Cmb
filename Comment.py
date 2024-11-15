import requests
import time
import random
import os
from colorama import init, Fore

init(autoreset=True)

def comment_bomber(tokens_file, target_post_id, comments_file, commenter_name, speed):
    # Token handling
    with open(tokens_file, "r") as file:
        tokens = file.readlines()

    # Comment handling
    with open(comments_file, "r") as file:
        comments = file.readlines()

    # Header setup
    headers = {
        "Connection": "keep-alive",
        "Cache-Control": "max-age=0",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": ("Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36"),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9,fr;q=0.8",
        "Referer": "(link unavailable)"
    }

    # Comment bombing loop
    while True:
        for comment_index, comment in enumerate(comments):
            token_index = comment_index % len(tokens)
            access_token = tokens[token_index].strip()
            full_comment = f"{commenter_name} {comment.strip()}"

            url = f"(link unavailable)"
            parameters = {"access_token": access_token, "message": full_comment}

            try:
                response = requests.post(url, json=parameters, headers=headers)
                response.raise_for_status()
                print(Fore.GREEN + f"[+] Comment {comment_index + 1} posted successfully!")
            except requests.exceptions.RequestException as e:
                print(Fore.RED + f"[x] Error posting comment {comment_index + 1}: {e}")

            time.sleep(speed)

def main():
    print(Fore.MAGENTA + "Welcome to Facebook Comment Bomber")
    print(Fore.CYAN + "------------------------------------")

    tokens_file = input(Fore.YELLOW + "Enter tokens file: ").strip()
    target_post_id = input(Fore.YELLOW + "Enter target post ID: ").strip()
    comments_file = input(Fore.YELLOW + "Enter comments file: ").strip()
    commenter_name = input(Fore.YELLOW + "Enter commenter name: ").strip()
    speed = float(input(Fore.YELLOW + "Enter speed (seconds): ").strip())

    comment_bomber(tokens_file, target_post_id, comments_file, commenter_name, speed)

if __name__ == "__main__":
    main()
