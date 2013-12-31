
##userurltime.py  从数据集里面提取用户id、发过的url、以及url发布的时间
##		url的时间以代码中变量startdate = '2011-05-01 00:00:00'为计时0点的秒数，可以在此修改
##		读入文件:	tweets文件夹下所有
##		输出文件：	UidUrltime**.txt  （**为计时0点的月份，05表示从5月1日）
##		输出事例：
##			***
##			123:1       		 	#uid: urlcount
##			http://co.ly	4321234	 	#url	urltime


import datetime
import sys, os

startdate = '2011-07-01 00:00:00'


global usercount

def timedelta(curtime):
    starttime = datetime.datetime.strptime(startdate, '%Y-%m-%d %H:%M:%S')
    d = datetime.datetime.strptime(curtime,'%a %b %d %H:%M:%S %Y')
    delta= d - starttime
    return delta.total_seconds()

def istime(temp):
    time = ' '.join(temp[1:5])
    time += ' '+temp[6]
    timejiange = timedelta(time)
    return timejiange


def geturlplain(infilename,outfile,uid):
    infile = open (infilename+'\\'+str(uid),'r')
#    global urlcount
    global usercount
    flag=0
    urllist=[]
    content=''
    url=''
##    print infile.readline()
    while 1:
        line = infile.readline().strip()
##        print line
        if line=='':
            break
        if line=='***' and flag == 0:
            flag = 1
            url=''
            content=''
            continue
        if line=='***' and flag == 1:
            flag = 0
            continue
        if flag == 1:
            temp = line.split()
            if temp[0]=='Text:':
                content = temp[1:]
            if temp[0]=='URL:' and len(temp)>1:
                url = temp[1]
##                print url
            if temp[0]=='Time:' and len(url)>0:
                jiange = istime(temp)
                if jiange > 0 :
                    urllist.append(' '.join(content))
##                    print url
    if len(urllist)>0:
        usercount += 1
        outfile.write(uid+'\t'+' '.join(urllist)+'\n')
##            print item
    infile.close()
                    
            

def run():
    try:
        global usercount
        usercount=0
        wfile=open(r'E:\dataset\content\URLplain07.txt','w')
        infile_dir = r'E:\dataset\tweets'
        Filelist = os.listdir(infile_dir)
        for uid in Filelist:
            geturlplain(infile_dir, wfile, uid)
            print str(usercount)+'\t'+str(uid)    
    finally:
        print 'user:\t'+str(usercount)
        wfile.close()

    #以2011年7月1日为始计算时间
    



if __name__=='__main__':
    run()
    
