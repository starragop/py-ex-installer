import urllib.request
from time import sleep
import logging
import ast

progressexists = False
try:
    from progress.bar import Bar
    progressexists = True
except:
    print("Progress bar doesn't exist. Run pip install progress")

logger = logging.getLogger('installlog')
hdlr = logging.FileHandler('installlog.log')
formatter = logging.Formatter('%(asctime)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.DEBUG)

filepage = 0

def install():
    with urllib.request.urlopen("https://raw.githubusercontent.com/starragop/xyzmessage/master/info") as url:
        filepage = url.read()
    data = filepage.decode('utf-8')
    data = ast.literal_eval(data)
    logger.info(data)
    if progressexists == True:
        with Bar('Downloading files...', max=(len(data))) as bar:
            for i in range(len(data)):
                x = data[i]
                logger.info("Installing " + x)
                print("Installing " + x)
                dat = urllib.request.urlopen("https://raw.githubusercontent.com/starragop/xyzmessage/master/" + x)
                file = open(x,"w")
                file.write((dat.read()).decode('utf-8'))
                file.close()
                print("Installed " + x)
                bar.next()
    else:
        for i in range(len(data)):
            x = data[i]
            logger.info("Installing " + x)
            print("Installing " + x)
            dat = urllib.request.urlopen("https://raw.githubusercontent.com/starragop/xyzmessage/master/" + x)
            file = open(x,"w")
            file.write((dat.read()).decode('utf-8'))
            file.close()
            print("Installed " + x)
    print("Done!")
    logger.info("Successfully installed!")
    sleep(3)

confirm = input("Install? (Y/N)")
if (confirm == "Y"):
    try:
        install()
    except Exception:
        logger.exception("Encountered an error during install")
