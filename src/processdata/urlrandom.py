
##urlrandom.py	输入文件：	urlsortbyinterval**.txt
##		输出文件:	url2id4exp**-****.txt
##		从urlsortbyinterval**.txt随机选择****个url，
##
import random

def run():
    infile = open('E:\dataset\urlsortbyinterval07.txt','r')
    outfile = open('E:\dataset\url2id4exp07-1000.txt','w')
    maxnum = 10000
    randnum = 1000

    rand = []
    for it in range(0, randnum):
        num = random.randint(0, maxnum)
        while num in rand:
            num = random.randint(0, maxnum)
        rand.append(num)
    print len(rand)
    count = 0
    while int(count) <  maxnum :
        line = infile.readline().strip()
        if line=='':
            print count
            break
        if count in rand:
            outfile.write(line+'\n')
            
        count += 1

    
    infile.close()
    outfile.close()


if __name__=='__main__':
    run()
