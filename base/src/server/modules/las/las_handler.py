import sys
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
        self.properties = self.las_file.keys()
    
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
        
        # print(self.choose_properties())
        self.run_crossplot()
    
    def run_crossplot(self):
        """Run the main crossplot process
        """
        x, y = self.choose_properties()
        self.show_crossplot(x, y)

    def choose_properties(self) -> tuple[str,str]:
        """Let user choose properties
        """
        # Showing menu
        self.show_properties()
        print("Choose your properties")
        print("------------------------\n")
        # TODO: Unhandled exceptions
        op1 = input('Property 1: ')
        op2 = input('Property 2: ')

        return op1, op2

    def show_properties(self) -> None:
        """Show properties available in a LAS file.
        """
        props = "Properties available:\n"

        for prop in self.properties:
            props += f"{prop} - {self.las_file[prop]}\n"

        print(props)

    def show_crossplot(self, x_property: str, y_property: str) -> None:
        """Show crossplot of two properties from LAS file.
        """
        x = self.las_file[x_property]
        y = self.las_file[y_property]

        plt.scatter(x, y)

        plt.xlabel(x_property)
        plt.ylabel(y_property)

        plt.show()

        print("Finishing program due to warning issues")
        sys.exit(0)
