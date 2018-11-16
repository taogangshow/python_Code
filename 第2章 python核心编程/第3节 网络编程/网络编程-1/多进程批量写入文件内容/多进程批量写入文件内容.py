from multiprocessing import Pool
import os,random

def writeFileTask(folderName,name):
    f = open(folderName+"/"+name,"w")
    f.write("速度与激情-"+str(random.randint(1,24)))
    f.close()
def main():
    folderName = input("请输入要执行的文件夹名:")
    fileNames = os.listdir(folderName)
    pool = Pool(5)
    for name in fileNames:
        pool.apply_async(writeFileTask,(folderName,name))

    pool.close()
    pool.join()
if __name__ == "__main__":
    main()