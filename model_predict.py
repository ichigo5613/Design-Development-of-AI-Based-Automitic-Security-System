#import cv2
import numpy as np
from matplotlib.pyplot import imread
from matplotlib.pyplot import imshow
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.imagenet_utils import decode_predictions
from tensorflow.keras.applications.imagenet_utils import preprocess_input
from tensorflow.keras.models import load_model
loaded_model_imageNet = load_model("main_model.h5")
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
import io
from PIL import Image
import cv2

import serial

try:
    print("[INFO] Connecting To Board")
    ser = serial.Serial('COM5', 9600, timeout=1)     #enter ur arduino COM port number
    print("Sucessfully Connected")
except:
    print("[INFO] Failed To Connect To Board Check COM Port Number And Connection")
    pass

disease_dic= ['Akash','Preetam','Roja','Sandhya','Unknown']
def irish_detection(image_path):				 


				img = image.load_img(image_path, target_size=(256,256))
				x = image.img_to_array(img)
				x = np.expand_dims(x, axis=0)
				x = preprocess_input(x)
				result = loaded_model_imageNet.predict(x)
				print((result*100).astype('int'))
				final_list_result=(result*100).astype('int')
				list_vals=list(final_list_result[0])
				result_val=max(list(final_list_result[0]))
				print(result_val)
				index_result = list_vals.index(result_val)

				#return   index_result

#print(pred_leaf_disease('corn.JPG'))



	            # Convert prediction to string label
				prediction_label = str(disease_dic[index_result])
				t = prediction_label
				#disease_dic = ['Akash', 'Preetam', 'Roja', 'Sandhya', 'Unknown']
				if t != "Unknown" and all(name in disease_dic for name in ['Akash', 'Preetam', 'Roja', 'Sandhya']):
    						print("open door")
    						ser.write(b'1')
				else:
    						print("close door")
    						ser.write(b'0')

				return prediction_label



#rslt=irish_detection('WIN_20240419_15_55_15_Pro.jpg')

#print(rslt)
