from urllib.request import urlopen
import ssl

context = ssl._create_unverified_context()

link = 'https://www.naver.com/'


def get_html():
    try:
        http_rsp = urlopen(link, context=context)
        print(http_rsp)
        html = http_rsp.read()
        print(html)
        html_decoded = html.decode()
        print(html_decoded)
    except Exception as ex:
        print('*** Failed to get Html! ***\n\n' + str(ex))
    else:
        return html_decoded


if __name__ == '__main__':
    get_html()
