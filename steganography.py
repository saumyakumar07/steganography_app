from PIL import Image

# Function to hide text inside an image
def encode_message(image_path, message, output_path):
    image = Image.open(image_path)
    encoded_image = image.copy()

    # Convert message to binary
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    binary_message += '1111111111111110'  # Delimiter to indicate end of message

    pixels = list(encoded_image.getdata())
    new_pixels = []

    message_index = 0
    for pixel in pixels:
        new_pixel = list(pixel)
        for i in range(3):  # Modify RGB values
            if message_index < len(binary_message):
                new_pixel[i] = (new_pixel[i] & ~1) | int(binary_message[message_index])
                message_index += 1
        new_pixels.append(tuple(new_pixel))

    encoded_image.putdata(new_pixels)
    encoded_image.save(output_path, "PNG")  # Ensure PNG format to prevent compression
    return output_path


# Function to extract hidden text from an image
def decode_message(image_path):
    image = Image.open(image_path)
    pixels = list(image.getdata())

    binary_message = ''
    for pixel in pixels:
        for i in range(3):  # Extract from RGB values
            binary_message += str(pixel[i] & 1)

    # Find the delimiter (16-bit '1111111111111110')
    end_marker = '1111111111111110'
    end_index = binary_message.find(end_marker)

    if end_index != -1:  # If delimiter found, extract only valid message
        binary_message = binary_message[:end_index]
    else:
        print("⚠️ Warning: No end marker found. Extracted data may be incorrect!")

    # Convert binary message back to text
    message = ''
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        if len(byte) == 8:  # Ensure we have full 8-bit chunks
            char = chr(int(byte, 2))
            if char.isprintable():  # Filter out non-printable characters
                message += char
            else:
                break  # Stop decoding at the first non-printable character

    return message


# Example Usage
if __name__ == "__main__":
    original_image = "input.png"   # Change to your image file
    secret_message = "Hello, this is hidden!"
    output_image = "stego_image.png"

    # Encode the message
    encode_message(original_image, secret_message, output_image)
    print("Message hidden successfully!")

    # Decode the message
    extracted_message = decode_message(output_image)
    print("Extracted Message:", extracted_message)
