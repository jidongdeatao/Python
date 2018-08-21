
如果解析页面parse_detail函数中有逻辑语句，或者想对爬取到的语句添加或做处理，
那么就需要用到这部分内容
在item.py文件中定义：

MapCompose可以传入函数对于该字段进行处理，而且可以传入多个

from scrapy.loader.processors import MapCompose
def add_mtianyan(value):
    return value+"-mtianyan"

 title = scrapy.Field(
        input_processor=MapCompose(lambda x:x+"mtianyan",add_mtianyan),
    )

注意：此处的自定义方法一定要写在代码前面。



create_date = scrapy.Field(
    input_processor=MapCompose(date_convert),
    output_processor=TakeFirst()
)

只取list中的第一个值。

自定义itemloader实现默认提取第一个
class ArticleItemLoader(ItemLoader):
    #自定义itemloader实现默认提取第一个
    default_output_processor = TakeFirst()



import scrapy
import datetime,re
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join

# 字符串转换时间方法
def date_convert(value):
    try:
        create_date = datetime.datetime.strptime(value, "%Y/%m/%d").date()
    except Exception as e:
        create_date = datetime.datetime.now().date()
    return create_date
# 获取字符串内数字方法
def get_nums(value):
    match_re = re.match(".*?(\d+).*", value)
    if match_re:
        nums = int(match_re.group(1))
    else:
        nums = 0
    return nums
# 去除标签中提取的评论方法
def remove_comment_tags(value):
    if "评论" in value:
        return ""
    else:
        return value
# 直接获取值方法
def return_value(value):
    return value




class ArticlespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

# 自定义itemloader实现默认取第一个值
class ArticleItemLoader(ItemLoader):
    default_output_processor = TakeFirst()

class JobBoleArticleItem(scrapy.Item):
    # front_image_url = scrapy.Field()
    # front_image_path = scrapy.Field()
    # title = scrapy.Field()
    # create_date = scrapy.Field()
    # url = scrapy.Field()
    # url_object_id = scrapy.Field()
    # praise_nums = scrapy.Field()
    # comment_nums = scrapy.Field()
    # fav_nums = scrapy.Field()
    # content = scrapy.Field()
    # tags = scrapy.Field()

    title = scrapy.Field()
    create_date = scrapy.Field(
        input_processor=MapCompose(date_convert),
    )
    url = scrapy.Field()
    url_object_id = scrapy.Field()
    front_image_url = scrapy.Field(
        # 使用自定义的outprocessor覆盖原始的take first 使得image_url是一个列表。
        output_processor=MapCompose(return_value)
    )
    front_image_path = scrapy.Field()
    #这样获取以下三个值可以共用get_nums方法
    praise_nums = scrapy.Field(
        input_processor=MapCompose(get_nums)
    )
    comment_nums = scrapy.Field(
        input_processor=MapCompose(get_nums)
    )
    fav_nums = scrapy.Field(
        input_processor=MapCompose(get_nums)
    )
    tags = scrapy.Field(
        input_processor=MapCompose(remove_comment_tags),
        # list使用逗号连接
        output_processor=Join(",")
    )
    content = scrapy.Field()
