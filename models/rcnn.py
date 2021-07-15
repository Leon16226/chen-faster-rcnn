from torchvision.models.detection.faster_rcnn import FasterRCNN

class OWOD_FasteRCNN(FasterRCNN):
    def __init__(self):
        super(FasterRCNN,self).__init__()

