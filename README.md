# Smart Store System
## Background
Recently, face recognition has become a hot topic, this project is aim to show a simple demonstration which use Python for face recognition and detection.
## Install
### python3.7
* PyMySQL
* PyQt5
* matplotlib
* pygal
* requests
* cv2
### Oracle MySQL

### Face++ Face Compare API
### Setup
* Execute build.bat to setup
1. double click buid.bat or input ```.\build.bat``` in console
2. add this command after bat statement if it's too slow.
```shell
--user -i http://mirrors.aliyun.com/pypi/simple/
```

* Face++ API
1. Go to [Face++](https://console.faceplusplus.com.cn/service/face) to get api key and secret
2. Copy to [Face.py](./Face.py) ```Your API key``` and ```Your API secret``` respectively.

* MySQL
1. Build MySQL Enviroment
2. Change the host name, port name, use id and password in the file [Database.py](Database.py) to yourself
```py
self.db = pymysql.connect(host = 'Your host address',user='Your user ID', passwd = 'Your password',db='Your database name',port = Your port number,charset='utf8')
```
3. Description of Database
[Customers.png](Customers.png)
[Flowrate.png](Flowrate.png)

##  Usage
This is a simple attempt to use Python for face recognition and detection with some other functions.
* Face Compare
1. Capture the picture first
2. Click search button to compare
3. Compare if exist a face in [.\Faces](.\Faces) Directory the same as the face in captured picture
4. Show the detailed information if exists, otherwise startup load information program, upload information of customer to MySQL database
* Face Detect
1. Detect how many faces in the left area of screen
2. Output the number of faces on GUI
* Other function
1. Settle accounts and upload to database
2. Query Information and show on GUI
3. Export customers flowrate data as a .txt file
4. Create chart of customers flowrate and export as .svg file

## Maintainers
[@Eclipse](https://github.com/928606496)

## Contributing

Feel free to dive in! [Open a issue](https://github.com/928606496/SmartStoreSystem/issues/new) or submit PRs.

## Lisence
[MIT](LICENSE) 