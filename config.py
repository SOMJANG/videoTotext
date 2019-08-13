IMAGE_CONFIG = {
    "resize_origin":
	{
		"standard_width": 512,
		"standard_height": 512
	},
	"gradient": 
	{
		"kernel_size_row":2,
		"kernel_size_col":2
	},
	"threshold": 
	{
		"mode": "mean",
		"block_size":15,
		"subtract_val": 21

	},
	"remove_line":
	{
		"threshold": 200,
		"min_line_length": 53, 
		"max_line_gap": 200
	},
	"close": 
	{
		"kernel_size_row": 25,
		"kernel_size_col": 10
	},
	"contour":
	{
		"min_width": 50,
		"min_height": 10
	}
}

RECO_CONFIG = {
    "tesseract": '/usr/local/Cellar/tesseract/4.1.0/bin/tesseract',
    "custom_oem_psm_config" : '--oem 3 --psm 6',
    "custom_config": '--psm 1 -c preserve_interword_spaces=1',
    "lang": 'kor'
}