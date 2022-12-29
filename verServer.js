/*
                ReDuowanmcbox version server                
                2022/11/10 - NotFlyLoong                    
*/


// 常量定义
const http          = require("http");
const { exit } = require("process");
const androidVER    = "0"
const pcmcboxVER    = "B1.0.0"
const iphoneVER     = "B0.1.1"
const linuxVER      = iphoneVER
const macOSVER      = linuxVER

//创建http服务器
try{
    http.createServer(function (require, resp){
        // 发送HTTP头
        // 状态:200 OK 内容类型 text/plain
        resp.writeHead(200, {'Content-Type': 'text/plain'});
        sendText = androidVER + '|' + pcmcboxVER + '|' + iphoneVER + '|' + linuxVER + '|' + macOSVER;
        resp.end(sendText);
    }).listen(1025)
    console.log('[LOG]Reduowanmcbox verServer running at prot 1025')
    const readline = require('readline');
    function readSyncByRl(tips) {
        tips = tips || '> ';
        return new Promise((resolve) => {
            const rl = readline.createInterface({
                input: process.stdin,
                output: process.stdout
            });
     
            rl.question(tips, (answer) => {
                rl.close();
                resolve(answer.trim());
            });
        });
    }

    readSyncByRl('Enter exit to close:').then((res) => {
        if(res == 'exit'){
            exit();
        }
    });
}
catch(e){
    console.error('[ERROR] The version server encountered a \n fatal error, delete try to get a detailed report')
}

