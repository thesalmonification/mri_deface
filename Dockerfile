FROM python:3.9.19

#Add files
COPY main.py main.py
COPY mri_deface_linux mri_deface_linux
COPY face.gca face.gca
COPY talairach_mixed_with_skull.gca talairach_mixed_with_skull.gca


#TODO:
#Add the requirements .txt; probably flask, etc.
COPY requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt


#Start the python Flask Server
CMD ["python", "main.py"]