import warnings
warnings.filterwarnings("ignore")

import torch
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration


class ImageCaptionGenerator:
    def __init__(self):
        model_name = "Salesforce/blip-image-captioning-base"

        self.device = "cuda" if torch.cuda.is_available() else "cpu"

        self.processor = BlipProcessor.from_pretrained(model_name)
        self.model = BlipForConditionalGeneration.from_pretrained(model_name)
        self.model.to(self.device)
        self.model.eval()

    def prepare_image(self, image):
        if image.mode != "RGB":
            image = image.convert("RGB")

        image = image.copy()
        image.thumbnail((384, 384))
        return image

    def generate_caption(self, image, prompt=None):
        image = self.prepare_image(image)

        if prompt:
            inputs = self.processor(image, prompt, return_tensors="pt").to(self.device)
        else:
            inputs = self.processor(image, return_tensors="pt").to(self.device)

        with torch.inference_mode():
            output = self.model.generate(
                **inputs,
                max_new_tokens=28,
                num_beams=3,
                do_sample=False
            )

        caption = self.processor.decode(output[0], skip_special_tokens=True)
        return caption.strip()

    def generate_caption_candidates(self, image):
        prompts = [
            None,
            "a photo of",
            "an image of",
            "a person in",
            "a detailed photo of"
        ]

        captions = []

        for prompt in prompts:
            caption = self.generate_caption(image, prompt)
            if caption and caption not in captions:
                captions.append(caption)

        return captions