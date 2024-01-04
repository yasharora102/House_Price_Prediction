# compress files to pbz2
import os
import bz2file as bz2
import pickle
# get files 
def fetch_files(folder_name):
    files = []
    for file in os.listdir(folder_name):
        if file.endswith(".pkl"):
            files.append(os.path.join(folder_name, file))
    return files


# compress files

def compress_pickle(file_list):
    for file in file_list:
        data = pickle.load(open(file, "rb"))
        compressed_pickle = bz2.BZ2File(file + ".pbz2", "wb")
        pickle.dump(data, compressed_pickle)
        compressed_pickle.close()
        print(f"{file} Compressed")


def main():
    # get files
    folder_name = "training"
    files = fetch_files(folder_name)
    # compress files
    compress_pickle(files)

    # delete files
    for file in files:
        os.remove(file)


if __name__ == "__main__":
    main()