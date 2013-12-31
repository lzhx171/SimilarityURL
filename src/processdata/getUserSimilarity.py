import sys, os, math, time
import threading

global total
global UserUrls

def getUserUrl(fileName):
   global UserUrls
   UserUrls = {}

   readFile = open(fileName, 'r')
   count = 0
   while 1:
       count += 1
       if count % 10000 == 0:
          print('already reading '+str(count))
       user = readFile.readline()
       #print(user)
       if user == '':
           break
       userID = user.split()[1]

       line = readFile.readline()
       
       while line!='\n':
           urls = line.split()
           if len(urls)<=0:
              break
           URL = URLTIME()
           URL.url = int(urls[1])
           URL.time = float(urls[2])
           #print(URL)
           #didn't consider the replicate urls
           try:
              UserUrls[int(userID)].add(URL)
           except(KeyError):
              UserUrls[int(userID)] = set([])
              UserUrls[int(userID)].add(URL)

           line = readFile.readline()

   readFile.close()
   print('reading is done')

class URLTIME:
   url = -1
   time = -1

class userSimilarity(threading.Thread):
  
   def __init__(self, num, outFileName, begin, end):
      threading.Thread.__init__(self)
      print('initial')
      self.thread_num = num
      self.thread_stop = False
      self.outFileName = outFileName
      self.begin = begin
      self.end = end
      print('initial done')

   def run(self):
      print('in thread ')
      getUserSimilarityViaTime(self.outFileName, self.begin, self.end)
      
   def stop():
      self.thread_stop = True


def getUserSimilarityViaTime(outFileName, start, stop):
   print(start)
   print(stop)
   outFile = open(outFileName, 'w')

   global total
   global UserUrls
   #print('total number of urls is '+str(total))

   userList = UserUrls.keys()
   index = start
   for item in userList[start:stop]:
      print('process '+str(index))
      index += 1
      for another in userList[index:]:
         count = 0
         for urla in UserUrls[item]:
            for urlb in UserUrls[another]:
               if urla.url == urlb.url:
                  timeDiff = -math.fabs(urla.time - urlb.time)/float(3600)
                  #print('timeDiff '+str(timeDiff))
                  
                  count += math.exp(timeDiff)
         if count == 0:
            similarity = 0
         else:
            #print(count/total)
            
            similarity = (math.log(float(len(UserUrls[item]))/total)+math.log(float(len(UserUrls[another]))/total))/(2*(math.log(float(count)/total)))
            outFile.write(str(item)+'\t'+str(another)+'\t'+str(similarity)+'\n')
##            print(str(item)+'\t'+str(another)+'\t'+str(similarity))
   outFile.close()




##def getUserSimilarityViaTime(outFileName, start, stop):
##   print(start)
##   print(stop)
##   outFile = open(outFileName, 'w')
##
##   global total
##   global UserUrls
##   #print('total number of urls is '+str(total))
##
##   userList = UserUrls.keys()
##   index = start
##   for item in userList[start:stop]:
##      print('process '+str(index))
##      index += 1
##      for another in userList[index:]:
##         count = 0
##         for urla in UserUrls[item]:
##            for urlb in UserUrls[another]:
##               if urla.url == urlb.url:
##                  timeDiff = -math.fabs(urla.time - urlb.time)/float(3600)
##                  #print('timeDiff '+str(timeDiff))
##                  
##                  count += math.exp(timeDiff)
##         if count == 0:
##            similarity = 0
##         else:
##            #print(count/total)
##            
##            similarity = (math.log(float(len(UserUrls[item]))/total)+math.log(float(len(UserUrls[another]))/total))/(2*(math.log(float(count)/total)))
##            outFile.write(str(item)+'\t'+str(another)+'\t'+str(similarity)+'\n')
####            print(str(item)+'\t'+str(another)+'\t'+str(similarity))
   outFile.close()




def getURLNumber(fileName):
   urlSet = set([])
   readFile = open(fileName, 'r')
   while 1:
       user = readFile.readline()
       #print(user)
       if user == '':
           break
       url = readFile.readline()
       
       while url!='\n':
           URL = url.split('\t')[1]
           #print(URL)
           urlSet.add(URL)
           url = readFile.readline()
   readFile.close()
   #for item in urlSet:
      #print('L '+item)
   return len(urlSet)

def getUserSimilarityJustURL(fileName, outFileName, recordFile):
   outFile = open(outFileName, 'w')
   total = getURLNumber(fileName)
   record = open(recordFile, 'w')
   print('total number of urls is '+str(total)+'\t'+str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))))
   record.write('total number of urls is '+str(total)+'\t'+str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))))
   UserUrls = {}

   readFile = open(fileName, 'r')
   while 1:
       user = readFile.readline()
       #print(user)
       if user == '':
           break
       userID = user.split()[1]

       url = readFile.readline()
       
       while url!='\n':
           URL = url.split('\t')[1]
           #print(URL)
           try:
              UserUrls[int(userID)].add(int(URL))
           except(KeyError):
              UserUrls[int(userID)] = set([])
              UserUrls[int(userID)].add(int(URL))

           url = readFile.readline()
   record.write('reading process is done.''\t'+str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))))
   print('reading process is done.''\t'+str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))))
   readFile.close()

   index = 0
   for item in UserUrls.keys():
      index += 1
      if index%1000 == 0:
         print('already process '+ str(index)+'\t'+str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))))
         record.write('already process '+ str(index)+'\t'+str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))))
      for another in UserUrls.keys()[index:]:
         count = len(UserUrls[item] & UserUrls[another])
         
         if count == 0:
            similarity = 0
         else:
            similarity = (math.log(float(len(UserUrls[item]))/total)+math.log(float(len(UserUrls[another]))/total))/(2*(math.log(float(count)/total)))
            outFile.write(str(item)+'\t'+str(another)+'\t'+str(similarity)+'\n')
            print(str(item)+'\t'+str(another)+'\t'+str(similarity))
   outFile.close()


def cur_file_dir():
    
    path = sys.path[0]
    
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)

        
def run():
    cur_dir = cur_file_dir()
    getUserUrl(cur_dir+r'\UidUrlId07.txt')
    global total
    total =  3667162
    getUserSimilarityViaTime(cur_dir+r'\dataFile\userSimilarityViaTime0-20000.txt', 0, 2000)
##    thread1 = userSimilarity(1, cur_dir+r'\dataFile\userSimilarityViaTime0-20000.txt', 0, 20000)
##    thread2 = userSimilarity(2, cur_dir+r'\dataFile\userSimilarityViaTime20000-40000.txt', 20000, 40000)
##    thread3 = userSimilarity(3, cur_dir+r'\dataFile\userSimilarityViaTime40000-70000.txt',40000, 70000)
##    thread4 = userSimilarity(4, cur_dir+r'\dataFile\userSimilarityViaTime70000-110992.txt',70000, 110992)
##    thread1.start()
##    thread2.start()
##    thread3.start()
##    thread4.start()
'''
    t = [1,2,3,4,5]
    index = 0
    for item in t:
      index += 1
      for another in t[index:]:
         print(item, another)
'''
    #getStruct(r'E:\experiment\twitter\destinationURL\UserUrl06.txt', r'E:\experiment\twitter\destinationURL\StructUserUrl06.txt')
    #getUserURLs(cur_dir+r'/dataFile/structedURL.txt', cur_dir+r'/dataFile/CandidateUserUrl>=1.txt')
    #get(r'E:\experiment\twitter\destinationURL\CandidateUserUrl07-10.txt')
    #getURLNumber(cur_dir+r'/dataFile/CandidateUserUrl>=1.txt')

    
if __name__ == '__main__':
    run()
