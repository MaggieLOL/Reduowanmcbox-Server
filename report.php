<?php

/*
                ReDuowanmcbox Report             
                2022/11/10 - NotFlyLoong                    
*/

$met = $_GET["met"];
if($met == "reportbug"){
    echo '<a href="https://bug.mc-m.net/">点击反馈bug</a>';
}
elseif ($met == "withp"){
    echo '<a href="http://wpa.qq.com/msgrd?v=3&uin=2924613132&site=qq&menu=yes" target="_blank"><img src="http://wpa.qq.com/pa?p=2:2924613132:51" alt="" title=""></a>'
}
