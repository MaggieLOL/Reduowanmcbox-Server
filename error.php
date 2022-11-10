<!DOCTYPE html>
<html lang="cn">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="https://cdn.staticfile.org/twitter-bootstrap/5.1.1/css/bootstrap.min.css" rel="stylesheet">
  <script src="https://cdn.staticfile.org/twitter-bootstrap/5.1.1/js/bootstrap.bundle.min.js"></script>
  <title>Errorrrrrrrrrrrrrrrrrrr! <?php echo $_GET["errorcode"];?> Server Error</title>
</head>
<body>
  <div class="container mt-5">
    <div class="row">
      <div class="col-sm-4">
        <img src="http://101.43.48.113/error.png" height="100" width="100" id="img01"></img>
        <h3>Reduowanmcbox <?php echo $_GET["error"];?></h3>
        <p id="errormsg">令人悲伤的Error界面呢······</p> 
        <script>
          var current = 0;
          // 末影人君 给他整个活
          img01.oncontextmenu = function (e) {
            document.getElementById("errormsg").innerHTML='末影人君 给他整个活';
              e.preventDefault();
              //每次点击鼠标右键 current都会增加90
              current += 90;
              this.style.transform = 'rotate(' + current + 'deg)';
          }
          img01.onclick = function () {
            document.getElementById("errormsg").innerHTML='末影人君 给他整个活';
              //每次点击鼠标左键 current都会减少90
              current -= 90;
              //向左旋转90度
              this.style.transform = 'rotate(' + current + 'deg)';
          }
      </script>
        <p>Error: <?php echo $_GET["msg"];?></p>
        <br /> <hr />
        <p>如果想获得服务器的实时修复进度,请前往<a href="https://mc-m.net/">本项目官网</a>寻找群号,QQ群组内有实时通知.</p>
      </div>
    </div>
  </div>
</body>
</html>