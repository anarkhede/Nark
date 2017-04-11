# Created by Atul Narkhede @ 5/14/2016
# Takes a list of WMHF's and creates 1 csv per subject 
# for x, y, z, I, L (I for intensity and L for label)

import os
import nibabel as nib
import numpy as np

# Reads csv (of WMHF addresses) 
TXTList=input("Location of .txt with list of WMHF.nii: ")

with open(TXTList, 'r') as f:
  for WMHF_add in f:
    WMHF_add=WMHF_add.rstrip('\n')
    # Split address to create FLAIR path 
    FL_add=os.path.join(os.path.dirname(WMHF_add), 'FLAIR.nii')
    # Read FLAIR.nii and read WMHF.nii
    FL=nib.load(FL_add)
    WMHF=nib.load(WMHF_add)
    if FL.shape==WMHF.shape: # Check if they are the same size
      I_mat = FL.get_data() # Returns a numpy.nd array
      L_mat = WMHF.get_data()
      # Save csv at required location for further processing.
      os.chdir(os.path.dirname(WMHF_add))
      with open('XYZIL.txt','w') as xyzilfile:
        for idx, I in np.ndenumerate(I_mat):
          L_val=L_mat.item((idx[0],idx[1],idx[2]))
          # Write in a txt x, y, z, I, L
          xyzilfile.write(str(idx[0])+','+str(idx[1])+','+str(idx[2])+','+str(I)+','+str(L_val)+'\n')  
      xyzilfile.close()
    else:
      print("FLAIR and WMHF mismatch in: " + WMHF_add)
      
      
