import os
import os.path
import xml.etree.ElementTree as ET
import glob

class_names = ['person with helmet','person','helmet','person without helmet']
xmlpath='C:/Users/18251/Desktop/TrainImage2/train_annot_folder'
txtpath='C:/Users/18251/Desktop/TrainImage2/txt_annot'


def xml_to_txt(xmlpath,txtpath):

    os.chdir(xmlpath)
    annotations = os.listdir('.')
    annotations = glob.glob(str(annotations)+'*.xml')

    file_save = 'train' + '.txt'
    file_txt = os.path.join(txtpath, file_save)
    f_w = open(file_txt, 'w')

    for i,file in enumerate(annotations):

        in_file = open(file)
        tree=ET.parse(in_file)
        root = tree.getroot()


        filename = root.find('filename').text

        for obj in root.iter('object'):
                current = list()
                name = obj.find('name').text

                class_num = class_names.index(name)

                xmlbox = obj.find('bndbox')

                x1 = xmlbox.find('xmin').text
                x2 = xmlbox.find('xmax').text
                y1 = xmlbox.find('ymin').text
                y2 = xmlbox.find('ymax').text

                f_w.write('VOCdevkit/VOC2007/JPEGImages/'+filename+'.jpg '+x1+','+y1+','+x2+','+y2+','+str(class_num)+'\n')

xml_to_txt(xmlpath,txtpath)






# C:/Users/18251/Desktop/TrainImage2/train_annot_folder
# C:/Users/18251/Desktop/TrainImage2/txt_annot
