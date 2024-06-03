from flask import *
import os, re, requests, random, string

app = Flask(__name__)

headers = {
  'User-Agent': "Mozilla/5.0 (Linux; Android 11; Infinix X6511B Build/RP1A.201005.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36",
  'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
  'Accept-Encoding': "gzip, deflate",
  'cache-control': "max-age=0",
  'upgrade-insecure-requests': "1",
  'dnt': "1",
  'save-data': "on",
  'x-requested-with': "mark.via.gp",
  'sec-fetch-site': "same-origin",
  'sec-fetch-mode': "navigate",
  'sec-fetch-user': "?1",
  'sec-fetch-dest': "document",
  'referer': "https://www.google.com/",
  'accept-language': "en-US,en;q=0.9"
}

@app.route("/")
def run_dood():
    url = request.args.get("")
    
    response = requests.get(url, headers=headers).text
    md = re.findall(f"\$\.get\(('/.*/.*?/.*?)'", response)
    print(md)
    return "Success"
    



if __name__ == "__main__":
    app.run()