###截图
import cv2
import re
from PIL import ImageGrab

def cutImage(topleftx, toplefty, lowrightx, lowrighty, name):
    piclocation = (topleftx, toplefty, lowrightx, lowrighty)
    im = ImageGrab.grab(piclocation)
    name = re.sub('.png', '', name)
    name = re.sub('.PNG', '', name)
    name = re.sub('.jpg', '', name)
    name = re.sub('.JPG', '', name)
    name = re.sub('.jpeg', '', name)
    name = re.sub('.JPEG', '', name)
    name = re.sub('.tif', '', name)
    name = re.sub('.TIF', '', name)
    count = 0
    im.save(name + '_' + str(count) + '.png')
    return 0

cutImage(0, 0, 1920, 1080, 'test.png')
 
# 去除字符串中相同的字符
#s = '\tabc\t123\tisk'
#print(s.replace('\t', ''))
#import re
# 去除\r\n\t字符
#s = '\r\nabc\t123\nxyz'
#print(re.sub('[\r\n\t]', '', s))

