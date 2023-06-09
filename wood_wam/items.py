# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose


def replace_space(text: str):
    return float(text.replace(' ', '')[:-3])


class WoodWamItem(scrapy.Item):
    product_id = scrapy.Field()
    product_url = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field(input_processor=MapCompose(str.strip, replace_space))
    category = scrapy.Field()
