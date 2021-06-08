from fuzzywuzzy import fuzz
import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def change_reg(reg, conn) :
    if fuzz.partial_ratio(reg.lower(), 'markmonitor')>=80 :
        return 'Markmonitor'

    if 'RU-CENTER' in reg :
        return 'RU-CENTER'

    if ',' in reg :
        reg =reg.split(",")[0]

    if ';' in reg :
        reg =reg.split(";")[0]

    if ' #' in reg :
        reg =reg.split(" #")[0]

    if 'd/b/a' in reg :
        reg = reg.split('d/b/a')[0]

    if 'dba ' in reg :
        reg = reg.split('dba ')[0]

    if ' DBA' in reg :
        reg = reg.split(' DBA')[0]

    if ' GmbH' in reg :
        reg = reg.split(' GmbH')[0]

    if ' Co.' in reg :
        reg = reg.split(' Co.')[0]

    if ' Ltd' in reg :
        reg = reg.split(' Ltd')[0]

    if ' SAS' in reg :
        reg = reg.split(' SAS')[0]

    if ' LLC' in reg :
        reg = reg.split(' LLC')[0]

    if '(http:' in reg :
        reg = reg.split('(http:')[0]

    if 'Inc.' in reg :
        reg = reg.split('Inc.')[0]

    if ' (Aust)' in reg :
        reg = reg.split(' (Aust)')[0]

    if ' S.A.S' in reg :
        reg = reg.split(' S.A.S')[0]

    if ' S.r.l.' in reg :
        reg = reg.split(' S.r.l.')[0]

    if ' s.r.l.' in reg :
        reg = reg.split(' s.r.l.')[0]

    if ' s.p.a.' in reg.lower() :
        reg = reg.split(' s.p.a.')[0]

    if ' sp.' in reg.lower() :
        reg = reg.split(' Sp.')[0]
    
    if ' S.A.' in reg :
        reg = reg.split(' S.A.')[0]

    if ' Pty' in reg :
        reg = reg.split(' Pty')[0]

    if ' (Pty)' in reg :
        reg = reg.split(' (Pty)')[0]

    if ' Limited' in reg :
        reg = reg.split(' Limited')[0]

    if ' LIMITED' in reg :
        reg = reg.split(' LIMITED')[0]

    if ' (www.' in reg :
        reg = reg.split(' (www.')[0]

    if ' INDONESIA' in reg :
        reg = reg.split(" INDONESIA")[0]

    if ' (PARIS)' in reg :
        reg = reg.split(" (PARIS)")[0]

    if ' (' in reg :
        reg = reg.split(" (")[0]

    if ' (Paris)' in reg :
        reg = reg.split(" (Paris)")[0]

    if '(Beijing)' in reg :
        reg = reg.split("(Beijing)")[0]

    if ' [Tag =' in reg :
        reg = reg.split(" [Tag =")[0]

    if 'alibaba' in reg.lower() :
        return 'Alibaba'

    if 'LEXSYNERGY' in reg :
        return 'Lexsynergy'

    if 'Beril Teknoloji' in reg :
        return 'Beril Teknoloji'

    if 'Megazone' in reg :
        return 'Megazone'

    if '101domain' in reg :
        return '101domain'

    if 'google' in reg.lower() :
        return 'Google'

    if 'domain name network' in reg.lower() :
        return 'Domain Name Network'

    if 'Çizgi' in reg :
        return 'Cizgi'

    if 'Amazon' in reg :
        return 'Amazon'

    if '1&1' in reg :
        return '1&1 IONOS'

    if 'Tucows' in reg :
        return 'Tucows'

    if 'İsimtescil' in reg :
        return 'Isimtescil'

    if 'GoDaddy' in reg :
        return 'GoDaddy'

    if 'Gandi' in reg :
        return 'Gandi'

    if 'Genious Communications' in reg :
        return 'Genious Communications'

    if 'NameSecure' in reg :
        return 'NameSecure'

    if '赛尔网络有限公司' in reg :
        return 'Purcell Network'

    if 'Atak Domain' in reg :
        return 'Atak Domain'

    if 'Hong Kong Domain' in reg :
        return 'Hong Kong Domain'

    if 'ong Kong Domain' in reg :
        return 'Hong Kong Domain'

    if '阿里云计算有限公司（万网）' in reg :
        return 'Alibaba'

    if '北京神州长城通信技术发展中心' in reg :
        return 'Alibaba'

    if 'ALIBABA' in reg :
        return 'Alibaba'

    if '阿里巴巴云计算（北京）有限公司' in reg :
        return 'Alibaba'

    if '成都西维数码科技有限公司' in reg :
        return 'Xiwei Digital '

    if '广东时代互联科技有限公司' in reg :
        return 'Guangdong Times '

    if '中企动力科技股份有限公司' in reg :
        return 'China Enterprise Power Technology'

    if '北京东方网景信息科技有限公司' in reg :
        return 'Oriental Netscape'

    if '易介集团北京有限公司' in reg :
        return 'Yijie Group'

    if '北京光速连通科贸有限公司' in reg :
        return 'Beijing Lightspeed Link Technology'

    if '商中在线科技股份有限公司' in reg :
        return 'Shangzhong Online Technology'

    if '北京国旭网络科技有限公司' in reg :
        return 'Guoxu Network'

    if '北京新网互联科技有限公司' in reg :
        return 'Xinwang Internet'

    if '遵义中域智科网络技术有限公司' in reg :
        return 'Zunyi Zhongyu Zhike'
    
    if '厦门' in reg :
        return 'Xiamen eName Technology'

    if '北京中科三方网络技术有限公司' in reg :
        return 'Zhongke Sanfang Network Technology'
    
    if '新网数码信息技术有限公司' in reg :
        return 'Xinwang Digital Technology'

    if '浙江贰贰网络有限公司' in reg :
        return 'Zhejiang Two Two Network'

    if '烟台帝思普网络科技有限公司' in reg :
        return 'Yantai Desp Network'

    if '上海美橙科技信息发展有限公司' in reg :
        return 'Shanghai Meicheng Technology Information'

    if 'eName ' in reg :
        return 'eName'

    if '广东金万邦科技投资有限公司' in reg :
        return 'Jinwanbang Technology'

    if 'abcdomain' in reg :
        return 'abcdomain'

    if fuzz.partial_ratio(reg[0:7], 'Xiamen')>=90 :
        return 'eName'

    if 'COM LAUDE' in reg :
        return 'Com Laude'

    if 'Com Laude' in reg :
        return 'Com Laude'

    if 'reg.ru' in reg.lower() :
        return 'reg.ru'
    
    if 'ODTÜ GELİŞTİRME VAKFI' in reg :
        return 'METU'

    if 'CSC' in reg :
        return 'Corporation Service Company'

    if 'Computer Service Langenbach' in reg :
        return 'Computer Service Langenbach'

    if 'Valtion tieto' in reg :
        return 'Valtion tieto'

    if '赛尔网络有限公司 ' in reg :
        return 'Purcell Network'
    
    if '成都飞数科技有限公司' in reg :
        return 'Chengdu Feisu'

    if '成都世纪东方网络通信有限公司' in reg :
        return 'Chengdu Century Eastern Network '

    if '郑州世纪创联电子科技开发有限公司' in reg :
        return 'Chuanglian Electronic Technology '

    if '北京万维通港科技有限公司' in reg :
        return 'Beijing Lightspeed Link Technology'

    if '深圳市万维网信息技术有限公司' in reg :
        return 'Shenzhen World Wide Web'

    if '广东互易网络知识产权有限公司' in reg :
        return 'Guangdong'
    
    if '重庆智佳信息科技有限公司' in reg :
        return 'Chongqing Zhijia Information Technology'

    if '天津追日科技发展有限公司' in reg :
        return 'Tianjin Zuri'
    
    if '杭州爱名网络有限公司' in reg :
        return 'Hangzhou'
    
    if 'Tianjin Zhuiri' in reg :
        return 'HTianjin Zhuiri'

    return reg

def delete_data(conn, d):

    sql = 'DELETE FROM data_registrar WHERE domain=?'
    cur = conn.cursor()
    cur.execute(sql, (d,))
    print(d, ' - deleted')
    conn.commit()

def select_all_data(conn):

    cur = conn.cursor()
    cur.execute("SELECT * FROM data_registrar")

    rows = cur.fetchall()

    for row in rows:
        
        reg = row[1]
        if(reg==''):
            delete_data(conn, row[0])
        else :
            reg1 = change_reg(reg, conn)
            if reg1 != reg :
                print(reg1, ' - ' , reg)
                data=(reg1,row[0])
                sql = ''' Update data_registrar set registrar = ? where domain = ?'''
                cur.execute(sql, data)
                conn.commit()

   

if __name__ == '__main__':
    print("Start")

    database = r"../pythonsqlite17000.db"

    # create a database connection
    conn = create_connection(database)

    with conn :
        select_all_data(conn)

    print("End")

    