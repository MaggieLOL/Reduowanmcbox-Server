# Re多玩我的世界盒子 - 联机盒子API文档

该api实现了获得房间列表,加入房间以及退出房间的功能.

## 1.获得房间列表

请求地址:http://101.43.48.113/api/onlinebox/main/onlineBoxApis.php?method=
参数列表:
method  固定值  getRoomList
返回格式:
Array
(
    [0] => .(无用值)
    [1] => ..(无用值)
    [2] => onlineBoxApis.php(无用值)
    [3] => 玩家1ip-is-房间名.flag
    [4] => 玩家2ip-is-房间名.flag
    ······
)

## 2.加入房间

请求地址:http://101.43.48.113/api/onlinebox/main/onlineBoxApis.php?method=&roomName=
参数列表:
method  固定值  craft
roomName 变量 房间名称
返回格式:
room is craft. 代表创建操作完成

## 3.退出房间

请求地址:http://101.43.48.113/api/onlinebox/main/onlineBoxApis.php?method=&roomName=
参数列表:
method  固定值  exitRoom
roomName 变量 房间名称
返回格式:
exit Over. 代表退出操作完成.

提示:务必使用 == 等于符而不是 in 来判断操作是否成功完成,因为在一些情况下 即使操作出现了问题也可能打印
包含操作正常完成字样的信息.