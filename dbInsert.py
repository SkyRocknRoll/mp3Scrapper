#!/usr/bin/python
#Filename:Db
import MySQLdb   
import re


 
def insertIntoDB(songName , MovieName , url):
    sql = "insert into music ( Song_Name, Movie_Name, Song_URL) values ('"+ songName + "','"+MovieName+"','"+url+"');"
    print sql
    try:
        cursor.execute(sql)
        con.commit()
        print songName + '--' + MovieName + '--' + url
    except:
        print "Insert Failed"


base_url = "http://mp3.tamilmp3songs.mobi"
con = MySQLdb.Connect('localhost', 'root','', 'psgkriya_rathimusic')
cursor = con.cursor();  
filename = '1.mp3.txt'
f = open(filename, "r")
for  line in f:
    songDetails = line.split('/')
    x = len(songDetails)
    
    onlySongName = re.sub('Tamilanda.net|Tamilanda.com|Tamilmp3songs.mobi|Tamilmp3songs.Mobi|Tamilanda.com|www.Tamilanda.Net|Tamisongs.mobi|Tamilsongs.mobi', '', songDetails[x-1])
    onlySongName = re.sub('.mp3|www|\[|\]|\-|\.|songs|\n' , '',onlySongName)
    onlySongName = re.sub('_' , ' ' , onlySongName)
    insertIntoDB(onlySongName ,songDetails[x-2] , base_url+line )
#    print  onlySongName + ','+songDetails[x-2]
    
#    print 'Movie Name: ' + songDetails[4]
   
