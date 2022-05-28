import argparse
import os.path
import os
import filecmp
    			

def Check_Directory(umar1, umar2):
    differentiate = filecmp.dircmp(dir1, dir2)
    if (differentiate.left_only or differentiate.right_only or differentiate.common_files or differentiate.diff_files):
        return False
    for subdir in compared.common_dirs:
        if not Check_Directory(os.path.join(umar1, subumardir), os.path.join(umar2, subumardir2)):
            return False
    return True
    	
def Check_file_in_Dir(file, dir):
	if(os.path.isdir(dir)==True):
		if(os.scandir(dir)):
			entry = os.scandir(dir)
			for entries in entry:
				if file == entries: 
					return True
				else:
					Check_Dir_File(file, dir+'/'+entries)
	return False

def Check_For_Files(file1, file2):
    if file1 != file2:
    	return False
    else:
    	return True
    	


if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('f1', help='path of first file')
    parser.add_argument('f2', help='path of second file')
    args = parser.parse_args()
    file1 = args.f1
    file2 = args.f2
    
    if os.path.isfile(file1) and os.path.isfile(file2):
    	x = Check_For_Files(file1, file2)
    	
    elif os.path.isdir(file1) and os.path.isdir(file2):
    	x = Check_Directory(file1, file2)
    	
    else:
    	if os.path.isfile(file1) and os.path.isdir(file2):
    		x = Check_file_in_Dir(file1, file2)
    	else:
    	    x = Check_file_in_Dir(file2, file1)	
    		 			    	
    if (x):
        print("found")
    else:
    	print("Not found")
    

