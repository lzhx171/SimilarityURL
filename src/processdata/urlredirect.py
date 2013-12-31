
import urllib2 as ul2
import requests


def run():
    filename=r'E:\dataset\urlsortbyinterval07_20k.txt'
    outfilename = r'E:\dataset\urlsortbyinterval07_20k_short2real.txt'
    key ='https://sb-ssl.google.com/safebrowsing/api/lookup?client=api&apikey=ABQIAAAATmBsvcdyCRFXZEX3c5aMEBQ5sS2Pfr3VJnIVqPVyDWdBfQOVGA&appver=1.0&pver=3.0&url=' 
    infile = open(filename,'r')
    outfile = open(outfilename, 'w')
    proxies = {"http":"http://127.0.0.1:8087","https":"https://127.0.0.1:8087"}
    count = 0
    try:
        while 1:
            line = infile.readline().strip()
            if line=='':
                break
            temp = line.split()
            last=''
            try:
                last = requests.get(temp[0],proxies=proxies,timeout=10)
                last = last.url
                #last = redirect.geturl()
                outfile.write(temp[0]+'\t'+last+'\n')
                print 'process\t'+ str(count) +'\t'+last
            except:
                outfile.write(temp[0]+'\n')
                print 'process\t'+ str(count) +'\twrong!'
                """try:
                    last = requests.get(temp[0],proxies=proxies)
                    last = last.url
                    outfile.write(temp[0]+'\t'+last+'\n')
                    print 'process\t'+ str(count) +'\t'+last
                except:"""
            count += 1
    finally:
        infile.close()
        outfile.close()    
        

if __name__=='__main__':
    run()