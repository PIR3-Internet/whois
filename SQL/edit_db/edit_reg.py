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
    if ',' in reg :
        reg =reg.split(",")[0]

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

    if ' INDONESIA' in reg :
        reg = reg.split(" INDONESIA")[0]

    if ' (PARIS)' in reg :
        reg = reg.split(" (PARIS)")[0]

    if '(Beijing)' in reg :
        reg = reg.split("(Beijing)")[0]

    if ' [Tag =' in reg :
        reg = reg.split(" [Tag =")[0]

    if 'Alibaba' in reg :
        return 'Alibaba'

    if 'Beril Teknoloji' in reg :
        return 'Beril Teknoloji'

    if 'Megazone' in reg :
        return 'Megazone'

    if '101domain' in reg :
        return '101domain'

    if 'Amazon' in reg :
        return 'Amazon'

    if '1&1' in reg :
        return '1&1 IONOS'

    if 'Tucows' in reg :
        return 'Tucows'

    if 'GoDaddy' in reg :
        return 'GoDaddy'

    if 'Gandi' in reg :
        return 'Gandi'

    if 'Genious Communications' in reg :
        return 'Genious Communications'

    if 'NameSecure' in reg :
        return 'NameSecure'

    if 'Atak Domain' in reg :
        return 'Atak Domain'

    if 'Hong Kong Domain' in reg :
        return 'Hong Kong Domain'

    if '阿里云计算有限公司（万网）' in reg :
        return 'Alibaba'

    if '北京神州长城通信技术发展中心' in reg :
        return 'Alibaba'

    if '商中在线科技股份有限公司' in reg :
        return 'Shangzhong Online Technology'
    
    if '厦门' in reg :
        return 'Xiamen eName Technology'

    if '北京中科三方网络技术有限公司' in reg :
        return 'Zhongke Sanfang Network Technology'
    
    if '新网数码信息技术有限公司' in reg :
        return 'Xinwang Digital Technology'

    if fuzz.partial_ratio(reg[0:7], 'Xiamen')>=90 :
        return 'Xiamen eName Technology'

    if 'COM LAUDE' in reg :
        return 'Com Laude'

    if 'Com Laude' in reg :
        return 'Com Laude'
    
    if 'ODTÜ GELİŞTİRME VAKFI' in reg :
        return 'METU'

    if 'CSC' in reg :
        return 'Corporation Service Company'

    if 'Computer Service Langenbach' in reg :
        return 'Computer Service Langenbach'
    
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

    database = r"../pythonsqlite.db"

    # create a database connection
    conn = create_connection(database)

    with conn :
        select_all_data(conn)

    print("End")

    