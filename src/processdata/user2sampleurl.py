

##user2spampleurl.py 	输入文件：url2id4exp**-****.txt、UidUrltime**.txt
##			输出文件：user2spampleurl.txt(计算相似度的输入文件)、Uid2testID.txt
##			从UidUrltime**.txt中找出在url2id4exp**-****.txt出现的url及涉及的用户


#用随机的url得到相关的用户


def run():

    infile = open('E:\dataset\urlsortbyinterval07.txt','r')
    outfile =open('E:\dataset\user2idexp_10k.txt','w')
    uidfile = open('E:\dataset\UidUrltime07.txt','r')
    outID = open(r'E:\dataset\Uid2testID_10k.txt','w')
    #
    urldict = {}
    while 1:
        line = infile.readline().strip()
        if line=='':
            break
        temp = line.split('\t')
        urldict[temp[0]]=temp[1]
    #
##    print urldict.keys()
    flag2uid = 0
    count = 0
    userurllist = []
    usercount = 0
    uid = ''
    while 1:
        line = uidfile.readline().strip()    
        if line=='':
            break
        if line=='***':
            flag2uid = 1      
            if count != 0 and len(userurllist)>1:
##                print userurllist
                outfile.write('U\t'+str(count)+'\n')
                outID.write(str(uid)+'\t'+str(count)+'\n')
                for item in userurllist:
                    outfile.write(item)
                outfile.write('\n')
                usercount += 1
##                print usercount
            userurllist = []
            continue
        if flag2uid == 1:
            temp = line.split(':')
            uid = temp[0]
            userurls = temp[1]
            flag2uid = 0
            count += 1
            if count%1000==0:
                print str(count)+'\t'+str(usercount)
##            outfile.write('U\t'+str(count)+'\n')
##            outID.write(str(uid)+'\t'+str(count))
##            print 'write\t'+str(count)
            
        else:
            temp = line.split('\t')
            if temp[0] in urldict.keys():
                userurllist.append('L\t'+str(urldict[temp[0]])+'\t'+str(temp[1])+'\n')

    outID.close()
    uidfile.close()
    infile.close()
    outfile.close()


    
    
if __name__=='__main__':
    run()
