import pandas as pd
from datetime import datetime
from tabulate import tabulate

def updateDateFormat(timestamp):
    # assuming at timestamp is PST timestamp
    dt = datetime.fromtimestamp(timestamp/1000)
    return dt.strftime("%Y-%m-%d %H:%M:%S PST")

def parse_update_CSV(file_path):
    df = pd.read_csv(file_path)
    df.fillna("", inplace=True)
    df['formattedDate'] = df['timeStamp'].apply(lambda x: updateDateFormat(x))
    df = df[df['responseCode'] != 200]
    df = df[['label', 'responseCode', 'responseMessage', 'failureMessage', 'formattedDate']]
    print(tabulate(df, headers='keys', tablefmt='fancy_grid'))
    print("****" * 10)


if __name__ == "__main__":
    file_paths = ['./Data/Jmeter_log1.jtl', './Data/Jmeter_log2.jtl']
    for file_path in file_paths:
        parse_update_CSV(file_path)