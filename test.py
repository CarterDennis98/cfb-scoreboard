from PIL import Image, ImageDraw, ImageFont
from rgbmatrix import RGBMatrix, RGBMatrixOptions
import time


def run():
	draw.text((5,5), "Hello World", font=font, fill=(255,255,255,255))
	matrix.SetImage(image)
	time.sleep(100)



if __name__ == "__main__":

	options = RGBMatrixOptions()
	options.rows = 64
	options.cols = 64
	options.chain_length = 1
	options.parallel = 1
	options.gpio_slowdown = 2

	matrix = RGBMatrix(options=options)

	image = Image.new("RGB", (64, 64))

	draw = ImageDraw.Draw(image)

	font = ImageFont.load_default()

	run()
