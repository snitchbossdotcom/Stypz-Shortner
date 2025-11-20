import requests
import os

os.system("clear")
def shorten_url(long_url):
    api_url = "https://tinyurl.com/api-create.php"
    params = {"url": long_url}

    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()  # catch API errors
        return response.text
    except Exception as e:
        return f"Error: Contact Stypz Administrator for help"

def main():
    logo = "Stypz Shortener"
    print(logo)
    long_url = input("Enter a URL to shorten: ")

    short_url = shorten_url(long_url)
    print("\nShortened URL:", short_url)

def save_history(long_url, short_url):
    with open("history.txt", "a") as f:
        f.write(f"{long_url} -> {short_url}\n")

if __name__ == "__main__":
    main()
