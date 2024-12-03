import os 
import pandas as pd


def populate_csv():

    main_folder = r'C:\Users\tarus\COVID-19\data\ModelResults2'
    results = []

    for country in os.listdir(main_folder):
        country_path = os.path.join(main_folder,country)
        for file in os.listdir(country_path):
            print("For Country:",country,"\n")
            if file.endswith('.txt'):
                file_path = os.path.join(country_path,file)
                header = file_path.split('_Results')[0]
                
                with open(file_path,'r'):
                    data = file.splitlines()
                    print(data)
                    try:
                        mse = data[-2].split(': ')[-1]
                        r2_score = data[-1].split(': ')[-1]

                        result = {'Country':country,'Model':header,'MSE':mse,'R2':r2_score}
                        results.append(result)
                    except Exception as e:
                        print(e)

    print(results)


if __name__ == "__main__":
    populate_csv()
                    
                


                    
                    

