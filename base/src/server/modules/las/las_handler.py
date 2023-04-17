import lasio

import werkzeug.datastructures

class LAS_Handler:
    def __init__(self, file: werkzeug.datastructures.FileStorage) -> None:
        """Class responsible of handling LAS files.
        """
        print(f"Trying to upload file of type {type(file)}...")
        self.las_file = self.read_las_file(file)
    
    def read_las_file(self, file: werkzeug.datastructures.FileStorage) -> lasio.LASFile:
        """Read a LAS file.
        """
        try:
            return lasio.read(file.stream.read().decode())
        except Exception as e:
            print("Exception while trying to read LAS file.")
            print(f"Unhandled exception of type {type(e)}\n{e}")
        
        return None

    def test_las_file(self) -> None:
        """Test LAS file.
        """
        if not self.las_file:
            print("No LAS file to work with")
            return
        # Access the header information
        header = self.las_file.header

        print(header)
        print("Header read successfully")