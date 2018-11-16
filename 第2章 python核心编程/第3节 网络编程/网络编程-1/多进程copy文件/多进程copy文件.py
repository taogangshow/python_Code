from multiprocessing import Pool,Manager
import os,time

def copyFileTask(name,oldFolderName,newFolderName,queue):
    fr = open(oldFolderName+"/"+name)
    fw = open(newFolderName+"/"+name,"w")
    content = fr.read()
    fw.write(content)

    fr.close()
    fw.close()
    queue.put(name)
def main():
    try:
        oldFolderName = input("请输入要复制的文件夹名:")
        newFolderName = oldFolderName+"-复件"

        #print("复制成功后的文件夹名为:%s"%newFolderName)
        os.mkdir(newFolderName)
        fileNames = os.listdir(oldFolderName)
    except Exception as result:
        if os.path.exists(newFolderName):
            print("已捕获到异常信息如下:")
            print(result)
    pool = Pool(5)
    queue = Manager().Queue()
    for name in fileNames:
        pool.apply_async(copyFileTask,(name,oldFolderName,newFolderName,queue))

    #pool.close()
    #pool.join()
    num = 0
    allNum = len(fileNames)
    while True:
        queue.get()
        num+=1
        copyRate = num/allNum
        print("\r复制的进度为:%.2f%%" % (copyRate * 100), end="")
        time.sleep(0.1)
        if num == allNum:
            break
    print("\n已完成复制...")

if __name__ == "__main__":
    main()