
from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np

def clasificador(image):
    # Disable scientific notation for clarity
  np.set_printoptions(suppress=True)

  # Load the model
  model = load_model("keras_model.h5", compile=False)

  # Load the labels
  class_names = open("labels.txt", "r").readlines()

  # Create the array of the right shape to feed into the keras model
  # The 'length' or number of images you can put into the array is
  # determined by the first position in the shape tuple, in this case 1
  data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

  # Replace this with the path to your image
  image = Image.open(image).convert("RGB")

  # resizing the image to be at least 224x224 and then cropping from the center
  size = (224, 224)
  image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

  # turn the image into a numpy array
  image_array = np.asarray(image)

  # Normalize the image
  normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

  # Load the image into the array
  data[0] = normalized_image_array

  # Predicts the model
  prediction = model.predict(data)
  index = np.argmax(prediction)
  class_name = class_names[index]
  confidence_score = prediction[0][index]

  # Print prediction and confidence score
  print("Clase:", class_name[2:], end="")
  print("Porcentaje de coincidencia:", confidence_score)

  print(class_name)


  if class_name[2:] == "Freezer\n":
    return("Identifico un Refrigerador. Mis recomendaciones son: Cierra bien las puertas, evita abrir tan seguido el refrigerador y evita sobrecargar el interior para que el refrigerador funcione óptimamente.  La electricidad utilizada para alimentarlo produce gases invernaderos (Co2), ya que esta energía generalmente se genera quemando combustibles fósiles. Un refrigerador eficiente consume menos electricidad y usa refrigerantes con menor potencial de calentamiento global. Informate sobre las emisiones de dioxido de carbono con el comando <$co2>.")
  elif class_name[2:] == "Microondas\n":
    return("Identifico un Microondas/horno electrico. Mis recomendaciones son: Desenchúfalo cuando no se use, aunque el microondas en modo de espera consume poca energía, desconectarlo puede ayuda a reducir el consumo innecesario de energía electrica. Informate sobre las emisiones de dioxido de carbono con el comando <$co2>.")
  elif class_name[2:] == "TV\n":
    return("Identifico una sala de estar con TV. Mis recomendaciones son: Evita dejar la TV en modo de espera o dejar prendida la pantalla sin ocuparla. Desconecta si no planeas usarla por un tiempo ayuda a recudir el consumo electrico. Informate sobre las emisiones de dioxido de carbono con el comando <$co2>.")
  elif class_name[2:] == "PC\n":
    return("Identifico un estudio/oficina/setup gamer. Mis recomendaciones son: Apaga y/o desconecta monitores, impresoras y otros periféricos cuando no estén en uso para evitar el consumo en espera a ser usados. Configura la PC y activa el modo eficiencia energetica, y entrar en modo de suspensión o hibernación cuando no se usen. Especificamente las computadoras con componentes más profesionales consumen más, por lo que puede hacer una gran diferencia aplicar este consejo. Informate sobre las emisiones de dioxido de carbono con el comando <$co2>.")

