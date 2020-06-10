import pandas as pd
import xml.etree.ElementTree as ET
import glob

def xml_to_csv(path):
    xml_list = []
   
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text)
                     )
            xml_list.append(value)
            
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df

def generate_csv(xml_path, record_path):
    xml_df = xml_to_csv(xml_path)
    dataset_type = os.path.basename(os.path.dirname(xml_path)) # gets the penultimate directory name
    xml_df.to_csv(record_path + '/' + dataset_type +'_labels.csv', index=None)
    print("Successfully converted " + dataset_type + " xml to csv.")
