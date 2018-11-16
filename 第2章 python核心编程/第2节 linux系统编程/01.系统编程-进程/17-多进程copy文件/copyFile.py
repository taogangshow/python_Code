from multiprocessing import Pool,Manager
import os

def copyFileTask(name,oldFolderName,newFolderName,queue):
    fr = open(oldFolderName+"/"+name)
    fw = open(newFolderName+"/"+name,"w")
    
    content = fr.read()
    fw.write(content)
    
    fr.close()
    fw.close()

    queue.put(name)
def main():
    #1.获取要copy的文件夹名
    oldFolderName = input("请输入要复制的文件名:")
    #2.创建文件夹
    newFolderName = oldFolderName+"-复件"
    #print(newFolderName)
    os.mkdir(newFolderName)
    #3.获取old文件夹中所有文件名字
    fileNames = os.listdir(oldFolderName)
    #print(fileNames)
    #4.使用多进程的方式copy原文件中的所有文件到新文件中
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
        print("\rcopy的进度为:%.2f%%"%(copyRate*100),end="")
        if num == allNum:
            break
    print("")
if __name__ == "__main__":
    main()
