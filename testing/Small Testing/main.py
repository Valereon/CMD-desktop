from PIL import Image
import sys
import os
import shutil

def display_image_in_terminal(image_path, max_width=None, max_height=None, scale_factor=1.0):
    """
    Display an image in the terminal using RGB Unicode blocks.
    Automatically scales to terminal size if max_width and max_height are not specified.
    """
    try:
        # Open the image
        img = Image.open(image_path)
        
        # Get terminal size
        terminal_size = shutil.get_terminal_size()
        
        # Calculate usable terminal dimensions with scaling factor
        usable_width = int((terminal_size.columns - 2) * scale_factor)
        usable_height = int((terminal_size.lines - 3) * scale_factor)  # Extra line for status
        
        # Use terminal dimensions if not specified, but with more conservative sizing
        if max_width is None:
            max_width = usable_width
        if max_height is None:
            max_height = usable_height
        
        # Calculate new dimensions while maintaining aspect ratio
        aspect_ratio = img.height / img.width
        width = min(max_width, usable_width)
        height = int(aspect_ratio * width / 2)  # Divide by 2 because terminal characters are taller than wide
        
        # Ensure height doesn't exceed max_height
        if height > max_height:
            height = max_height
            width = int(height * 2 / aspect_ratio)
        
        # Resize the image
        img = img.resize((width, height))
        
        # Convert to RGB if it's not already
        img = img.convert('RGB')
        
        # Get pixel data
        pixels = list(img.getdata())
        pixel_matrix = [pixels[i:i+width] for i in range(0, len(pixels), width)]
        
        # Clear the terminal first (for better display)
        os.system('clear' if os.name == 'posix' else 'cls')
        
        # Display the image using Unicode block character with ANSI color codes
        for row in pixel_matrix:
            line = ""
            for r, g, b in row:
                # Use ANSI escape codes to set the background color and print a space
                line += f"\033[48;2;{r};{g};{b}m  \033[0m"
            print(line)
        
        print(f"Terminal: {terminal_size.columns}x{terminal_size.lines} | Image: {width}x{height} | Scale: {scale_factor:.2f}")
        return True
        
    except Exception as e:
        print(f"Error: {e}")
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_image> [width] [height] [scale_factor]")
        print("Example: python main.py sample.jpg")
        print("Example with scale: python main.py sample.jpg 0 0 0.75")
        return
    
    image_path = sys.argv[1]
    
    # Get optional width and height parameters if provided
    max_width = None
    max_height = None
    scale_factor = 0.75  # Default to 75% of terminal size to avoid needing zoom
    
    if len(sys.argv) > 2:
        try:
            max_width = int(sys.argv[2])
            if max_width == 0:  # Allow 0 to mean "auto size"
                max_width = None
        except ValueError:
            print("Width parameter must be an integer")
            return
    
    if len(sys.argv) > 3:
        try:
            max_height = int(sys.argv[3])
            if max_height == 0:  # Allow 0 to mean "auto size"
                max_height = None
        except ValueError:
            print("Height parameter must be an integer")
            return

    if len(sys.argv) > 4:
        try:
            scale_factor = float(sys.argv[4])
            if scale_factor <= 0 or scale_factor > 1.0:
                print("Scale factor must be between 0.1 and 1.0")
                scale_factor = 0.75
        except ValueError:
            print("Scale factor must be a float between 0.1 and 1.0")
            return
    
    display_image_in_terminal(image_path, max_width, max_height, scale_factor)

if __name__ == "__main__":
    main()