# -*- coding:utf-8 -*-
import excel_outputer
import html_downloader
import html_outputer
import html_parser
import url_manager


class GuSpider(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        # download URL
        self.downloader = html_downloader.Downloader()
        self.parser = html_parser.Parser()
        self.outputer = html_outputer.Outputer()
        self.eoutputer = excel_outputer.ExcelOutput()


    def craw(self, text):
        #获取URl列表
        urls = self.urls.get_urls(text)
        for url in urls:
            gu_piao_dict = self.parser.parse(url)
            self.eoutputer.collect_data(gu_piao_dict)
        #self.eoutputer.write_excel(text)

        # if text == '1_zhou.txt':
        #     urls = self.urls.get_urls(text)
        # #执行单个URL循环
        #     for url in urls:
        #         gu_piao_dict = self.parser.parse(url)
        #         self.outputer.collect_data(gu_piao_dict)
        #     self.outputer.html_output_1_zhou(text)
        # if text == '1_yue.txt':
        #     urls = self.urls.get_urls(text)
        # #执行单个URL循环
        #     for url in urls:
        #         gu_piao_dict = self.parser.parse(url)
        #         self.outputer.collect_data(gu_piao_dict)
        #     self.outputer.html_output_1_yue(text)
        # if text == '3_yue.txt':
        #     urls = self.urls.get_urls(text)
        # #执行单个URL循环
        #     for url in urls:
        #         gu_piao_dict = self.parser.parse(url)
        #         self.outputer.collect_data(gu_piao_dict)
        #     self.outputer.html_output_3_yue(text)
        # if text == '6_yue.txt':
        #     urls = self.urls.get_urls(text)
        # #执行单个URL循环
        #     for url in urls:
        #         gu_piao_dict = self.parser.parse(url)
        #         self.outputer.collect_data(gu_piao_dict)
        #     self.outputer.html_output_6_yue(text)
        # if text == '1_nian.txt':
        #     urls = self.urls.get_urls(text)
        # #执行单个URL循环
        #     for url in urls:
        #         gu_piao_dict = self.parser.parse(url)
        #         self.outputer.collect_data(gu_piao_dict)
        #     self.outputer.html_output_6_yue(text)

# ,'3_yue.txt','6_yue.txt','1_nian.txt'
if __name__ == '__main__':
    text_path = ['1_zhou.txt', '1_yue.txt', '3_yue.txt']
    obj_spider = GuSpider()
    for text in text_path:
        obj_spider.craw(text)

