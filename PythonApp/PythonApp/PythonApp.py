import webbrowser
import time

testing="haha"

html_content = f"<html> <head> </head> <h1> {testing} </h1> <body> </body> </html>"

with open("index.html", "w") as html_file:
    html_file.write(html_content)
    print("Html file created successfully !!")


time.sleep(2)
webbrowser.open_new_tab("index.html")