FROM --platform=linux/amd64 python:3.9.19

#Add deface tools
COPY mri_deface_linux mri_deface_linux
COPY face.gca face.gca
COPY talairach_mixed_with_skull.gca talairach_mixed_with_skull.gca
RUN chmod +x mri_deface_linux



#Add the requirements .txt; probably flask, etc.
COPY requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt

#Add flask serer
RUN mkdir Uploads
COPY main.py main.py


#Start the python Flask Server
EXPOSE 8080
CMD ["python", "main.py"]