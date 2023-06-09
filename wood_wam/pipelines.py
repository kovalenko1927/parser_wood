# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv


class CSVPipeline:
    def open_spider(self, spider):
        self.file = open(f'{spider.name}.csv', 'w', newline='')
        self.writer = csv.writer(self.file)
        self.writer.writerow(['product_id', 'title', 'price', 'category', 'product_url'])

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        row = [item['product_id'], item['title'], item['price'], item['category'], item['product_url']]
        self.writer.writerow(row)
        return item
