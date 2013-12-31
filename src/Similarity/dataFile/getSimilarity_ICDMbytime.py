
import os,sys
import math

def cur_file_dir():
    
    path = sys.path[0]
    
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)

class URLTIME:
    def __init__(self,url=-1,urlnum=-1,time=-1):
        self.url = url
        self.urlnum = urlnum
        self.time = time


def run():

    inraw = open('E:\ICDMexp\userSimilarity\dataFile\CandidateUserUrlWithURLID.txt','r')


    outfile = open('E:\ICDMexp\userSimilarity\dataFile\CandidateUserUrlWithURLID_last.txt','w')
    old2new = open('E:\ICDMexp\userSimilarity\dataFile\MyUidold2new.txt','w')
    outsimilarity = open('E:\ICDMexp\userSimilarity\dataFile\Similaritybytime2.txt','w')

    urltime = {}    #记录每个url的时间间隔
    urltocount = {} #记录每个url一共出现次数
    linecount = 0
    while 1:
        line = inraw.readline()
        linecount +=1
        if linecount%10000 == 0:
            print linecount
        if line=='':
            break
        temp = line.split()
        if len(temp)<1:
            continue
        if temp[0]=='L':
            try:
                urltime[temp[1]].append(temp[2])
            except:
                urltime[temp[1]]=[]
                urltime[temp[1]].append(temp[2])
    
    for url in urltime.keys():
        timelist=urltime[url]
        urltocount[url]=len(timelist)
        timelist.sort(key = lambda e:float(e))
        index=0
        sum = 0
        while index < urltocount[url]-1:
            sum += float(timelist[index+1])-float(timelist[index])
            index += 1
        if urltocount[url]==1:
            sum = -1
        else:
            sum = sum/len(timelist)
        urltime[url]=sum
        
 
    print 'Already process url-id-timeinterval'

    inraw.seek(0);
    ##获取Userurls
    count = 0
    tempuserurl = {}
    Userurls = {}   #全局保存所有user和url的字典
    uid = ''
    total = 0    #计算所有url数
    usernum = 0
    uidold2new={}
    while 1:
        line = inraw.readline()
        if line=='':
            break
        line = line.strip()
        if len(line)==0:
            #写文件
            if len(tempuserurl.keys())==0:
                continue
            Userurls[uid] = []  #对每个user初始化一个列表，保存user发的URLTIME对象
           # print uid
            #return 0
            outfile.write('U\t'+str(uid)+'\n')
            usernum += 1
            if usernum%10000==0:
                print str(usernum)+'\t'+str(count)
            for item in tempuserurl.keys():
                total += tempuserurl[item]
                Userurls[uid].append(URLTIME(item,tempuserurl[item],urltime[item]))
                outfile.write('L\t'+str(item)+'\t'+str(tempuserurl[item])+'\t'+str(urltime[item])+'\n')
            if count > 0 :
                outfile.write('\n')
            continue
        temp = line.split()
        if temp[0]=='U':
            tempuserurl = {}
            count += 1
            #print count#####
            uid = count
            uidold2new[temp[1]]=count
            old2new.write(str(temp[1])+'\t'+str(uid)+'\n')
            continue
       
        if temp[0]=='L':
            if urltime[temp[1]]==-1:
                continue
            try:
                tempuserurl[temp[1]] += 1
            except :
                tempuserurl[temp[1]] = 1
    
    outfile.close()
    old2new.close()
    print 'Already processed reading ! Next, compute similarity'     
    
    ##计算相似度
    userList = Userurls.keys()
    userList.sort()
    #return 0
    index = 0
    for item in userList:   #用户 i
        print 'process '+ str(index) +'\t'+str(item)
        index += 1
        #计算用户i的信息
        info_i = 0     
        for urli in Userurls[item]:
            info_i += int(urli.urlnum) * math.log(float(total)/float(urltocount[str(urli.url)])) * math.exp(-float(urli.time)/float(3600))      
            
        for another in userList[index:]:    #用户 j
            info_ij = 0        
            for urli in Userurls[item]:
                for urlj in Userurls[another]:            
                    if urli.url == urlj.url:
                        info_ij += (int(urli.urlnum)+int(urlj.urlnum)) * math.log(int(total)/float(urltocount[str(urlj.url)]))*math.exp(-float(urlj.time)/float(3600))
                                
          #计算用户i和j相似度
            info_j = 0
            if info_ij > 0:
                #计算用户j的信息         
                for urlj in Userurls[another]:
                    info_j += int(urlj.urlnum) * math.log(float(total)/float(urltocount[str(urlj.url)]))*math.exp(-float(urlj.time)/float(3600))
                similarity = float(info_ij)/(info_i+info_j)
                outsimilarity.write(str(item)+'\t'+str(another)+'\t'+str(similarity)+'\n')
                
            
        

    
    inraw.close()

    outsimilarity.close()
    print 'completed!'
    
if __name__=='__main__':
    run()
##    URL=URLTIME()
##    print URL.url
    
