import shutil, random, os

bucket_path = '/home/zachary_zhu/data/csci1430-final-project-ghibli'

train_path = '/home/zachary_zhu/Ghibli-Style-Transfer/data/trainB'
test_path = '/home/zachary_zhu/Ghibli-Style-Transfer/data/testB'

dirnames = os.listdir(bucket_path + '/imgs')

for movie in dirnames:
    moviePath = bucket_path + '/imgs/' + movie

    allfiles = os.listdir(moviePath)

    cutoff = len(allfiles) // 10

    for filename in allfiles:
        srcpath = os.path.join(moviePath, filename)
        if random.uniform(0, len(allfiles)) < cutoff:
            shutil.copy(srcpath, test_path)
        else:
            shutil.copy(srcpath, train_path)
