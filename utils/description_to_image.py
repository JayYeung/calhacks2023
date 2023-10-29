import together
from functools import cache
import base64
from PIL import Image
from io import BytesIO
from IPython.display import display
from random import randint
from time import sleep

together.api_key = 'dd6fc37975f3b9e88b25fa63b1ddd22ad6043a4449c39d061ffc6c8117a85f33'

@cache
def description_to_image(description: str, index: int):
    try: 
        model_list = together.Models.list()

        output = together.Image.create(
            prompt = description + ' in color', 
            model = "SG161222/Realistic_Vision_V3.0_VAE",
            width = 512, 
            height = 512,
            steps = 20,
            seed = randint(0, 100)
        )
        
        base64_string = output['output']['choices'][0]['image_base64']
        image_data = base64.b64decode(base64_string)
        image_buffer = BytesIO(image_data)
        image = Image.open(image_buffer)
        image.save(f'static/{index}.png')
    except Exception as e:
        print(e)
        sleep(3)
        description_to_image(description, index)