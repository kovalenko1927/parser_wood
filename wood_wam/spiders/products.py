import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst

from wood_wam.items import WoodWamItem


class ProductsSpider(scrapy.Spider):
    name = "products"
    allowed_domains = ["www.wood-wam.in.ua"]
    start_urls = ["https://www.wood-wam.in.ua/shop/"]
    product_id = 0

    def parse(self, response, **kwargs):
        for number in range(1, 16):
            next_page = f"https://www.wood-wam.in.ua/shop/page/{number}/"
            yield response.follow(next_page, self.parse_product_link)

    def parse_product_link(self, response):
        for link in response.css('h2.woocommerce-loop-product__title a::attr(href)'):
            yield response.follow(link, self.parse_product)

    def parse_product(self, response):
        loader = ItemLoader(item=WoodWamItem(), selector=response)
        self.product_id += 1
        loader.default_output_processor = TakeFirst()
        loader.add_value('product_id', self.product_id)
        loader.add_value('product_url', response.url)
        loader.add_css('title', 'h1.product_title::text')
        price = response.css('div.summary span.amount::text').get()
        if price:
            loader.add_value('price', price)
        else:
            loader.add_value('price', "NO PRICE")
        category = response.css('div.summary li a::text').getall()[1]
        loader.add_value('category', category)
        yield loader.load_item()
