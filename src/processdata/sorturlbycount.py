##sorturlbycount.py	输入文件：	url2id2time**last.txt
##			输出文件：	urlsortbyinterval**.txt
##			将url按出现次数排序，并取前10000个
#sort by time interval

def sortDic(Dict,valuePostion):
    return sorted(Dict.items(),key=lambda e:e[1][valuePostion],reverse=False) #reverse=True 倒排


def run():
    infile = open(r'E:\dataset\url2id2time07last.txt','r')
    outfile = open(r'E:\dataset\urlsortbyinterval07_20k.txt','w')
    urllist=[]
    count = 0
    while int(count) < 20000 :
        line = infile.readline().strip()
        if line=='':
            break
        temp = line.split('\t')
        temp[1] = str(count)
        urllist.append(temp)
        count += 1
    print len(urllist)
    urllist.sort(key = lambda e:float(e[2]),reverse=False)
    for it in range(0,len(urllist)):
##        print '\t'.join(urllist[it])
        outfile.write('\t'.join(urllist[it])+'\n')
    outfile.close()
    infile.close()

if __name__ == '__main__':
    run()
##    myDict = { 'item1' : [ 7, 1, 9], 'item2' : [8, 2, 3], 'item3' : [ 9, 3, 11 ] }
##    print sortDic(myDict,2)
