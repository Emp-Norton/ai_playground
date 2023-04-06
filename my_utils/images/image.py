import openai, os 


def create_image(**kwargs):	
 	 """ # TODO Check for mechanism to ensure keyword args fit expected terms, e.g. "prompt","size", and not "fubar"
 	 Kwargs includes: prompt=<string>, n=<int>, size=<string> \n Example: openai.Images.create(prompt='description of image', n=3, size="512x512") """
# TODO Check for mechanism to ensure keyword args fit expected terms, e.g. "prompt","size", and not "fubar"
# TODO Add option to toggle API return between URL and Base64 PNG
# TODO Add logging and save to file function for PNG
	r = openai.Image.create(**kwargs)
	return r 