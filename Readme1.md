# Project Nark Created by Atul Narkhede @ 05/10/2016

This project creates a semi-automated (for now) data analysis pipeline

Acquire.py: Takes a Study directory containing DICOM's creates a list of the files, checks if they are DICOM's organizes them as
in Study/Subject/DICOM/Sequence; converts each of these sequences into nifti's and organizes them in Study/Subject/Sequence
It renames the sequence folders to standard names (using look-up directories) and finally cleans the sequence folder with multiple
nifti's (for 3DT1, FLAIR and DTI) to required number (1,1,3) files set by user.

Create_dbs.py: Using above structure creates databases for each study with fields: Study Name, Data acq Date, Subj ID, Seq Name,
Analysis (type) Begin Date, Analysis Manual Correction (done, not done), Post Manual Calculations, Results, Closing Date.

Also, populates the fields as and when they exist

Request.py: Requests the user for type of analysis to be performed, populates the database with new fields and fills values 
as it gets processed. It performes the first automated steps for the related analysis.

Analysis: 
WMH.py: 

FS.py: 

DTI.py

Results.py
