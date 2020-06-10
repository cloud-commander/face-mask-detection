import shutil


def iterate_dir(source, dest, ratio):
    source = source.replace('\\', '/')
    dest = dest.replace('\\', '/')
    train_dir = os.path.join(dest, 'train')
    print(train_dir)
    test_dir = os.path.join(dest, 'test')
    print(test_dir)
    
    if not os.path.exists(train_dir):
        os.makedirs(train_dir)
    
    if not os.path.exists(test_dir):
        os.makedirs(test_dir)

        
    images = [f for f in os.listdir(source)
              if re.search(r'([a-zA-Z0-9\s_\\.\-\(\):])+(.jpg|.jpeg|.png)$', f)]

     
    num_images = len(images)
    num_test_images = math.ceil(ratio*num_images)
    
    print(num_test_images)
        
    for i in range(num_test_images):
        idx = random.randint(0, len(images)-1)
        
        filename = images[idx]
        filename_path = os.path.join(source, filename)
        
        xml_filename = os.path.splitext(filename)[0]+'.xml'
        xml_path = os.path.join(source, xml_filename)
        
        #copy image + XML files across only if accompanying XML file exists
        if os.path.isfile(xml_path):     
                shutil.copyfile(filename_path, os.path.join(test_dir, filename))
                shutil.copyfile(xml_path,os.path.join(test_dir,xml_filename))
        else:
            print("WARNING: the following XML file does not exist:" + xml_path)
        images.remove(images[idx])

    for filename in images:
        xml_filename = os.path.splitext(filename)[0]+'.xml'
        xml_path = os.path.join(source, xml_filename)
        filename_path = os.path.join(source, filename)
        
        #copy image + XML files across only if accompanying XML file exists
        if os.path.isfile(xml_path):
                shutil.copyfile(filename_path, os.path.join(train_dir, filename))
                shutil.copyfile(xml_path, os.path.join(train_dir, xml_filename))
        else:
            print("WARNING: the following XML file does not exist:" + xml_path)
