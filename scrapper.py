import requests
from bs4 import BeautifulSoup
import pandas as pd 


def get_html_page(url):

    script = '''
            headers = {
                ['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',
                ['cookie'] = 'DSID=AAO-7r4vZ98zMsbDZWLtUuKSjG30jZud1oI95aQdddQnO7PAq9QcK-3w5ePPU2P1Nm6Afaqwn9xzDB7MAalvR8f7zkiy8tdQ67PGwnHmh7JzdFx60hG7EkhxgdT814sS4_EsW4_89Jn5ofDhMG8ocKlsXJfHPsDfl1sA8gv99GK5Z21RXHGyth9TXdc449bKebjicaT8zP8cBH8hU1wuONOj7r0pSWt_3p_IiD8pP1pfapZ7h8k7SF8Ir-NtJtAOaYrIwAJcvB9p9OMyA9tA-dJ2O_KSdzTdHg; IDE=AHWqTUlGLl-sYGwleku3xPXnGiVUQ2rHiwvdytE41VInNfuXsy36Gt3RQm-yeiQrFT8'
            }
            splash:set_custom_headers(headers)
            splash.private_mode_enabled = false
            splash.images_enabled = false
            assert(splash:go(args.url))
            assert(splash:wait(1))
            return splash:html()
    '''

    html = requests.post(url='http://localhost:8050/run',
                                     json={
                                         'lua_source': script,
                                         'url': URL
                                     })
    
    return html

def top_50_crypto():
    
    # Requesting HTTP connection
    response = get_html_page(URL)
    
    # Creating soup object
    soup = BeautifulSoup(response.content, 'html.parser')
    
    #Extracting Top 10 crypto by market cap 
    results = soup.find('tbody').find_all('tr')[0:50]
    
    # Details container
    name = []
    ticker = []
    price = []
    marketcap = []
    supply = []
    volume = []
    
    # Name
    for result in results:
        name.append(result.find('p',{'class':'sc-1eb5slv-0 iworPT'}).get_text())
    
    # Ticker
    for result in results:
        ticker.append(result.find('p',{'class':'sc-1eb5slv-0 gGIpIK coin-item-symbol'}).get_text())
    
    # Price
    for result in results:
        price.append(result.find('div',{'class':'sc-131di3y-0 cLgOOr'}).get_text())
    
    # Market cap
    for result in results:
        marketcap.append(result.find('span',{'class':'sc-1ow4cwt-0 iosgXe'}).get_text())
    
    # Supply
    for result in results:
        supply.append(result.find('p',{'class':'sc-1eb5slv-0 kZlTnE'}).get_text())
    
    # 24h Volume traded
    for result in results:
        volume.append(result.find('p',{'class':'sc-1eb5slv-0 hykWbK font_weight_500'}).get_text())
    
    # Creating DataF=frame
    
    coin_details = pd.DataFrame({'Name': name, 'Symbol': ticker, 'Price': price, 'Market Cap': marketcap,
                                 'Circulating Supply': supply, '24H traded volume': volume})
    
    return coin_details

if __name__ == '__main__':
    url = 'https://coinmarketcap.com'
    output = top_50_crypto()
    print(output)
   
