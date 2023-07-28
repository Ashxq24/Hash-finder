import sys
import os
import hashlib


def get_hash(filename):
    """prints a hex hash signature of the file passed in as arg"""
    try:
        # Read File
        f=open(filename, 'rb')
        file=f.read()
        # Generate Hash Signature
        file_hashingmd5 = hashlib.md5(file)
        file_hashingsha256 = hashlib.sha256(file)
        file_hashingsha1 = hashlib.sha1(file)
        print("MD5 =",file_hashingmd5.hexdigest())
        print ("SHA256 =",file_hashingsha256.hexdigest())
        print ("SHA1 =",file_hashingsha1.hexdigest())
	
    except Exception as err:
        print(f'[-] {err}')

    finally:
        if 'f' in locals():
            f.close()


def main():

    sysargv=str(input("Enter the path of the file to find its Hash :"))
    print(get_hash(sysargv))


if __name__ == '__main__':
    main()
