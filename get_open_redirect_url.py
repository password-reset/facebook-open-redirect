from playwright.sync_api import sync_playwright
from urllib.parse import urlparse, parse_qs, urlencode
import sys

target_url = sys.argv[1]

with sync_playwright() as p:

	browser = p.chromium.launch(headless=True)
	page = browser.new_page()

	page.goto("https://www.facebook.com")

	redir_url = page.evaluate('''() => {
		let urls = [];
		document.querySelectorAll('*').forEach(element => {
			urls.push(element.src);
			urls.push(element.href);
			urls.push(element.url);
		});
		return [...new Set(urls.filter(url => url && url.includes('l.facebook.com/l.php')))];
		}''')

	parsed_url = urlparse(redir_url[0])
	query_dict = parse_qs(parsed_url.query)
	query_dict['u'] = [target_url]
	new_query = urlencode(query_dict, doseq=True)
	redir_link = parsed_url._replace(query=new_query).geturl()
	print(f"Temp redirect link expires in 15 min --> {redir_link}")
	browser.close()
