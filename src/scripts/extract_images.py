import os
import re
import base64
import sys
import glob

def extract_base64_images(markdown_file):
    # Create images directory if it doesn't exist
    images_dir = os.path.join(os.path.dirname(markdown_file), "images")
    os.makedirs(images_dir, exist_ok=True)
    
    # Read the markdown file
    with open(markdown_file, 'r') as f:
        content = f.read()
    
    # Looking for patterns like [image1]: <data:image/png;base64,...> or [image1]: <data:image/jpeg;base64,...>
    image_pattern = r'\[image(\d+)\]:\s*<data:image/([a-z]+);base64,([A-Za-z0-9+/=]+)>'
    
    # Find all matches
    replacements = {}
    image_count = 0
    for match in re.finditer(image_pattern, content):
        image_count += 1
        image_number = match.group(1)
        image_type = match.group(2)
        base64_data = match.group(3)
        
        print(f"Found image {image_count}: image{image_number} of type {image_type}")
        
        # Convert jpeg to jpg for the filename extension
        if image_type == "jpeg":
            file_extension = "jpg"
        else:
            file_extension = image_type
        
        # Generate a filename based on the image number
        filename = f"figure{image_number}.{file_extension}"
        filepath = os.path.join(images_dir, filename)
        
        # Save the image
        try:
            image_data = base64.b64decode(base64_data)
            with open(filepath, 'wb') as img_file:
                img_file.write(image_data)
            print(f"Saved image to {filepath}")
            
            # Store the replacement
            full_match = match.group(0)
            relative_path = f"images/{filename}"
            replacements[full_match] = f"[image{image_number}]: {relative_path}"
            
        except Exception as e:
            print(f"Error processing image {image_number}: {e}")
    
    if image_count == 0:
        print("No images found in the markdown file.")
    else:
        print(f"Found {image_count} images in total.")
    
    # Replace all occurrences in the content
    new_content = content
    for old, new in replacements.items():
        new_content = new_content.replace(old, new)
    
    # Write the updated content back to the file
    with open(markdown_file, 'w') as f:
        f.write(new_content)
    
    print(f"Updated {markdown_file} with {len(replacements)} image references")

if __name__ == "__main__":
    # Check if a filename was provided as command-line argument
    if len(sys.argv) > 1:
        markdown_file = sys.argv[1]
    else:
        # Get the current directory
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Find all markdown files in the directory and sort them
        markdown_files = sorted(glob.glob(os.path.join(current_dir, "*.md")))
        
        if markdown_files:
            # Use the first markdown file (alphabetically)
            markdown_file = os.path.basename(markdown_files[0])
            print(f"No filename provided, using first markdown file: {markdown_file}")
        else:
            print("No markdown files found in the directory.")
            print(f"Usage: python {os.path.basename(__file__)} [markdown_filename]")
            sys.exit(1)
    
    # Get the absolute path
    current_dir = os.path.dirname(os.path.abspath(__file__))
    markdown_path = os.path.join(current_dir, markdown_file)
    
    # Check if the file exists
    if not os.path.exists(markdown_path):
        print(f"Error: File '{markdown_file}' not found")
        print(f"Usage: python {os.path.basename(__file__)} [markdown_filename]")
        sys.exit(1)
    
    # Process the file
    extract_base64_images(markdown_path)
    print("Done!")
