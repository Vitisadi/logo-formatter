import argparse
from PIL import Image

def has_transparency(img):
    """Check if an image has transparency."""
    if img.mode == "P":
      transparent = img.info.get("transparency", -1)
      for _, index in img.getcolors():
         if index == transparent:
               return True
    elif img.mode == "RGBA":
      extrema = img.getextrema()
      if extrema[3][0] < 255:
         return True
    return False

def convert_and_resize_image(source_image_path, target_image_path, new_size):
   # Attempt to open   
   try:
      image = Image.open(source_image_path).convert("RGBA")
   except FileNotFoundError:
      print(f"Error: The file '{source_image_path}' was not found. Exiting.")
      return

   # Only process transparent
   if not has_transparency(image):
      print("The provided image does not have transparency. Exiting.")
      return
   
   new_image = Image.new("RGBA", image.size, (0, 0, 0, 0))
   
   for x in range(image.width):
      for y in range(image.height):
         
         r, g, b, a = image.getpixel((x, y))

         if a != 0:
               new_image.putpixel((x, y), (0, 0, 0, a))
   
   resized_image = new_image.resize(new_size)
   
   resized_image.save(target_image_path)

if __name__ == '__main__':
   parser = argparse.ArgumentParser(description='Convert and resize an image.')
   parser.add_argument('source_image_path', type=str, help='Path to the source image')
   
   args = parser.parse_args()

   target_image_path = "resized-image.png";
   new_size = (4000, 4000);
   convert_and_resize_image(args.source_image_path, target_image_path, new_size)
