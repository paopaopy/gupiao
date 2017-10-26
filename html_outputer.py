# -*- coding:utf-8 -*-


class Outputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, gu_piao_dict):
        self.datas.append(gu_piao_dict)



    def html_output_1_zhou(self, text):

        # 写入html
        fout = open('1_zhou.html', 'w', encoding='utf-8')
        fout.write('<html>')
        fout.write('<head><meta http-equiv=\'content-type\' content=\'text/html;charset=utf-8\'></head>')
        fout.write('<body>')
        fout.write('<h1>一周排行榜</h1>')
        fout.write('<table>')
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['ji_jin'])
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['gu_piao'])
            fout.write("</tr>")
        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')

    def html_output_1_yue(self, text):


        fout = open('1_yue.html', 'w', encoding='utf-8')
        fout.write('<html>')
        fout.write('<head><meta http-equiv=\'content-type\' content=\'text/html;charset=utf-8\'></head>')
        fout.write('<body>')
        fout.write('<h1>一月排行榜</h1>')
        fout.write('<table>')
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['ji_jin'])
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['gu_piao'])
            fout.write("</tr>")
        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')

    def html_output_3_yue(self, text):
        fout = open('3_yue.html', 'w', encoding='utf-8')
        fout.write('<html>')
        fout.write('<head><meta http-equiv=\'content-type\' content=\'text/html;charset=utf-8\'></head>')
        fout.write('<body>')
        fout.write('<h1>三月排行榜</h1>')
        fout.write('<table>')
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['ji_jin'])
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['gu_piao'])
            fout.write("</tr>")
        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')

    def html_output_6_yue(self, text):
        fout = open('6_yue.html', 'w', encoding='utf-8')
        fout.write('<html>')
        fout.write('<head><meta http-equiv=\'content-type\' content=\'text/html;charset=utf-8\'></head>')
        fout.write('<body>')
        fout.write('<h1>六月排行榜</h1>')
        fout.write('<table>')
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['ji_jin'])
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['gu_piao'])
            fout.write("</tr>")
        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')

    def html_output_1_nian(self, text):
        fout = open('1_nian.html', 'w', encoding='utf-8')
        fout.write('<html>')
        fout.write('<head><meta http-equiv=\'content-type\' content=\'text/html;charset=utf-8\'></head>')
        fout.write('<body>')
        fout.write('<h1>一年排行榜</h1>')
        fout.write('<table>')
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['ji_jin'])
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['gu_piao'])
            fout.write("</tr>")
        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')


