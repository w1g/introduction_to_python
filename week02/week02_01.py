import argparse
import json
import os
import tempfile

def wr(d, fl):
    with open(fl, 'a') as f:
        f.write(json.dumps(d) + '\n')

def rd(k, fl):
    l = []
    
    if not os.path.exists(fl):
        return l
        
    with open(fl, 'r') as f:
        s = f.readline()
        while s:
            d = json.loads(s)
            for tk, tv in d.items():
                if tk == k:
                    l.append(tv)
            s = f.readline()
    return l

if __name__ == '__main__':
    
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    

    parser = argparse.ArgumentParser()
    parser.add_argument("--key", help = "Key name", type=str)
    parser.add_argument("--val", help = "Value", type=str)
    parser.add_argument("--clear", help = "Delete the temporery storage file", action='store_true')
        
    args = parser.parse_args()
    
    if args.clear:
        os.remove(storage_path)
        
    if args.val != None:
        wr({args.key: args.val}, storage_path)
        
    if args.val == None:
        l = rd(args.key, storage_path)
        if l:
            s = ''
            for i in l[:len(l) - 1]:
                s += i + ', '
            s += l[len(l) - 1]
            print(s)
        else:
            print('')