import pandas as pd
from emoji import emojize
from pandas.core.frame import DataFrame

DATASET_PATH = r"C:\Users\behar\Desktop\Github\Python\Weather Analysis\weather_data.csv"


def log(msg=None):
    print("______________________________________")
    print(emojize(f'{msg}'))
    print("______________________________________")


def readCsv(path: str) -> DataFrame:
    try:
        csvDataset = pd.read_csv(path)
        log('Reading CSV :grinning_face_with_big_eyes:')
        return csvDataset
    except Exception as e:
        log(f'Error in Reading CSV :rolling_on_the_floor_laughing:{e}')
        return pd.DataFrame()


if __name__ == '__main__':
    weatherData = readCsv(DATASET_PATH)
    log(
        f"🏉 Type of weatherData:{type(weatherData)}")
    # Reading Top N Rows of the dataset csv
    log(weatherData.head(10))
    # To See No of Rows and Columns in dataset
    log(f'😎 Dataframe Shape:\n{weatherData.shape}')
    # To see the indexs i.e total records start and end position
    log(f'😎 Dataframe index:\n{weatherData.index}')
    # To see the Columns Names
    log(
        f'🤭  Column names:\n{weatherData.columns}')
    # Data type of each columns ⏰
    log(
        f'🐍 Type of Each Columns:\n{weatherData.dtypes}')

    # 🤧 Get the Unique Values from the single column..😥 Cannot be applied to entire dataframe
    log(
        f'🌹  Unique Values of a Column:\n{weatherData["Weather"].unique()}')

    # 🏂 To get the no of unique values in all the columns,
    log(
        f"❄ No of unique values in each columns of entire dataset:\n {weatherData.nunique()}")

    # 🍝  Get the Valid Not Null values in the data frame
    log(
        f" 🍝  Get the Valid Not Null values in the data frame:\n{weatherData.count()}")

    # 🐜   Get the No of types each value is repeated in a single column 😠 Cannot apply for multiple columns
    log(
        f" 🐜 Get the No of types each value is repeated in a single column:\n{weatherData['Weather'].value_counts()}")

    # 🌍 Basic Information About the DataFrame
    log(f"🌍{weatherData.info()}")

    # ------------------------------------------Questionary-------------------------------------

    # 🚬 Get the Records when weather is clear
    log(
        f"🚬 Get the Records where weather is clear: \n {weatherData[weatherData.Weather == 'Clear']}")

    # 🚬 Get the No of Records when weather is clear
    log(
        f"🚬 Get the No of Records where weather is clear:\n {weatherData['Weather'].value_counts()}")

    # 🔈 Group By for individual columns
    log(
        f"🚬 🔈 Group By for individual columns:\n {weatherData.groupby('Weather').get_group('Clear')}")

    # 🔊 To Check out any null values column wise
    log(
        f"🚬 🔊 To Check out any null values column wise:\n {weatherData.isnull().sum()}")
