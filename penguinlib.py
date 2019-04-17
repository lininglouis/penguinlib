import os
import re
import  magic

def get_string_no_suffix(string):
    # input xxxx/yyy.txt 
    # output xxx/yyy
	res = re.findall(pattern='(.*)\..*', string=string)
	if res:
		return res[0]
	else:
		return None

def getImageShape(image_path):
	metaStr = magic.from_file(image_path)
	res = re.search(string=metaStr, pattern=', (\d+)x(\d+)')
	#res = re.search(string=metaStr, pattern='height=(\d+).*width=(\d+)')
	if res:
		height, width = res.groups()
		return [int(height), int(width)]
	else:
		return [None, None]

def changeSuffixTo(string, destSuffix):
	#input  function(xxx//xxx.jpeg, destSuffix='txt'):
	#output xxx//xxx.txt
	return get_string_no_suffix(string) + '.' + destSuffix

def list_full_path(dirPath):
	file_paths = []
	for f in os.listdir(dirPath):
		file_paths.append(os.path.join(dirPath,f))
	file_paths.sort()
	return file_paths

def list_all_files_recursively(dirPath):
	file_paths = []
	for root, dirs, files in os.walk(dirPath, topdown=False):
		for name in files:
			file_paths.append(os.path.join(root, name))
	file_paths.sort()
	return file_paths


def mkdir_if_not_exists(dirPath):
	if not os.path.exists(dirPath):
		os.makedirs(dirPath)
		
		
def put_boxes(boxes, img):
    img_canvas = img.copy()
    for box in boxes:
        x1, y1, x2,y2 = box[:4]
        x1 = int(x1)
        y1 = int(y1)
        x2 = int(x2)
        y2 = int(y2)
        img_canvas = cv2.rectangle(img_canvas, (x1, y1), (x2, y2), (255,0,0), 2)
    return img_canvas

