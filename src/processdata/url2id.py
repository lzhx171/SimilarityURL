
##url2id.py 	将url转成数字id形式
##		读入文件：	UidUrltime**.txt
##		输出文件：	url2id2time*****.txt 
##		输出格式：url urlid avurltime（平均发布时间间隔）urlcount(被发布的次数)	
##
##


def run():
    infile = open(r'E:\dataset\UidUrltime07.txt','r')
    out = open(r'E:\dataset\url2id2time07more20.txt','w')
    url2id = {}
    counturl = 0
    user = 0
    while 1:
        line = infile.readline().strip()
##        if counturl>1000:
##            break
        if len(line)<1:
            break
        if line=='***':
            print user
            user += 1 
        temp = line.split('\t')
        if len(temp)<2:
            continue
        try:
            url2id[temp[0]].append(float(temp[1]))
        except:
            url2id[temp[0]] = []
            url2id[temp[0]].append(float(temp[1]))
            counturl += 1
    count = 1
    for item in url2id.keys():
        urltime = url2id[item]
        urltime.sort()
        time = 0
        if len(urltime)>5:
            for it in range(0,len(urltime)):
                time += float(urltime[it]) - float(urltime[0])
            time = time/len(urltime)
            out.write(str(item)+'\t'+str(count)+'\t'+str(time)+'\t'+str(len(urltime))+'\n')
            count += 1
    infile.close()
    out.close()


if __name__ == '__main__':
    run()
