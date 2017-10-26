# -*- coding:utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

class Parser(object):
    def parse(self, url):
        gu_piao_dict = {}
        gu_piaos = []
        response = urlopen(url)
        soup = BeautifulSoup(response.read(), 'html.parser')
        ji_jin_title = soup.find(class_="fundDetail-tit").get_text()
        tds = soup.find(id="quotationItem_DataTable").findAll('a', href = re.compile(r'^(http://quote.eastmoney.com)'))
        for td in tds:
            gu_piao_name = td.get_text()
            gu_piaos.append(gu_piao_name)

        gu_piao_dict['ji_jin'] = str(ji_jin_title)
        gu_piao_dict['url'] = str(url)
        gu_piao_dict['gu_piao'] = str(gu_piaos)

        return gu_piao_dict
