import shutil, random, os

bucket_path = '/home/zachary_zhu/data/csci1430-final-project-ghibli'

train_path = '/home/zachary_zhu/Ghibli-Style-Transfer/data/trainA'
test_path = '/home/zachary_zhu/Ghibli-Style-Transfer/data/testA'

dirnames = os.listdir(bucket_path + '/flickr')

folderPath = bucket_path + '/flickr'

allfiles = os.listdir(folderPath)

cutoff = len(allfiles) // 10

for filename in allfiles:
    srcpath = os.path.join(folderPath, filename)
    if random.uniform(0, len(allfiles)) < cutoff:
        shutil.copy(srcpath, test_path)
    else:
        shutil.copy(srcpath, train_path)
