# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyredistestItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title_name = scrapy.Field()
    pub_date = scrapy.Field()
    prave_num = scrapy.Field()
    fav_nums = scrapy.Field()
    comment_num = scrapy.Field()
    tags = scrapy.Field()
    from_image_url = scrapy.Field()
    from_image_path = scrapy.Field()
    url = scrapy.Field()
    url_object_id = scrapy.Field()
