import lasio
import matplotlib.pyplot as plt

import werkzeug.datastructures

class LAS_Handler:
    def __init__(self, file: werkzeug.datastructures.FileStorage, verbose=False) -> None:
        """Class responsible of handling LAS files.
        """
        if verbose: print(f"Trying to upload file of type {type(file)}...")
        self.filename = file.filename
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
        
        def get_header_info(): return self.las_file.header
        def get_las_props(): return self.las_file.keys()
        
        # print(get_las_props())
        self.show_crossplot('DT', 'RHOB')
        print(f"Test of {self.filename} done successfully")
    
    def show_crossplot(self, x_property: str, y_property: str) -> None:
        """Show crossplot of two properties from LAS file.
        """
        x = self.las_file[x_property]
        y = self.las_file[y_property]

        plt.scatter(x, y)

        plt.xlabel(x_property)
        plt.ylabel(y_property)

        plt.show()
