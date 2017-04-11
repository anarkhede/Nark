# Takes in Study folder location and organizes files based on patientid, study and sequence information, if its a dicom.
# Using package pydicom called as dicom

import os
import dicom

fld = raw_input("Please enter Study Folder path: ")

for p, d, f in os.walk(fld):
    for name in f:
        try:
            dcm_info = dicom.read_file(os.path.join(p, name))
            PId = dcm_info.PatientID
            PId = PId.replace('WHICAP_', '')
            seq = dcm_info.SeriesDescription
            seq = seq.replace(' ', '')  # remove spaces
            seq = seq.replace('/', '')  # remove /
            # Seq to Std format
            if 'MPRAGE' in seq:
                seq = '3DT1'
            if '3D' in seq and 'FLAIR' in seq:
                seq = 'FLAIR'
            if 'DTI' in seq:
                seq = 'DTI'

            if not os.path.isdir(os.path.join(fld, PId)):
                os.makedirs(os.path.join(fld, PId))
            if not os.path.isdir(os.path.join(fld, PId, 'DICOM', seq)):
                os.makedirs(os.path.join(fld, PId, seq))
                os.makedirs(os.path.join(fld, PId, 'DICOM', seq))
            os.rename(os.path.join(p, name), os.path.join(fld, PId, 'DICOM', seq, name))

        except:
            print ('This is not a DICOM: ' + os.path.join(p, name))
