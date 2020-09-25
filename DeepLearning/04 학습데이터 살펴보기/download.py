import os
from urllib.request import urlretrieve

def download(url:str, dir : str, filename : str):

    if not os.path.isdir(dir):
        os.makedirs(dir)
    
    filepath = os.path.join(dir,filename)

    urlretrieve(url,filepath)

    
    
