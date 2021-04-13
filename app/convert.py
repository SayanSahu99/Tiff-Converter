import os
import cv2
from zipfile import ZipFile
from app import app

def convert_jpg(files):
  # create a ZipFile object
  zipObj = ZipFile('sample.zip', 'w')
  # Add multiple files to the zip
  for file in files:
    path = os.path.join(app.config['UPLOAD_PATH'], file.filename)
    outfile = path.split('.')[0] + '.jpg'
    read = cv2.imread(path)
    # Convert to .jpg
    cv2.imwrite(outfile,read,[int(cv2.IMWRITE_JPEG_QUALITY), 200])
    zipObj.write(outfile, arcname=file.filename.split('.')[0] + '.jpg')
  # close the Zip File
  zipObj.close()
  delete()

def convert_png(files):
  # create a ZipFile object
  zipObj = ZipFile('sample.zip', 'w')
  # Add multiple files to the zip
  for file in files:
    path = os.path.join(app.config['UPLOAD_PATH'], file.filename)
    outfile = path.split('.')[0] + '.png'
    read = cv2.imread(path)
    # Convert to .png
    cv2.imwrite(outfile, read)
    zipObj.write(outfile, arcname=file.filename.split('.')[0] + '.png')
  # close the Zip File
  zipObj.close()
  delete()

def delete():
  #delete uploads dir files
  dir = app.config['UPLOAD_PATH']
  for f in os.listdir(dir):
    os.remove(os.path.join(dir, f))