##userurlidtime.py	将UidUrltime**.txt中的url变成urlid
##			输入：	UidUrltime**.txt  url2id2time.txt
##			输出：	UidUrlId.txt



def run():
    try:
        infileuid = open(r'E:\dataset\UidUrltime07.txt','r')
        infileurl = open(r'E:\dataset\url2id2time07.txt','r')
        outfile = open(r'E:\dataset\UidUrlId07.txt','w')
        outID = open(r'E:\dataset\Uid2testID.txt','w')
        url2id = {}

        #读入url2id文件
        while 1:
            line = infileurl.readline().strip()
            if line=='':
                break
            temp = line.split('\t')
            url2id[temp[0]] = temp[1]
        print 'reading completed'
        #读入并处理
        flag2uid = 0
        count = 0
        while 1:
            line = infileuid.readline().strip()
            if line=='':
                break
            if line=='***':
                flag2uid = 1
                if count != 0:
                   outfile.write('\n') 
                continue
            if flag2uid == 1:
                temp = line.split(':')
                uid = temp[0]
                userurls = temp[1]
                flag2uid = 0
                outfile.write('U\t'+str(count)+'\n')
                outID.write(str(uid)+'\t'+str(count)+'\n')
                print 'write\t'+str(count)
                count += 1
            else:
                temp = line.split('\t')
                outfile.write('L\t'+str(url2id[temp[0]])+'\t'+str(temp[1])+'\n')
                
    except e:
        print e
    finally:
        infileuid.close()
        infileurl.close()
        outfile.close()
        outID.close()
        
            
    


if __name__=='__main__':
    run()
