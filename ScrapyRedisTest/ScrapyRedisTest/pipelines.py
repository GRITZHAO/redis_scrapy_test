# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exporters import JsonItemExporter
import codecs
import json


class ScrapyredistestPipeline(object):
    def process_item(self, item, spider):

        return item

# 获取图片
class ArticalImagePipline(ImagesPipeline):
    def item_completed(self, results, item, info):
        for ok, value in results:
            image_file_path = value['path']
        item['from_image_path'] = image_file_path

        return item


class JsonWithEncodingPipeline(object):
    def __init__(self):
        self.file = codecs.open('artical.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        lines = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(lines)
        return item

    def spider_close(self,spider):
        self.file.close()
