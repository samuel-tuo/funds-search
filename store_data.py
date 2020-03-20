import requests
import pymysql

token = 'DcROwZZkaH'
fund_code = '000001'
columns_names = ['code','name','type','net_worth','expect_worth','total_worth',
                 'expect_growth', 'day_growth', 'last_moth_growth', 'last_three_month_growth',
                 'last_six_month_growth', 'last_year_growth', 'buy_min', 'buy_source_rate',
                 'buy_rate', 'manager', 'fund_scale', 'worth_date', 'expect_worth_date',
                 'net_worth_data']
url = 'https://api.doctorxiong.club/v1/fund/detail?code={}&token={}'.format(fund_code, token)
response = requests.get(url).json()
#### 向数据库中写入数据
# 打开数据库(如数据库不存在会报错)
db = pymysql.connect(host = "localhost",
                            user = "root",
                            password = "xt25257758",
                            db = "funds_data",
                            port = 3306,
                            charset = 'utf8')
values = (response['data']['code'],
          response['data']['name'], response['data']['type'],
          response['data']['netWorth'], response['data']['expectWorth'],
          response['data']['totalWorth'], response['data']['expectGrowth'],
          response['data']['dayGrowth'], response['data']['lastMonthGrowth'],
          response['data']['lastThreeMonthGrowth'], response['data']
          ['lastSixMonthGrowth'],response['data']['lastYearGrowth'],
          response['data']['buyMin'],response['data']['buySourceRate'],
          response['data']['buyRate'], response['data']['manager'],
          response['data']['fundScale'],
          response['data']['worthDate'], response['data']['expectWorthDate'],
          str(response['data']['netWorthData']))

incert_funds_features = "INSERT INTO funds_features(code,name,type,net_worth,expect_worth,total_worth,expect_growth, day_growth,last_moth_growth, last_three_month_growth,last_six_month_growth,last_year_growth, buy_min, buy_source_rate,buy_rate, manager,fund_scale, worth_date, expect_worth_date,net_worth_data)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
# 使用cursor()方法创建一个游标对象
cursor = db.cursor()
# 使用execute()方法执行SQL语句
cursor.execute(incert_funds_features, values)


db.commit()
cursor.close()
db.close()
print('Done!')





