from os import listdir, remove
labels = listdir('../data/BIO/all/labels/FirstPage')
images = listdir('../data/BIO/all/images/FirstPage')
for image in images:
    if '{}.{}'.format(image.split('.')[0], 'txt') not in labels:
        print('Going to remove %s' % image)
        remove('../data/BIO/all/images/FirstPage/%s' % image)