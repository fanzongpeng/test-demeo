import requests


class Iouapi():

    def create_iou(self,data):
        return requests.post("http://59.110.219.71:9111/ioucenter/iou/getIou",
                         headers={"Content-Type":"application/json"},
                         json=data
                      )


