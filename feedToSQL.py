import feedparser
import sqlite3
from datetime import datetime

rss_url = 'https://www.eluniverso.com/arc/outboundfeeds/rss-subsection/noticias/ecuador/?outputType=xml'
feed = feedparser.parse(rss_url)
'''
dict_keys(['title', 'title_detail', 'links', 'link', 'id', 'guidislink', 'authors', 'author', 'author_detail',
 'summary', 'summary_detail', 'published', 'published_parsed', 'content', 'media_content'])
'''
conexion=sqlite3.connect("rssFeed.db")
try:
    conexion.execute("""
                            create table feed (
                              id integer primary key autoincrement,
                              titulo text,
                              enlace text,
                              sumario text,
                              autor text,
                              fecha text)
                     """)
    print("se creo la tabla articulos")                        
except sqlite3.OperationalError:
    print("La tabla articulos ya existe")  

nf = len(feed.entries)
if feed.status == 200:
    print(f'Añadiendo {nf} filas')
    for entry in feed.entries:
        try:
            d = entry.published
            d = d[4:-6]   
            datetime_object = datetime.strptime(d.strip(),'%d  %b %Y %H:%M:%S' ) 
            conexion.execute("insert into feed(titulo,enlace,sumario,autor,fecha) values (?,?,?,?,?)", (entry.title, entry.link, entry.summary, entry.author, str(datetime_object)))
        except:
            continue
        
else:
    print("Status code:", feed.status)

conexion.commit()
conexion.close()   



















