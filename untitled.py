import sys
import glob
import hashlib
import time

dirname = sys.argv[1]   # get the argument (dirname) from the user

results = {}

for one_filename in glob.glob(f'{dirname}/*'):

    try:
        digest = hashlib.file_digest(open(one_filename, 'rb'), 'sha1')
        results[one_filename] = digest.hexdigest()
    except Exception as e:
        pass

    time.sleep(0.1)

for key, value in results.items():
    print(f'{key}: {value}')