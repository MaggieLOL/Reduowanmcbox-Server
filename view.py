from django.http import HttpResponse
import os
def craftRoom(request):
    with open ("room.flag","w") as f:
        f.write(request.POST["flag"])
    return HttpResponse("ok")
def quitRoom(request):  
    os.system("rm -rf room.flag")
    return HttpResponse("ok")
