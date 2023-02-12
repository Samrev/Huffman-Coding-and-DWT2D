import pywt,numpy as np
from PIL import Image

#------------------------------------------------------------------#
# Convert a image into grayscale and load a image into numpy array #                   #
#------------------------------------------------------------------#

def load_image(img):
	img = Image.open(img).convert('L')
	img.load()
	data = np.asarray(img, dtype="int32" )
	return data

def save_image(array, img) :
	array = array.astype(np.uint8)
	im = Image.fromarray(array)
	im.save(img)
	return im

img = load_image("Images/sample.webp")
# print(img)
# print(img.shape)
# im_out = save_image(img, "sample_out.webp")
# im_out.show()

#----------------------------------------------------------------#
#                    Multilevel Decomposition                    #
#----------------------------------------------------------------#
def Haar2D(img,lev):
	coeffs = pywt.wavedec2(img, 'haar', level=lev)
	return coeffs

#----------------------------------------------------------------#
#                    Inverse  DWT                                #
#----------------------------------------------------------------#
def InvHaar2D(coeffs):
	reimg = pywt.waverec2(coeffs, 'haar')
	return reimg

#----------------------------------------------------------------#
#                      3-scale DWT                               #
#----------------------------------------------------------------#

# img = np.array([[1,2],[3,4]])
coeffs = Haar2D(img , 3)
'''(cA3,(cH3,cV3,cD3),(cH2,cV2,cD2),(cH1,cV1,cD1))
 where cA3 is a approximation coefficient and cHi,cVi,cDi's are detail coefficient'''

reimg = InvHaar2D(coeffs)
re_im_out = save_image(reimg, "Images/Output/sample_rec.webp")
# re_im_out.show()

#----------------------------------------------------------------#
#            Scaling the detail coefficient                      #
#----------------------------------------------------------------#

'''In the case of the Haar wavelet, the detail coefficients are typically 
scaled by a factor of 0.5. This is because the Haar wavelet 
has a simple structure, and scaling the detail coefficients by a factor 
of 0.5 ensures that 
the energy balance is maintained in the transformed image.'''

def scale_detail_coefficients(coeffs,scaling_factor):
	for i in range(1,len(coeffs)):
		coeffs[i] = [d*scaling_factor for d in coeffs[i]]
	return coeffs

coeffs = scale_detail_coefficients(coeffs,0.5)
reimg = InvHaar2D(coeffs)
# print(reimg)
re_im_out = save_image(reimg, "Images/Output/scaled_image.webp")
# re_im_out.show()


#----------------------------------------------------------------#
#            Wavelet Transform Modifications                     #
#----------------------------------------------------------------#

'''Reducing the size of our input image in half by row-column deletion, and
padding it with 0s to obtain a 512 × 512 array.'''

def reduce(img):
	''' We are reducing the image by half by taking every alternate row
	and coloumn and then paddding with zeros to make it a 512*512 size'''

	img = img[::2, ::2]
	(r,c) = img.shape
	padding = np.zeros((512, 512))
	padding[:r, :c] = img
	return padding

def zeroA(coeffs):
	coeffsA = coeffs.copy()
	coeffsA[0] = coeffsA[0]*0
	return coeffsA

def zerodetail(coeffs , detail):
	#detail = 0 --> horizonatl
	#detail = 1 --> vertical
	#detail = 2 --> diagonal

	coeffsdetail = coeffs.copy()
	for i in range(1,len(coeffsdetail)):
		coeffsdetail[i] = list(coeffsdetail[i])
		coeffsdetail[i][detail] = coeffsdetail[i][detail]*0
	return coeffsdetail

reduced_img = reduce(img)
re_im_out = save_image(reduced_img, "Images/Output/sample_reduced_and_padded.webp")
# re_im_out.show()

#----------------------------------------#
#            Scale = 1                   #
#----------------------------------------#

coeffs = Haar2D(reduced_img , 1)

#zeroing approximatioin coefficients
coeffsA = zeroA(coeffs)
reimg = InvHaar2D(coeffsA)
re_im_out = save_image(reimg, "Images/Output/sample_scale1_reduced_and_padded_zeroA.webp")
# re_im_out.show()

#zeroing horizontal coefficients
coeffsdetail1 = zerodetail(coeffs,0)
reimg = InvHaar2D(coeffsdetail1)
re_im_out = save_image(reimg, "Images/Output/sample_scale1_reduced_and_padded_zeroH.webp")
# re_im_out.show()

#zeroing vertical coefficients
coeffsdetail2 = zerodetail(coeffs,1)
reimg = InvHaar2D(coeffsdetail2)
re_im_out = save_image(reimg, "Images/Output/sample_scale1_reduced_and_padded_zeroV.webp")
# re_im_out.show()

#zeroing both horizontal and vertical coefficients
coeffsdetail12 = zerodetail(coeffs,0)
coeffsdetail12 = zerodetail(coeffsdetail12,1)
reimg = InvHaar2D(coeffsdetail12)
re_im_out = save_image(reimg, "Images/Output/sample_scale1_reduced_and_padded_zeroHV.webp")
# re_im_out.show()

#----------------------------------------#
#            Scale = 2                   #
#----------------------------------------#

coeffs = Haar2D(reduced_img , 2)

#zeroing approximatioin coefficients
coeffsA = zeroA(coeffs)
reimg = InvHaar2D(coeffsA)
re_im_out = save_image(reimg, "Images/Output/sample_scale2_reduced_and_padded_zeroA.webp")
# re_im_out.show()


#zeroing horizontal coefficients
coeffsdetail1 = zerodetail(coeffs,0)
reimg = InvHaar2D(coeffsdetail1)
re_im_out = save_image(reimg, "Images/Output/sample_scale2_reduced_and_padded_zeroH.webp")
# re_im_out.show()

#zeroing vertical coefficients
coeffsdetail2 = zerodetail(coeffs,1)
reimg = InvHaar2D(coeffsdetail2)
re_im_out = save_image(reimg, "Images/Output/sample_scale2_reduced_and_padded_zeroV.webp")
# re_im_out.show()

#zeroing both horizontal and vertical coefficients
coeffsdetail12 = zerodetail(coeffs,0)
coeffsdetail12 = zerodetail(coeffsdetail12,1)
reimg = InvHaar2D(coeffsdetail12)
re_im_out = save_image(reimg, "Images/Output/sample_scale2_reduced_and_padded_zeroHV.webp")
# re_im_out.show()


#----------------------------------------#
#            Scale = 3                   #
#----------------------------------------#

coeffs = Haar2D(reduced_img , 3)

#zeroing approximatioin coefficients
coeffsA = zeroA(coeffs)
reimg = InvHaar2D(coeffsA)
re_im_out = save_image(reimg, "Images/Output/sample_scale3_reduced_and_padded_zeroA.webp")
# re_im_out.show()

#zeroing horizontal coefficients
coeffsdetail1 = zerodetail(coeffs,0)
reimg = InvHaar2D(coeffsdetail1)
re_im_out = save_image(reimg, "Images/Output/sample_scale3_reduced_and_padded_zeroH.webp")
# re_im_out.show()

#zeroing vertical coefficients
coeffsdetail2 = zerodetail(coeffs,1)
reimg = InvHaar2D(coeffsdetail2)
re_im_out = save_image(reimg, "Images/Output/sample_scale3_reduced_and_padded_zeroV.webp")
# re_im_out.show()

#zeroing both horizontal and vertical coefficients
coeffsdetail12 = zerodetail(coeffs,0)
coeffsdetail12 = zerodetail(coeffsdetail12,1)
reimg = InvHaar2D(coeffsdetail12)
re_im_out = save_image(reimg, "Images/Output/sample_scale3_reduced_and_padded_zeroHV.webp")
# re_im_out.show()

#----------------------------------------#
#            Scale = 4                   #
#----------------------------------------#

coeffs = Haar2D(reduced_img , 4)

#zeroing approximatioin coefficients
coeffsA = zeroA(coeffs)
reimg = InvHaar2D(coeffsA)
re_im_out = save_image(reimg, "Images/Output/sample_scale4_reduced_and_padded_zeroA.webp")
# re_im_out.show()


#zeroing horizontal coefficients
coeffsdetail1 = zerodetail(coeffs,0)
reimg = InvHaar2D(coeffsdetail1)
re_im_out = save_image(reimg, "Images/Output/sample_scale4_reduced_and_padded_zeroH.webp")
# re_im_out.show()

#zeroing vertical coefficients
coeffsdetail2 = zerodetail(coeffs,1)
reimg = InvHaar2D(coeffsdetail2)
re_im_out = save_image(reimg, "Images/Output/sample_scale4_reduced_and_padded_zeroV.webp")
# re_im_out.show()

#zeroing both horizontal and vertical coefficients
coeffsdetail12 = zerodetail(coeffs,0)
coeffsdetail12 = zerodetail(coeffsdetail12,1)
reimg = InvHaar2D(coeffsdetail12)
re_im_out = save_image(reimg, "Images/Output/sample_scale4_reduced_and_padded_zeroHV.webp")
# re_im_out.show()


#----------------------------------------#
#            Scale = 5                   #
#----------------------------------------#

coeffs = Haar2D(reduced_img , 5)

#zeroing approximatioin coefficients
coeffsA = zeroA(coeffs)
reimg = InvHaar2D(coeffsA)
re_im_out = save_image(reimg, "Images/Output/sample_scale5_reduced_and_padded_zeroA.webp")
# re_im_out.show()


#zeroing horizontal coefficients
coeffsdetail1 = zerodetail(coeffs,0)
reimg = InvHaar2D(coeffsdetail1)
re_im_out = save_image(reimg, "Images/Output/sample_scale5_reduced_and_padded_zeroH.webp")
# re_im_out.show()

#zeroing vertical coefficients
coeffsdetail2 = zerodetail(coeffs,1)
reimg = InvHaar2D(coeffsdetail2)
re_im_out = save_image(reimg, "Images/Output/sample_scale5_reduced_and_padded_zeroV.webp")
# re_im_out.show()

#zeroing both horizontal and vertical coefficients
coeffsdetail12 = zerodetail(coeffs,0)
coeffsdetail12 = zerodetail(coeffsdetail12,1)
reimg = InvHaar2D(coeffsdetail12)
re_im_out = save_image(reimg, "Images/Output/sample_scale5_reduced_and_padded_zeroHV.webp")
# re_im_out.show()


#----------------------------------------#
#            Scale = 6                   #
#----------------------------------------#

coeffs = Haar2D(reduced_img , 6)

#zeroing approximatioin coefficients
coeffsA = zeroA(coeffs)
reimg = InvHaar2D(coeffsA)
re_im_out = save_image(reimg, "Images/Output/sample_scale6_reduced_and_padded_zeroA.webp")
# re_im_out.show()


#zeroing horizontal coefficients
coeffsdetail1 = zerodetail(coeffs,0)
reimg = InvHaar2D(coeffsdetail1)
re_im_out = save_image(reimg, "Images/Output/sample_scale6_reduced_and_padded_zeroH.webp")
# re_im_out.show()

#zeroing vertical coefficients
coeffsdetail2 = zerodetail(coeffs,1)
reimg = InvHaar2D(coeffsdetail2)
re_im_out = save_image(reimg, "Images/Output/sample_scale6_reduced_and_padded_zeroV.webp")
# re_im_out.show()

#zeroing both horizontal and vertical coefficients
coeffsdetail12 = zerodetail(coeffs,0)
coeffsdetail12 = zerodetail(coeffsdetail12,1)
reimg = InvHaar2D(coeffsdetail12)
re_im_out = save_image(reimg, "Images/Output/sample_scale6_reduced_and_padded_zeroHV.webp")
# re_im_out.show()


#----------------------------------------#
#            Scale = 7                   #
#----------------------------------------#

coeffs = Haar2D(reduced_img , 7)

#zeroing approximatioin coefficients
coeffsA = zeroA(coeffs)
reimg = InvHaar2D(coeffsA)
re_im_out = save_image(reimg, "Images/Output/sample_scale7_reduced_and_padded_zeroA.webp")
# re_im_out.show()


#zeroing horizontal coefficients
coeffsdetail1 = zerodetail(coeffs,0)
reimg = InvHaar2D(coeffsdetail1)
re_im_out = save_image(reimg, "Images/Output/sample_scale7_reduced_and_padded_zeroH.webp")
# re_im_out.show()

#zeroing vertical coefficients
coeffsdetail2 = zerodetail(coeffs,1)
reimg = InvHaar2D(coeffsdetail2)
re_im_out = save_image(reimg, "Images/Output/sample_scale7_reduced_and_padded_zeroV.webp")
# re_im_out.show()

#zeroing both horizontal and vertical coefficients
coeffsdetail12 = zerodetail(coeffs,0)
coeffsdetail12 = zerodetail(coeffsdetail12,1)
reimg = InvHaar2D(coeffsdetail12)
re_im_out = save_image(reimg, "Images/Output/sample_scale7_reduced_and_padded_zeroHV.webp")
# re_im_out.show()

#----------------------------------------#
#            Scale = 8                   #
#----------------------------------------#

coeffs = Haar2D(reduced_img , 8)

#zeroing approximatioin coefficients
coeffsA = zeroA(coeffs)
reimg = InvHaar2D(coeffsA)
re_im_out = save_image(reimg, "Images/Output/sample_scale8_reduced_and_padded_zeroA.webp")
# re_im_out.show()


#zeroing horizontal coefficients
coeffsdetail1 = zerodetail(coeffs,0)
reimg = InvHaar2D(coeffsdetail1)
re_im_out = save_image(reimg, "Images/Output/sample_scale8_reduced_and_padded_zeroH.webp")
# re_im_out.show()

#zeroing vertical coefficients
coeffsdetail2 = zerodetail(coeffs,1)
reimg = InvHaar2D(coeffsdetail2)
re_im_out = save_image(reimg, "Images/Output/sample_scale8_reduced_and_padded_zeroV.webp")
# re_im_out.show()

#zeroing both horizontal and vertical coefficients
coeffsdetail12 = zerodetail(coeffs,0)
coeffsdetail12 = zerodetail(coeffsdetail12,1)
reimg = InvHaar2D(coeffsdetail12)
re_im_out = save_image(reimg, "Images/Output/sample_scale8_reduced_and_padded_zeroHV.webp")
# re_im_out.show()


#----------------------------------------------------------------#
#            Truncating Detail coefficient                       #
#----------------------------------------------------------------#

def truncate(coeffs , threshold):
	'''we are compressing the image by truncating the detail coefficients
	into -threshold to threshold'''

	'''A lower threshold will result in a higher level of compression but 
	lower image quality, as more detail coefficients will be truncated. 
	On the other hand, a higher threshold will result in lower 
	compression but higher image quality, as fewer detail coefficients will 
	be truncated.'''

	coeffs_truncate = coeffs.copy()
	for i in range(1,len(coeffs_truncate)):
		coeffs_truncate[i] = [np.clip(d,-threshold,threshold) for d in coeffs_truncate[i]]

	return coeffs_truncate

def quantization_error(img , reimg):

	'''We have calculated the quantization error by 
	 the root mean square error (RMSE) between the original image and i
	ts quantized version'''
	error = np.mean((img - reimg) ** 2)
	return error

#----------------------------------------#
#            Scale = 1                   #
#----------------------------------------#


coeffs = Haar2D(img , 1)
coeffs_truncate = truncate(coeffs,100) #threshold = 100
reimg = InvHaar2D(coeffs_truncate)
re_im_out = save_image(reimg, "Images/Output/sample_scale1_reduced_and_padded_truncate.webp")
#re_im_out.show()
error = quantization_error(img , reimg)
print("Quantization_error for scale 1: ",error)

#----------------------------------------#
#            Scale = 2                   #
#----------------------------------------#

coeffs = Haar2D(img , 2)
coeffs_truncate = truncate(coeffs,100) #threshold = 100
reimg = InvHaar2D(coeffs_truncate)
re_im_out = save_image(reimg, "Images/Output/sample_scale2_reduced_and_padded_truncate.webp")
#re_im_out.show()
error = quantization_error(img , reimg)
print("Quantization_error for scale 2: ",error)

#----------------------------------------#
#            Scale = 3                   #
#----------------------------------------#

coeffs = Haar2D(img , 3)
coeffs_truncate = truncate(coeffs,100) #threshold = 100
reimg = InvHaar2D(coeffs_truncate)
re_im_out = save_image(reimg, "Images/Output/sample_scale3_reduced_and_padded_truncate.webp")
#re_im_out.show()
error = quantization_error(img , reimg)
print("Quantization_error for scale 3: ",error)

#----------------------------------------#
#            Scale = 4                   #
#----------------------------------------#

coeffs = Haar2D(img , 4)
coeffs_truncate = truncate(coeffs,100) #threshold = 100
reimg = InvHaar2D(coeffs_truncate)
re_im_out = save_image(reimg, "Images/Output/sample_scale4_reduced_and_padded_truncate.webp")
#re_im_out.show()
error = quantization_error(img , reimg)
print("Quantization_error for scale 4: ",error)

#----------------------------------------#
#            Scale = 5                   #
#----------------------------------------#

coeffs = Haar2D(img , 5)
coeffs_truncate = truncate(coeffs,100) #threshold = 100
reimg = InvHaar2D(coeffs_truncate)
re_im_out = save_image(reimg, "Images/Output/sample_scale5_reduced_and_padded_truncate.webp")
#re_im_out.show()
error = quantization_error(img , reimg)
print("Quantization_error for scale 5: ",error)

#----------------------------------------#
#            Scale = 6                   #
#----------------------------------------#

coeffs = Haar2D(img , 6)
coeffs_truncate = truncate(coeffs,100) #threshold = 100
reimg = InvHaar2D(coeffs_truncate)
re_im_out = save_image(reimg, "Images/Output/sample_scale6_reduced_and_padded_truncate.webp")
#re_im_out.show()
error = quantization_error(img , reimg)
print("Quantization_error for scale 6: ",error)

#----------------------------------------#
#            Scale = 7                   #
#----------------------------------------#

coeffs = Haar2D(img , 7)
coeffs_truncate = truncate(coeffs,100) #threshold = 100
reimg = InvHaar2D(coeffs_truncate)
re_im_out = save_image(reimg, "Images/Output/sample_scale7_reduced_and_padded_truncate.webp")
#re_im_out.show()
error = quantization_error(img , reimg)
print("Quantization_error for scale 7: ",error)

#----------------------------------------#
#            Scale = 8                   #
#----------------------------------------#

coeffs = Haar2D(img , 8)
coeffs_truncate = truncate(coeffs,100) #threshold = 100
reimg = InvHaar2D(coeffs_truncate)
re_im_out = save_image(reimg, "Images/Output/sample_scale8_reduced_and_padded_truncate.webp")
#re_im_out.show()
error = quantization_error(img , reimg)
print("Quantization_error for scale 8: ",error)



























































