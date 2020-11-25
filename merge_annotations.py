import glob
import os
import shutil

list_of_folders = []
texts_list = []

merged = "./merged"

while 1:
    folder_path = input('enter annotations catagorical path or enter q to quit\t')
    if folder_path.lower() == 'q':
        break
    list_of_folders.append(folder_path)

    texts = glob.glob(folder_path + '/*txt')
    base_texts = []
    for t in texts:
        base_t = os.path.basename(t)
        base_texts.append(base_t)
    texts_list.append(base_texts)

print(len(texts_list))


def get_marking(filenames=None):
    marking = []
    if filenames is not None:
        for filename in filenames:
            with open(filename) as f:
                lines = f.readlines()
                for l in lines:
                    marking.append(l)

    return marking


for t in texts_list[0]:
    print(t)
    j = 0
    filenames = []
    filenames.append(list_of_folders[j] + "/" + t)
    while 1:
        j += 1
        if j < len(texts_list):
            pass
        else:
            break
        if t in texts_list[j]:
            filenames.append(list_of_folders[j] + "/" + t)
    markings = get_marking(filenames=filenames)
    if os.path.exists('./merged/' + t):
        os.remove('./merged/' + t)
    with open('./merged/' + t, 'a') as f:
        for m in markings:
            f.write(m)