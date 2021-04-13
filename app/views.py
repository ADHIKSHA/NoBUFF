from django.shortcuts import render
import pymongo
from pymongo import MongoClient
import pandas 
import json
from gridfs import GridFS
from bson import objectid
from django.views.decorators.csrf import csrf_exempt
from app.models import *
from django.http import HttpResponse
import cv2
import numpy
# Create your views here.
class MongoDB(object):
	def __init__(self,dbName=None,collectionName=None):
		self.dbName = dbName
		self.collectionName=collectionName
		self.client = pymongo.MongoClient("mongodb+srv://root:root@cluster0.ce6lh.mongodb.net/videos?retryWrites=true&w=majority")
		self.DB=self.client[self.dbName]
		self.collection=self.DB[self.collectionName]

	def  InsertData(self):
		fs= GridFS(self.DB,"video")
		stream = open(u'F:\\vids\\rec1.mp4', "rb")
		#bytes = bytearray(stream.read())
		#numpyarray = numpy.asarray(bytes, dtype=numpy.uint8)
		#bgrImage = cv2.imdecode(numpyarray, cv2.IMREAD_UNCHANGED)
		video = fs.put(stream,content_type='video/mp4',filename='rec1.mp4')
		print("Inserted the data !")

	def showData(self):
		fs= GridFS(self.DB,"video")
		f = fs.get_last_version(filename="rec1.mp4")
		return f

@csrf_exempt
def homepage(request):
	#mongodb=MongoDB(dbName='videos',collectionName='video')
	#mongodb.InsertData()
	#stream = mongodb.showData()
	return render(request,'Landingpage.html')
