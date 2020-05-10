import os
import sys

def rename(name,str_len):
    print('name = ',name)
    PACKAGE_DIRECTORY = os.path.abspath('.')
    path=PACKAGE_DIRECTORY #這就是欲進行檔名更改的檔案路徑，路徑的斜線是為/，要留意下！
    files=os.listdir(path)
    print('files=',files) #印出讀取到的檔名稱，用來確認自己是不是真的有讀到

    
    n=0 #設定初始值
    for i in files: #因為資料夾裡面的檔案都要重新更換名稱        
        name_find= files[n].find(name)
        print (name_find)
        if (name_find>0):
            ext_name=os.path.splitext(files[n])[1]
            print("ext_name=",ext_name)
            newname=files[n][name_find:name_find+int(str_len)]
            newname = newname+ext_name;
            print('newname=',newname)
            #oldname=path+ '\ ' +files[n] #指出檔案現在的路徑名稱，[n]表示第n個檔案
            oldname= os.path.join(path,files[n]) 
            newname2= os.path.join(path,newname)            
            os.rename(oldname,newname)
            

        #print('oldname = ',oldname2)
        #newname=path+'2017-'+str(n+1)+'.wav' #在本案例中的命名規則為：年份+ - + 次序，最後一個.wav表示該檔案的型別
        #os.rename(oldname,newname)
        #print(oldname+'>>>'+newname) #印出原名與更名後的新名，可以進一步的確認每個檔案的新舊對應
        n=n+1 #當有不止一個檔案的時候，依次對每一個檔案進行上面的流程，直到更換完畢就會結束
    


def main (args):
    if (len(args)>1):
        rename(args [1])
    else:
        cut_str=input("請輸入從哪個字串前刪除")
        str_len=input("保留字串長度")
        rename(cut_str,str_len)
    
    
    
if __name__ == '__main__':
    main (sys.argv)
    