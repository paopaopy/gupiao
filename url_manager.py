# -*- coding:utf-8 -*-
from selenium import webdriver

class UrlManager(object):



    def get_urls(self, text):
        file = open(text, 'r')
        urls = [line.strip() for line in file.readlines()]
        file.close()
        return urls



