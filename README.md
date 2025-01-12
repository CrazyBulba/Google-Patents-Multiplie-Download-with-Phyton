# Google Patents Multiplie Download Script
Allow to download a multiplie patents from Google.Patents site

Script requires a Phyton ver >= 3.6

And installed modules:
1. requests_html
2. pyppeteer
3. wget
4. time

# How it works
1. Add list of patent-ID in the "input.txt" in format: one ID per line.
2. If it exists in Google.Patents database, the script will download it automatically.
3. All downloaded pdf-files will be saved to the "pdf" folder.
4. If the patent is unavailable or does't exist - relevant note will save into file "errors.txt"

At the first use, the chromium browser will be downloaded (~150 MB).
