<?php

// Re多玩我的世界盒子 - 联机盒子部分
// 2022/11/5 该文件为api

$var1 = $_GET['method'];
$var2 = $_GET['roomName'];
$ip = (string)$_SERVER["REMOTE_ADDR"];
if($var2 != '' and $var1 == 'craft'){
    //开始创建房间
    $ip = (string)$_SERVER["REMOTE_ADDR"]."-is-".$var2.".flag"; //获得用户ip并加上.flag后辍
    $userFile = fopen($ip, "w");
    fwrite($userFile, 'userJohn');
    echo 'room is craft.';
}elseif($var1 == 'getRoomList'){
    //获取当前文件所在的绝对目录
    $dir =  dirname(__FILE__);
    //扫描文件夹
    $file = scandir($dir);
    //显示
    echo '<pre>';
    print_r($file);

}elseif($var1 == 'exitRoom'){
    $ip = (string)$_SERVER["REMOTE_ADDR"].$var2.".flag"; //获得用户ip并加上.flag后辍
    unlink($ip); //删除文件
    echo 'exit Over.'
}