# Scrapy settings for scrapy1 project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'scrapy1'

SPIDER_MODULES = ['scrapy1.spiders']
NEWSPIDER_MODULE = 'scrapy1.spiders'
FEED_EXPORTERS_BASE = {
'json': 'scrapy.contrib.exporter.JsonItemExporter',
'jsonlines': 'scrapy.contrib.exporter.JsonLinesItemExporter',
'csv': 'scrapy.contrib.exporter.CsvItemExporter',
'xml': 'scrapy.contrib.exporter.XmlItemExporter',
'marshal': 'scrapy.contrib.exporter.MarshalItemExporter',
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'scrapy1 (+http://localhost:6080)'
