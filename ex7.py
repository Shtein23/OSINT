import requests
import re
from bs4 import BeautifulSoup

types_of_proxy = [['HTTP'], ['HTTPS'], ['SOCKS4'], ['SOCKS5']]


def get_proxy(types):
    for proxy_type in types:
        response = requests.post("https://www.proxyscan.io/Home/FilterResult/?status=1&ping=&selectedType=" +
                                 proxy_type[0] + "&sortPing=false&sortTime=true&sortUptime=false")
        site_proxies = BeautifulSoup(response.text, 'lxml')
        for proxy in site_proxies.select('tr'):
            proxy_type.append(proxy.th.text.strip() + ':' + proxy.td.text.strip())
        print(proxy_type)
    return types


def check_proxy(proxies_servers):
    http_txt = open('HTTP_proxy.txt', 'w')
    https_txt = open('HTTPS_proxy.txt', 'w')
    socks4_txt = open('SOCKS4_proxy.txt', 'w')
    socks5_txt = open('SOCKS5_proxy.txt', 'w')
    for proxy_servers in proxies_servers:
        if proxy_servers[0] == 'HTTP':
            print(proxy_servers[0])
            for http_proxy in proxy_servers:

                try:
                    r1 = requests.get('http://ifcfg.co', proxies={"http": http_proxy, "https": http_proxy}, timeout=5)
                    ip_list1 = re.findall(r'[0-9]+(?:\.[0-9]+){3}', http_proxy)[0]
                    ip_get1 = re.findall(r'[0-9]+(?:\.[0-9]+){3}', r1.text)[0]
                    if ip_list1 == ip_get1:
                        http_txt.write(http_proxy + "\n")
                except:
                    pass
            http_txt.close()
            print('Формирование списка HTTP proxy завершено - результаты в файле HTTP_proxy.txt ')
        elif proxy_servers[0] == 'HTTPS':
            print(proxy_servers[0])
            for https_proxy in proxy_servers:
                try:
                    r2 = requests.get('https://api.myip.com', proxies={"http": https_proxy, "https": https_proxy})
                    ip_list2 = re.findall(r'[0-9]+(?:\.[0-9]+){3}', https_proxy)[0]
                    ip_get2 = re.findall(r'[0-9]+(?:\.[0-9]+){3}', r2.text)[0]
                    if ip_list2 == ip_get2:
                        https_txt.write(r2.text + "\n")
                        print('zapisal')

                except:
                    pass
            https_txt.close()
            print('Формирование списка HTTPS proxy завершено - результаты в файле HTTPS_proxy.txt ')
        if proxy_servers[0] == 'SOCKS4':
            print(proxy_servers[0])
            for socks4_proxy in proxy_servers:
                try:
                    r3 = requests.get('https://api.myip.com', proxies={"http": "socks4://" + socks4_proxy,
                                                                       "https": "socks4://" + socks4_proxy})
                    ip_list3 = re.findall(r'[0-9]+(?:\.[0-9]+){3}', socks4_proxy)[0]
                    ip_get3 = re.findall(r'[0-9]+(?:\.[0-9]+){3}', r3.text)[0]
                    if ip_list3 == ip_get3:
                        socks4_txt.write(r3.text + "\n")
                        print('zapisal')

                except:
                    pass
            socks4_txt.close()
            print('Формирование списка SOCKS4 proxy завершено - результаты в файле SOCKS4_proxy.txt ')
        elif proxy_servers[0] == 'SOCKS5':
            print(proxy_servers[0])
            for socks5_proxy in proxy_servers:
                try:
                    r4 = requests.get('https://api.myip.com', proxies={"http": "socks5://" + socks5_proxy,
                                                                       "https": "socks5://" + socks5_proxy})
                    ip_list4 = re.findall(r'[0-9]+(?:\.[0-9]+){3}', socks5_proxy)[0]
                    ip_get4 = re.findall(r'[0-9]+(?:\.[0-9]+){3}', r4.text)[0]
                    if ip_list4 == ip_get4:
                        socks5_txt.write(r4.text + "\n")
                        print('zapisal')
                except:
                    pass
            socks5_txt.close()
            print('Формирование списка SOCKS5 proxy завершено - результаты в файле SOCKS5_proxy.txt ')
    print('Сканирование закончено')


lists_of_proxies = get_proxy(types_of_proxy)
check_proxy(lists_of_proxies)
