import csv

class WriteIntoCsv():
    def __init__(self) -> None:
        """
        This method initialize WriteIntoCsv object
        """
        self.csv_name = None

    def __check_csv_creat(self) -> None:
        """
        This method identifies if csv is already created
        """
        # Put a open csv into a try 
        try:
            file_csv = open(self.csv_name)
            file_csv.close()
        except FileNotFoundError as e:
            # If excepition raise create a csv file with the write name
            with open(self.csv_name, 'a+', newline="") as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(('Image name','Identification'))
    
    def writer(self, informations:tuple, folder_name:str) -> None:
        """
        This method write informations into csv about images

        Args:
            informations (tuple): informations about image name and classification
            folder_name (str): name of folder to put into csv name
        """
        self.csv_name = folder_name + '.csv'
        self.__check_csv_creat()

        with open(self.csv_name, 'a+', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(informations)
    

if __name__ == '__main__':
    writer = WriteIntoCsv()
    writer.writer(('download (1).jpg', 'Macaque'), 'cade')
    print('acabei')