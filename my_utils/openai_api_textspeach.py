import os
import openai
import env 


def create_image(**kwargs):	
 	 """ Create an image or series of images fitting a given description (i.e. prompt). Kwargs includes: prompt=<string>, n=<int>, size=<string> \n Example: openai.Images.create(prompt='description of image', n=3, size="512x512") """
# TODO Check for mechanism to ensure keyword args fit expected terms, e.g. "prompt","size", and not "fubar"

def transcribe_audio():
	""" """"