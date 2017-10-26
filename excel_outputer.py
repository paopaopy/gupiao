# -*- coding: utf-8 -*-
from xlrd import open_workbook
from xlutils.copy import copy
import xlwt
import datetime

class ExcelOutput(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, gu_piao_dict):
        self.datas.append(gu_piao_dict)

    def write_excel(self, text_path):
        rexcel = open_workbook('持仓股票.xls')
        wexcel = copy(rexcel)
        if wexcel.get_sheet(str(datetime.date.today())) is None:
            wexcel.add_sheet(str(datetime.date.today()))
        worksheet = wexcel.get_sheet(str(datetime.date.today()))

        gu_piao_list = self.get_gu_piao_list()

        if text_path == '1_zhou.txt':
            for i in range(0, len(gu_piao_list)):
                worksheet.write(1 + i, 0, gu_piao_list[i])

        if text_path == '1_yue.txt':
            for i in range(0, len(gu_piao_list)):
                worksheet.write(1+i, 2, gu_piao_list[i])

        if text_path == '3_yue.txt':
            for i in range(0, len(gu_piao_list)):
                worksheet.write(1+i, 4, gu_piao_list[i])

        wexcel.save('持仓股票.xls')

    def get_gu_piao_list(self):
        gu_piao_list = set()
        for data in self.datas:
            old_list = eval(data['gu_piao'])
            for gu_piao in old_list:
                gu_piao_list.add(gu_piao)
        gu_piao_list = list(gu_piao_list)
        return gu_piao_list