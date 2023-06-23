import pandas as pd
import sys

def txt2csv(filename):
    with open(filename) as f:
        contents = f.readlines()
    
    lst = []
    for l in contents:
        lst.append(l)
    
    datacontent = {'docs': lst}
    
    df = pd.DataFrame(data=datacontent)
    
    csvfilename = filename[:-4]+'.csv'
    df.to_csv(csvfilename)
    
    excelfilename = filename[:-4]+'.xlsx'
    df.to_excel(excelfilename)
    
    
    
''' -------------------------------------- '''    
''' ---------------- Main ---------------- '''
def main():
    filename = sys.argv[1]
    txt2csv(filename)
    
''' ---------------------------------------'''
if __name__ == "__main__":  
    main()
