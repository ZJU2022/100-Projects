'''
对于熟悉 CSS 选择器和 JavaScript 的开发者来说，
通过 CSS 选择器获取页面元素可能是更为简单的选择，
因为浏览器中运行的 JavaScript 本身就可以document对象的querySelector()和querySelectorAll()方法基于 
CSS 选择器获取页面元素。在 Python 中，我们可以利用三方库beautifulsoup4或pyquery来做同样的事情。
Beautiful Soup 可以用来解析 HTML 和 XML 文档，修复含有未闭合标签等错误的文档，通过为待解析的页面在内存中创建一棵树结构，
实现对从页面中提取数据操作的封装。可以用下面的命令来安装 Beautiful Soup。
'''

import bs4
import requests

for page in range(1, 11):
    resp = requests.get(
        url=f'https://movie.douban.com/top250?start={(page - 1) * 25}',
        headers={'User-Agent': 'BaiduSpider'}
    )
    # 创建BeautifulSoup对象
    soup = bs4.BeautifulSoup(resp.text, 'lxml')
    # 通过CSS选择器从页面中提取包含电影标题的span标签
    title_spans = soup.select('div.info > div.hd > a > span:nth-child(1)')
    # 通过CSS选择器从页面中提取包含电影评分的span标签
    rank_spans = soup.select('div.info > div.bd > div > span.rating_num')
    for title_span, rank_span in zip(title_spans, rank_spans):
        print(title_span.text, rank_span.text)