import csv


class WriteIntoCsv:
    def __init__(self) -> None:
        """
        This method initialize WriteIntoCsv object
        """
        self.csv_name = None

    def __check_csv_create(self) -> None:
        """
        This method identifies if csv is already created
        """
        # Put a open csv into a try 
        try:
            file_csv = open(self.csv_name)
            file_csv.close()
        except FileNotFoundError as e:
            # If exception raise create a csv file with the write name
            with open(self.csv_name, 'a+', newline="") as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(('Image name', 'Identification'))
    
    def writer(self, information: tuple, folder_name: str) -> None:
        """
        This method write information into csv about images

        Args:
            information (tuple): information about image name and classification
            folder_name (str): name of folder to put into csv name
        """
        self.csv_name = folder_name + '.csv'
        self.__check_csv_create()

        with open(self.csv_name, 'a+', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(information)
    