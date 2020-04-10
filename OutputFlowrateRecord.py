from Database import Database
import os
class OutputFlowrateRecord():
    def __init__(self):
        super().__init__()

    def output(self):
        db = Database()
        items = db.getAllTimeFlowrate()
        with open('FlowrateRecord.txt','w') as file_object:
            file_object.write('ID\t\tNumber\t\tTime\n')
            for item in items:
                file_object.write(str(100000 + item[0]) + "\t\t" +str(item[1]) + "\t\t" + item[2] + '\n')
        print("Output the record successfully!")