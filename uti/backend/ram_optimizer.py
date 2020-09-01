import psutil,os,subprocess,time,eel
# @eel.expose
# def dummy():
#     return "fdbfskdf",21,43,45,56
@eel.expose
def optimize():
    m=psutil.virtual_memory()[2]
    p=subprocess.check_output("EmptyStandbyList.exe workingsets",stderr=subprocess.PIPE)
    p=subprocess.check_output("EmptyStandbyList.exe modifiedpagelist",stderr=subprocess.PIPE)
    p=subprocess.check_output("EmptyStandbyList.exe standbylist",stderr=subprocess.PIPE)
    p=subprocess.check_output("EmptyStandbyList.exe priority0standbylist",stderr=subprocess.PIPE)
    time.sleep(4)
    return m-psutil.virtual_memory()[2]
eel.init(r'C:\Users\User\IdeaProjects\utilitysoft\uti\frontend')
eel.start(r"C:\Users\User\IdeaProjects\utilitysoft\uti\frontend\index.html",size=(1000,600))
