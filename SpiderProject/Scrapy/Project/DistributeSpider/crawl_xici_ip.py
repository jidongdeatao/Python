# _*_ coding: utf-8 _*_
import requests
from scrapy.selector import Selector
import MySQLdb

conn = MySQLdb.connect('127.0.0.1', 'root', '123212', 'spider_a', charset="utf8", use_unicode=True)
cursor = conn.cursor()

def crawl_ips():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0"}
    for i in range(1,10):
        re = requests.get("http://www.xicidaili.com/nn/{0}".format(i), headers=headers)
        selector = Selector(text=re.text)
        all_trs = selector.css("#ip_list tr")

        ip_list = []
        for tr in all_trs[1:]:
            speed_str = tr.css(".bar::attr(title)").extract()[0]
            if speed_str:
                speed = float(speed_str.split("秒")[0])
            all_texts = tr.css("td::text").extract()

            ip = all_texts[0]
            port = all_texts[1]
            proxy_type = all_texts[5]

            ip_list.append((ip, port, proxy_type, speed))

    for ip_info in ip_list:
        try:
            cursor.execute(
                "insert into proxy_ip(ip, port,proxy_type, speed ) VALUES('{0}', '{1}', '{2}', '{3}')".format(
                    ip_info[0], ip_info[1], ip_info[2],ip_info[3]
                )
            )

            conn.commit()
        except Exception as e:
            print("将爬取到到IP保存到数据库中有误 " + e)


class Get_IP(object):

    #从数据库中提取Ip
    def get_random_ip(self):
        #从数据库中随机提取一个ip和对应掉端口
        random_sql  = """
        SELECT ip, port,proxy_type FROM proxy_ip ORDER BY RAND() LIMIT 1
        """
        result = cursor.execute(random_sql)
        for ip_info in cursor.fetchall():
            ip = ip_info[0]
            port = ip_info[1]
            proxy_type = ip_info[2].lower()
            judge_re = self.check_ip(ip, port,proxy_type)
            if judge_re:
                return "{2}://{0}:{1}".format(ip, port,proxy_type)
            else:
                return self.get_random_ip()

    #检查Ip是否可用
    def check_ip(self,ip,port,proxy_type):
        #判断ip是否可用
        http_url = "http://www.baidu.com"
        proxy_url = "http://{0}:{1}".format(ip, port)
        headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
        }

        try:
            proxy_dict = {
                proxy_type:proxy_url,
            }
            response = requests.get(http_url, proxies=proxy_dict,headers=headers,timeout =5 )
            code = response.status_code
            if code >= 200 and code < 300:
                print("effective ip：%s"%proxy_url)
                return True
            else:
                print("invalid ip and port")
                self.delete_ip(ip)
                return False

        except Exception as e:
            print ("invalid ip and port")
            self.delete_ip(ip)
            return False


    def delete_ip(self, ip):
        # 从数据库中删除随机提取的无用的ip
        try:
            cursor.execute("DELETE FROM proxy_ip WHERE ip = '{0}'".format(ip))
            conn.commit()
        except Exception as e:
            print("删除随机提取的无用的ip有误 :" + e)


#关闭数据库连接
def close_mysql():
    try:
        cursor.close()
        conn.close()
    except Exception as e:
        print(e)

if __name__ == "__main__" :
    # crawl_ips()
    M = Get_IP()
    print(M.get_random_ip())
    close_mysql()
