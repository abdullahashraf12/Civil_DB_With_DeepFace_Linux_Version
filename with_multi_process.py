from deepface import DeepFace
import time
from PySide6.QtCore import QThread
from numba import jit,cuda
import mysql.connector as mysqlcon
from multiprocessing import Process
import multiprocessing 
class multi_thread_class:
    def __init__(self,values={}) :
        self._values=values
    def set_values(self,values):
        self._values=values
    def get_values(self):
        return self._values
    def multi_thread(self,image1,image2):
        start_time=time.time()

        models = [
        "VGG-Face", # 0
        "Facenet",  # 1
        "Facenet512", # 2
        "OpenFace", # 3
        "DeepFace", # 4
        "DeepID", # 5
        "ArcFace", # 6
        "Dlib", # 7
        #   "SFace", # 8
        ]
        backends = [
        'opencv', # 0
        'ssd', # 1
        'dlib', # 2
        'mtcnn', # 3
        'retinaface', # 4 
        'mediapipe'# 5
        ]
        
        result = DeepFace.verify(img1_path = image1, 
            img2_path = image2, 
            model_name = models[7],
            detector_backend=backends[2]
            )
        self.set_values(result)        
        # if(result["verified"]==False):
            # b.set_x(b.get_x()+(time.time() - start_time))

def main():
    connection = mysqlcon.connect(
    user='abdo', 
    password='01123119835',
    host='127.0.0.1',
    database='civil_db')
    cursor = connection.cursor(buffered=True)



    sql_fetch_blob_query = "SELECT * FROM civilization_table"

    cursor.execute(sql_fetch_blob_query)
    connection.commit()
    record = cursor.fetchall()
    cursor.close()
    connection.close()
    
    
    first_name=""
    second_name=""
    full_name=""
    day_birth=""
    month_birth=""
    year_birth=""
    gender_type=""
    address=""
    ssn=""
    uic=""
    social_state_text=""
    person_image_data=[]
    type_of_image=""
    process=[]
    b=a()
    start=time.time()
    for i in record:
    #     person_image_data.append(i[10])
    # for row in person_image_data:
    
        # multi_thread(i[10],b)
        # print(i)
        proc=Process(target=multi_thread_class.multi_thread,args=(str(i[10]),"C:/Users/alpha/OneDrive/Desktop/Database Project/Data_Base_Project/image_to_find/Screenshot 2023-01-12 190303.jpg",))
        print(b.get_x())

        proc.start()
    print("Execution Time {}".format(time.time()-start))
        # process.append(proc)
    # for i in process:
    #     print(i)
    # n_cores = multiprocessing.cpu_count()
    # print("Number of cores :{}".format(n_cores))
    

        
        
        
if __name__ == '__main__':
    main()