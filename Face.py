import requests
from json import JSONDecoder
import cv2
import os

class Face():
    def __init__(self):
        super().__init__()


        #Search the Faces Library to get all the filename,ready to regonize.
        self.FileList = []
        path = ".\Faces"
        for home,dirs,files in os.walk(path):
            for filename in files:
                self.FileList.append(os.path.join(home, filename))
        
    def search(self,faceId1):
        compare_url = "https://api-cn.faceplusplus.com/facepp/v3/compare"
        key ="Your Key"
        secret ="Your Secret"
        flag = False
        for faceId2 in self.FileList:
            if faceId2 == "Main.py":
                continue
            data = {"api_key": key, "api_secret": secret}
            files = {"image_file1": open(faceId1, "rb"), "image_file2": open(faceId2, "rb")}
            response = requests.post(compare_url, data=data, files=files)

            req_con = response.content.decode('utf-8')
            req_dict = JSONDecoder().decode(req_con)
            #print(req_dict)
            confindence = req_dict['confidence']
            #print(confindence)
            if confindence >= 65:
                print('The same\n')
                flag = True
                name = faceId2
                break
            else:
                print('Not the same\n')

        if flag:
            print("YES\n")
            print(name)
            return name
        else:
            print("NO")
            return None
