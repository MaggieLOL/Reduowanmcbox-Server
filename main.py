import flask,uuid,sqlite3,json,base64,time,datetime,hashlib,random
from captcha.image import ImageCaptcha
roomList=[]
captchas={}
CAP_CHARATERS='123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
app=flask.Flask("ReDuowanBox-Backend(Remake) By Maggie")
app.config["JSON_AS_ASCII"]=False
"""
@app.errorhandler(500)
def error500(err):
    return {"code":500,"text":"未知错误"}
@app.errorhandler(404)
def error404(err):
    return {"code":404,"text":"找不到页面"}
"""
@app.route("/api/captcha")
def captcha():
    global captchas
    captcha_uuid=str(uuid.uuid4())
    captcha_string="".join([random.choice(CAP_CHARATERS) for char in range(4)])
    gener=ImageCaptcha(width=170,height=80)
    img=gener.generate_image(captcha_string)
    img.save(f"./assets/{captcha_uuid}.png")
    captchas.update({captcha_uuid:{"authed":False,"answer":captcha_string}})
    return {"code":200,"text":"验证码生成成功","path":"/api/assets/"+captcha_uuid+".png","uuid":captcha_uuid}
@app.route("/api/captcha/answer")
def cap_answer():
    global captchas
    uuid=flask.request.args["uuid"]
    answer=flask.request.args["answer"]
    right=captchas[uuid]["answer"]
    if answer.upper()==right:
        captchas[uuid]["authed"]=True
        return {"code":200,"text":"验证成功！"}
    captchas.pop(uuid)
    return ({"code":500,"text":"验证失败"},500)
def captchaAuth(uuid):
    global captchas
    try:
        if captchas[uuid]["authed"]:
            captchas.pop(uuid)
            return True
        else:
            return False
    except:
        return False
@app.route("/api/assets/<cap_id>")
def assets(cap_id):
    with open(f"./assets/{cap_id}","rb") as f:
        return flask.Response(f.read(), mimetype='image/jpeg')
@app.route("/api/account/restiger",methods=["GET"])
def restiger():
    args=flask.request.args
    try:
        if not captchaAuth(args["captcha-uuid"]):
            return ({"code":500,"text":"错误：非法的人机验证鉴权码"},500)
        name=args['name']
        if name == "" or len(name) >= 24:
            return ({"code":500,"text":"您的名称是不是太长了？"})
        gender=args['gender']
        if gender.lower() not in ["male","female","other","unknown"]:
            return ({"code":500,"text":"非法性别"},500)
        birthday=args['birthday']
        #check is the birthday vaild
        blist=birthday.split("-")
        byr=blist[0]
        if len(byr) != 4:
            return ({"code":500,"text":"您的生日过于离谱。"},500)
        if int(byr)>=3000 or int(byr)<=1900:
            return ({"code":500,"text":"您的生日过于离谱。"},500)
        bmo=blist[1]
        if int(bmo)>12 or int(bmo)<1:
            return ({"code":500,"text":"你哪来的这个月份？"},500)
        bday=blist[2]
        if int(bday)>31 or int(bday)<1:
            return ({"code":500,"text":"日期不合法"},500)
        if len(blist) > 3:
            return ({"code":500,"text":"非法生日格式"},500)
        #end birthday check
        password=args["password"]
        if len(password)<=8:
            return ({"code":500,"text":"您的密码不够安全。"},500)
        password=hashlib.sha512(password.encode("utf-8")).hexdigest()
        bio=args.get("bio")
        if bio == None or bio == "":
            bio="这个人很懒，什么都没写"
        if len(bio) >= 200:
            return ({"code":500,"text":"简介≠论文。您要不少写点字？(<200)"},500)
        bio=base64.b64encode(bio.encode("utf-8")).decode("ascii")
        resday=datetime.datetime.now().strftime("%Y-%m-%d")
        coin=0
        sqlcommand="INSERT INTO users (NAME,GENDER,BIRTHDAY,BIO,RESTIGERDAY,COIN,PASSWORD) values (?,?,?,?,?,?,?)"
        sqlvalues=(name,gender,birthday,bio,resday,coin,password)
        conn=sqlite3.connect("./users.db")
        if len(conn.execute("select * from users where NAME=?",(name,)).fetchall()) > 5:
            return ({"code":500,"text":"使用此名称的用户过多，请换一个名称。"},500)
        conn.execute(sqlcommand,sqlvalues)
        conn.commit()
        length=conn.execute("select ID from users;")
        ID=length.fetchall()[-1][0]
        conn.close()
        return {"code":200,"text":"注册成功！","id":ID}
    except Exception as error:
        return ({"code":500,"text":f"参数缺失或服务器出现错误：{error}"},500)
@app.route("/api/account/<ID>/info",methods=["GET"])
def getaccountinfo(ID):
    try:
        int(ID)
    except:
        return ({"code":500,"text":"非法ID"},500)
    conn=sqlite3.connect("./users.db")
    cur=conn.execute("select * from users where ID=?",ID)
    data=cur.fetchall()
    if data==[]:
        return ({"code":404,"text":"此用户不存在"},404)
    data=data[0]
    conn.close()
    return {
        "code":200,
        "text":"成功获取用户资料",
        "info":{
            "ID":data[0],
            "name":data[1],
            "gender":data[2],
            "birthday":data[3],
            "bio":base64.b64decode(data[4].encode("ascii")).decode("utf-8"),
            "restigertime":data[5],
            "coin":data[6]
            }
        }

app.run(host="0.0.0.0",port=5069)
