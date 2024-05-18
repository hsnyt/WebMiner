import scrapy


class EnvBasicSpider(scrapy.Spider):
    name = "env_basic"
    # spiderがアクセスできるドメイン
    allowed_domains = ["haonnoah.com"]
    # https:// である必要がある
    start_urls = ["http://haonnoah.com/"]


    # Google Chromeで確認したXPathやCSSセレクタを用いて情報の抽出を行う
    def parse(self, response):
        pass

    """
    例）
        def parse(self, response):
            books = response.xpath('//h3')
            # books = response.css('h3')
            yield {
                'books': books
            }
    """
