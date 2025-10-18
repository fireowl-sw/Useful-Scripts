import os

def show_filenames_without_extensions(directory_path, excluded_extensions=None):
    """
    Display filenames without their extensions in the terminal.
    This does NOT rename any files - it only displays them.
    
    Args:
        directory_path (str): Path to the directory containing files
        excluded_extensions (list): List of extensions to exclude from display
    """
    if excluded_extensions is None:
        excluded_extensions = []
    
    print(f"Files in {directory_path} (without extensions):")
    
    for root, dirs, files in os.walk(directory_path):
        # Calculate indentation based on directory depth
        level = root.replace(directory_path, '').count(os.sep)
        indent = '  ' * level
        
        # Print directory name
        if level > 0 or root != directory_path:
            print(f"{indent}{os.path.basename(root)}/")
        
        # Print files without extensions (sorted alphabetically)
        subindent = '  ' * (level + 1)
        sorted_files = sorted(files)
        for file in sorted_files:
            filename, ext = os.path.splitext(file)
            # Skip files with excluded extensions
            if ext.lower() not in excluded_extensions:
                print(f"{subindent}{filename}")

# Example usage:
if __name__ == "__main__":
    # Example 1: Show all files in a directory without extensions
    directory = "/Users/fireowl/Downloads/PolyuStudy/S1_04_EE546_ElectricEnergyStorageandNewEnergySourcesforElectricVehicles_Semester1"
    show_filenames_without_extensions(directory)
