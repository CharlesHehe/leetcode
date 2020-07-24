#
# import urllib.request
# from concurrent.futures import ThreadPoolExecutor
#
#
# urls = [
#     'http://www.python.org',
#     'https://docs.python.org/3/',
#     'https://docs.python.org/3/whatsnew/3.7.html',
#     'https://docs.python.org/3/tutorial/index.html',
#     'https://docs.python.org/3/library/index.html',
#     'https://docs.python.org/3/reference/index.html',
#     'https://docs.python.org/3/using/index.html',
#     'https://docs.python.org/3/howto/index.html',
#     'https://docs.python.org/3/installing/index.html',
#     'https://docs.python.org/3/distributing/index.html',
#     'https://docs.python.org/3/extending/index.html',
#     'https://docs.python.org/3/c-api/index.html',
#     'https://docs.python.org/3/faq/index.html'
# ]
#
#
# results = []
# for url in urls:
#     with urllib.request.urlopen(url) as src:
#         results.append(src)
#
# print(results)
import base64

s = "st3geoeojf"


print(base64.b64encode(bytes(s, 'utf-8')))
