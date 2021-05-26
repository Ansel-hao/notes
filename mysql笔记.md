# MYSQL
***
## MYSQL安装 or 连接
#### Ubuntu安装MYSQL服务
> 安装服务端：sudo aot-get install mysql-server
> 安装客户端：sudo apt-get install mysql-client
>> 配置文件：/etc/mysql
>> 命令集：/usr/bin
>> 数据库存储目录：/var/lib/mysql

#### Windows安装Mysql
> 下载MYSQL安装包（widndows）
>> [MYSQL下载] https://dev.mysql.com/downloads/mysql/

#### 启动和连接mysql服务
>服务端启动
>> 查看Mysql状态：sudo /etc/init.d/mysql status
>>启动服务：sodo /etc/init.d/mysql start | stop | restart

> 客户端连接
>> 命令格式
>>> mysql -h主机地址 -u用户名 -p密码
mysql -hlocalhost -uroot -p123456
本地连接可省略 -h 选项： mysql -uroot -p123456

## Mysql数据库操作
#### 数据库操作
* 查看已有库
> show databases; 

* 创建库（指定字符集）
> create database 库名 [character set utf8];
or
create database 库名 [charset=utf8];

* 查看创建数据库语句（字符集）
> show create database 库名；

>e.g. 查看stu创建方法
show create database stu;

* 查看当前数据库 
>select database();

*  切换库
> use 库名；

> e.g. 使用stu数据库
use stu;

* 删除库
> drop database 库名;

>e.g. 删除test数据库
drop database test;

#### 数据表的管理
1. 表结构设计初步
    * 确定存储内容
    * 确定字段构成
    * 确定字段类型
2. 数据类型支持
> 整型:
>> 整数类型（精确值） -INTEFETR，INT
>> 

| 类型 | 大小 | 范围（有符号）| 范围（无符号）| 用途 |
| :----: | :----: | :----: | :----: | :----: | 
| TINYINT | 1字节 | (-128,127) | (0,255) | 小整数值 |
| SMALLINT | 2字节 | (-32 768，32 767) | (0，65 535) | 大整数值 |
| MEDIUMINT | 3字节 | (-8 388 608，8 388 607) | (0，16 777 215) | 大整数值 |
| INT 或 INTEGER | 4字节 | (-2 147 483 648，2 147 483 647) | 	(0，4 294 967 295) | 大整数值 |
| BIGINT | 8字节 | (-9,223,372,036,854,775,808，9 223 372 036 854 775 807) | (0，18 446 744 073 709 551 615) | 极大整数值 |
| FLOAT | 4字节 | (-3.402 823 466 E+38，-1.175 494 351 E-38)，0，(1.175 494 351 E-38，3.402 823 466 351 E+38) | 0，(1.175 494 351 E-38，3.402 823 466 E+38) | 单精度 浮点数值 |
| DOUBLE | 8字节 | (-1.797 693 134 862 315 7 E+308，-2.225 073 858 507 201 4 E-308)，0，(2.225 073 858 507 201 4 E-308，1.797 693 134 862 315 7 E+308) | 0，(2.225 073 858 507 201 4 E-308，1.797 693 134 862 315 7 E+308) | 双精度 浮点数值 |
| DECIMAL | 对DECIMAL(M,D) | 依赖于M和D的值 | 	依赖于M和D的值 | 小数值 |

#### 日期和时间类型
>表示时间值的日期和时间类型为DATETIME、DATE、TIMESTAMP、TIME和YEAR。
每个时间类型有一个有效值范围和一个"零"值，当指定不合法的MySQL不能表示的值时使用"零"值。
TIMESTAMP类型有专有的自动更新特性，将在后面描述。

![](../img/日期和时间类型.png)

#### 字符串类型
> 字符串类型指CHAR、VARCHAR、BINARY、VARBINARY、BLOB、TEXT、ENUM和SET。该节描述了这些类型如何工作以及如何在查询中使用这些类型。

![](../img/字符串.png)

#### 数据的基本操作
##### 创建数据表
> CREATE TABLE table_name (column_name column_type);
>> e.g.
CREATE TABLE IF NOT EXISTS `runoob_tbl`(
   `runoob_id` INT UNSIGNED AUTO_INCREMENT,
   `runoob_title` VARCHAR(100) NOT NULL,
   `runoob_author` VARCHAR(40) NOT NULL,
   `submission_date` DATE,
   PRIMARY KEY ( `runoob_id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

##### 插入（insert）
> insert into 表名 values（值1），（值2），.....;
> insert into 表名 （, , , ,） values ('','',....)

##### 查询（select）
> select * from 表名； # 查询所有列 [where 条件]；
> select 字段1，字段名2 from 表名 [where 条件]；
>> e.g. 
>> select * from calss_1;
>> select name,age from calss_1;

##### where子句
> SELECT field1, field2,...fieldN FROM table_name1, table_name2...
[WHERE condition1 [AND [OR]] condition2.....

##### 更新(updata）
> UPDATE table_name SET field1=new-value1, field2=new-value2
[WHERE Clause]

##### 删除（delete）

> e.g. delete from calss_1 where id = 7

#### 表字段的操作（alter）
> 语法：alter table 表名 执行动作；
* 添加字段（add）
>> alter table 表名 add 字段名 数据类型；
alter table 表名 add 字段名 数据类型 first；
alter table 表名 add 字段名 数据类型 after 某字段 后；
* 删除字段（drop）
>> alter table 表名 drop 字段名；
* 修改数据类型（modify）
>> alter table 表名 modify 字段名 新数据类型
* 表重命名（rename）
>> alter table 表名 rename 新表名；

##### 时间类型数据
> 时间和日期类型：
>> date,Datetime和timestamp类型
>> time类型
>> year

###### 时间格式
> date:"yyyy-mm-dd"
> time:"hh:mm:ss"
> datetime:"yyyy-mm-dd hh:mm:ss"
> timestamp:"yyyy-mm-dd hh:mm:ss"
注意
1.datetime:不给值默认返回null值
2.timestamp:不给值默认返回系统当前时间

##### 日期时间函数
* now()返回服务器当前时间
* curdate()返回当前日期
* curtime()返回当前时间
* date(date)返回指定时间的日期
* time(date)返回指定时间的时间

#### 高级查询语句
##### 模糊查询和正则查询

* 使用 LIKE 子句从数据表中读取数据的通用语法：
>select field1,field2,...fieldN
from table_name
where field1 like condition1
e.g. 
mysql> select * from calss_1  where name like 'A%';

* mysql对正则表达式的支持有限，只支持部分正则元字符
> select field1,field2,...fieldN
from table_name
where field1 regexp condition1
e.g. 
mysql> select * from calss_1  where name regexp 'b.+';

##### 排序
> select field1,field2,...fieldN from table_namewhere field1 
order by condition1 [desc] <- : 加上desc为降序
e.g.
> select cbj from table_namewhere field1 
order by age

##### 联合查询
> select expression1, expression2,...expression_n
from tales
[where conditions]
UNION [ALL | DISTINCT]
> select expression1, expression2,...expression_n
from tales
[where conditions];

#### 数据备份
1. 备份命令格式
> mysqldump -u用户名 -p源库名 > ~/***.sql
>> --all-databases 备份所有库
库名 备份单个库
-B 库1 库2 库3 备份多个库
库名 表1 表2 表3 备份指定库的多张表
2. 恢复命令格式
> mysql -uroot -p 目标库名 < ***.sql
从所有库备份中恢复某一个库（--one-database）
>> mysqk -uroot -p --one-database 目标库名 < all.sql

#### pymysql使用流程
1. 建立数据库连接（db = pymysql.connect(...)）
2. 创建游标对象（c = db.cursor()）
3. 游标方法：c.execute("instert...")
4. 提交到数据库：db.commit()
5. 关闭游标对象：c.close()
6. 断开数据库连接：db.close()

#### 常用函数
> db = pymysql.connect(参数列表)
>> host:主机地址，本地localhost
port:端口号，默认3306
user：用户名
password：密码
database：库
charset：编码方式，推荐使用utf8
