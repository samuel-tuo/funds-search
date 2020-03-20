import pymysql

# 数据库信息



# 打开数据库(如数据库不存在会报错)
db = pymysql.connect(host = "localhost",
                            user = "root",
                            password = "xt25257758",
                            db = "funds_data",
                            port = 3306,
                            charset = 'utf8')
# 使用cursor()方法创建一个游标对象
cursor = db.cursor()
# 使用execute()方法执行SQL语句
# 确定数据表是否存在，存在立即删除
cursor.execute("DROP TABLE if exists funds_features")
#创建基金查询结果表
sql_create_fund_table = """CREATE TABLE funds_features(
                        id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
                        code VARCHAR(50) NOT NULL,
                        name  VARCHAR(255) NOT NULL ,
                        type  VARCHAR(100) NOT NULL ,
                        net_worth FLOAT  NOT NULL,
                        expect_worth FLOAT NOT NULL,
                        total_worth FLOAT NOT NULL,
                        expect_growth VARCHAR(50) NOT NULL,
                        day_growth VARCHAR(50) NOT NULL,
                        last_moth_growth VARCHAR(50) NOT NULL,
                        last_three_month_growth VARCHAR(50) NOT NULL,
                        last_six_month_growth VARCHAR(50) NOT NULL,
                        last_year_growth VARCHAR(50) NOT NULL,
                        buy_min FLOAT NOT NULL,
                        buy_source_rate FLOAT NOT NULL,
                        buy_rate FLOAT NOT NULL,
                        manager VARCHAR(100) NOT NULL,
                        fund_scale VARCHAR(100) NOT NULL,
                        worth_date DATE NOT NULL,
                        expect_worth_date DATETIME NOT NULL,
                        net_worth_data   MEDIUMTEXT NOT NULL                       
                        )"""
# 在execute里面执行SQL语句
cursor.execute(sql_create_fund_table)

db.commit()
cursor.close()
# 关闭数据库
db.close()
print('Done!')