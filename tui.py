from rich import print
from rich.panel import Panel
from rich.console import Console
from rich.text import Text
import sqlite3
import time
console = Console()
conexion = sqlite3.connect("rssFeed.db")
cursor = conexion.execute("""SELECT * FROM feed ORDER BY RANDOM() LIMIT 5""")
for _ in cursor:
    id_ = [0]
    titulo= _[1]
    link= _[2]
    resumen= _[3]
    autor= _[4]
    fecha= _[5]
    console.print(Panel(renderable=f'[red]{titulo.title()}\n[white]{resumen}\n[blue]{link}\n',title=autor, subtitle=fecha))
    time.sleep(0.5)

conexion.close()
















