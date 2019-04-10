import cv2
import glob

# Cleaning up variables to prevent loading data multiple times (which may cause memory issue)
try:
   del EOSINOPHIL,LYMPHOCYTE
   del MONOCYTE, NEUTROPHIL, All_cell
   print('Clear previously loaded data.')
except:
   pass

path = "./data"
EOSINOPHIL = [cv2.imread(file) for file in glob.glob(path+"/*.jpeg")]
sam_eosino = len(EOSINOPHIL)
print(sam_eosino)

print(5)
