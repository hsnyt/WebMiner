import scrapy

class EnvBasicSpider(scrapy.Spider):
    name = "env_basic"
    allowed_domains = ["webscraper.io"]
    start_urls = ["https://webscraper.io/test-sites"]

    def parse(self, response):
        # すべてのh1タグのテキストを抽出
        h1_tags = response.xpath('//h1/text()').getall()

        # すべてのリンクを抽出
        links = response.xpath('//a/@href').getall()

        # 一つのアイテムとして抽出した情報を辞書にまとめてyieldする
        yield {
            'h1_tags': h1_tags,
            'links': links
        }


    """
    例）
        def parse(self, response):
            books = response.xpath('//h3')
            # books = response.css('h3')
            yield {
                'books': books
            }
    """
