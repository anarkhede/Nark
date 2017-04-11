# Created by Atul Narkhede on 18 Oct 2016
# Takes the Study Buffer folder containing DICOM's and organizes in the following format:
# ./Study/DICOM/Sequence/dicom_files
# ./Study/Sequence/nifti_files
# ./Study/Analysis/Proc_files

import os
import pydicom as dicom
import shutil

# Takes users input of path as a string
study_path = input('Please Enter Study Path: ')

# Use walk to get the list of files and organize into Study/Sub/DICOM/Seq
for dirpath, dirs, files in os.walk(study_path):
    for f in files:
        try:  # So we continue the loop without exiting
            dcm_hdr = dicom.read_file(os.path.join(dirpath, f))  # Get dicom header
            Sub = dcm_hdr.PatientID
            Seq = dcm_hdr.SeriesDescription
            if not os.path.exists(os.path.join(study_path, Sub)):
                os.makedirs(os.path.join(study_path, Sub))
                os.makedirs(os.path.join(study_path, Sub, 'DICOM'))
            elif not os.path.exists(os.path.join(study_path, Sub, 'DICOM', Seq)):
                os.makedirs(os.path.join(study_path, Sub, 'DICOM', Seq))
            shutil.move(os.path.join(dirpath, f), os.path.join(study_path, Sub, 'DICOM', Seq))
        except:
            pass

# Convert DICOM's into Nifti's and move them to Study/Sub/Seq

# Make Directories for Analysis

#os.makedirs(os.path.join(study_path))
