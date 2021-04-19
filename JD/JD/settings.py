# Scrapy settings for JD project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'JD'

SPIDER_MODULES = ['JD.spiders']
NEWSPIDER_MODULE = 'JD.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',

    'Cookie': '__jdu=15996523783091221593093; shshshfpa=e866d765-c61e-cff6-21a9-c1a9fd882724-1599652386; shshshfpb=rKZq97iyLStQI18g5sYVOgA%3D%3D; areaId=11; unpl=V2_ZzNtbRVeREAhChIGeEleV2IFG1hLAEsUdgEUXC5JWQBmBRoPclRCFnUUR1ZnG1wUZwMZXEdcQRBFCEdkeBBVAWMDE1VGZxBFLV0CFSNGF1wjU00zQwBBQHcJFF0uSgwDYgcaDhFTQEJ2XBVQL0oMDDdRFAhyZ0AVRQhHZHsdVA1gBxFfRF5BFH0IRVd7HVQHZgsQbXJQcyVFD0ZQchxbNWYzE20AAx8ddApFV3NUXAFvCxVZQVVFHHcJTlR4GlwBbwETVUBnQiV2; __jdv=76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_f86de3ec2a3c47848f9028c9da44079c|1617159877726; PCSYCityID=CN_150000_150500_150502; __jdc=122270672; shshshfp=53347a8aaf6a5aad7169d401bca9c04c; ipLoc-djd=11-902-32769-58182; jwotest_product=99; __jda=122270672.15996523783091221593093.1599652378.1617159878.1617165532.8; user-key=283d199f-2761-4456-be78-c97bc70c233f; wlfstk_smdl=ereivwsixgj33qe7m5lvgnrheqmb2xeg; mt_xid=V2_52007VwMWWlVfVlkdTxBeBG8DEVFdXFpYHkEbbFZuAxAGDV9TRhtLHlUZYgFHVkEIUl1MVUlZUmEFQFtcWQddGHkaXQZnHxNQQVpSSx9LEl4CbAYaYl9oUmodTBpaAW8DFVNYaFJcG00%3D; JSESSIONID=44C73C89987F81017517AB581264B28C.s1; 3AB9D23F7A4B3C9B=6IPO4T3X67SQDX3MVI75LS7QR6X6TX2DXOB6CGIWOXYCULF7KSRK62BMYQ7HOZMZ67HYEYOEIPE77EQXH2BJ7Q6OTQ; shshshsID=f6b9fb41ef7e1bdac7129eb3f79223e9_17_1617172759753; __jdb=122270672.20.15996523783091221593093|8.1617165532',

    'Referer': 'https://item.jd.com/'


}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'JD.middlewares.JdSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'JD.middlewares.JdDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'JD.pipelines.JdPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
