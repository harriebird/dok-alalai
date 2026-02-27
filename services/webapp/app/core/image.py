import base64
import io

async def image_to_base64(image):
    readfile = await image.read()
    image_bytes = io.BytesIO(readfile)
    return base64.b64encode(image_bytes.getvalue()).decode("utf-8")
