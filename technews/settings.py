BOT_NAME = "technews"

SPIDER_MODULES = ["technews.spiders"]
NEWSPIDER_MODULE = "technews.spiders"

ROBOTSTXT_OBEY = False

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"


