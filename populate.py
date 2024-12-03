import os 
import pandas as pd


def populate_csv():

    main_folder = r'C:\Users\tarus\COVID-19\data\ModelResults2'
    results = []

    for country in os.listdir(main_folder):
        country_path = os.path.join(main_folder,country)
        print("We are in Country:",country,"\n")
        for file in os.listdir(country_path):
            if file.endswith('.txt'):
                file_path = os.path.join(country_path,file)
                header = file.split('_Results')[0]
                
                with open(file_path,'r') as file:
                    data = file.readlines()
                    #print(data)
                    try:
                        mse = data[-3].split(': ')[-1]
                        r2_score = data[-2].split(': ')[-1]

                        result = {'Country':country,'Model':header,'MSE':mse,'R2':r2_score}
                        results.append(result)
                    except Exception as e:
                        print(e)

    print(results)

    results_df = pd.DataFrame(results)
    csv_file = "COVID_model_results.csv"
    directory = os.path.join(main_folder,csv_file)

    if not os.path.exists(directory):
        os.makedirs(directory)

    results_df.to_csv(directory, index=False)


if __name__ == "__main__":
    populate_csv()
                    
                


                    
                    

