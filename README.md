# Facebook Open Redirect Tool   

### TL;DR

<img src="https://x42.obscurechannel.com/images/linkshim-fb.jpg"></img>

When you click on a non-Facebook link inside the platform, the site redirects the user through `https://l.facebook.com/l.php?u=<target url>`, which is part of their URL redirection system aka (<a href="https://www.facebook.com/whitehat/bugbounty-education/647477776391439/" target="_blank">Linkshim</a>). 

However, the site also generates these links from some of the footer links at the bottom of the main login page with a temporary (non "user-specific" hash).

<img src="https://x42.obscurechannel.com/images/facebook-open-redirect.jpg"></img>


This Python script utilizes the Playwright library to extract these temporary URLs and their associated encrypted `h=` parameter ("user-specific hash") values. By modifying the target destination but re-using the encrypted parameter value, we can generate a redirect URL valid for 15 minutes.

### **Caveats**

- If the user is already logged into Facebook, they might see a warning before being redirected.

- If they aren’t logged in, they’ll be redirected to the target site.


### Usage

Install playwright:
```bash
pip install playwright
```  

Run the script with your target URL:  
```bash
python get_redirect_url.py https://target-site.com
```  

Replace `https://target-site.com` with wherever you want the redirect to go.  

### What's the big deal?

<a href="https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html" target="_blank">Open redirects</a> can be used for phishing, social engineering, and in some cases, SSRF attacks.


### Disclaimer  

This tool is meant for educational and security research purposes, don't be dumb.

Download <a href="https://github.com/password-reset/facebook-open-redirect" target="_blank">here</a>
