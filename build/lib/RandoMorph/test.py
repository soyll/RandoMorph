import random
import pandas as pd
import dataframe_image as dfi
import requests

address = [i.strip() for i in requests.get('https://github.com/soyll/RandoMorph/blob/main/dicts/address.txt').json()['payload']['blob']['rawLines']]
date = [i.strip() for i in requests.get('https://github.com/soyll/RandoMorph/blob/main/dicts/date.txt').json()['payload']['blob']['rawLines']]
email = [i.strip() for i in requests.get('https://github.com/soyll/RandoMorph/blob/main/dicts/email.txt').json()['payload']['blob']['rawLines']]
user_id = [i.strip() for i in requests.get('https://github.com/soyll/RandoMorph/blob/main/dicts/id.txt').json()['payload']['blob']['rawLines']]
name = [i.strip() for i in requests.get('https://github.com/soyll/RandoMorph/blob/main/dicts/name.txt').json()['payload']['blob']['rawLines']]

class randoMorph:
    def __init__(self):
        self.user_id = None
        self.date = None
        self.email = None
        self.address = None
        self.name = None
        self.df = None
        self.length = None
        self.out_path = None
        self.file_name = None
        self.sample = None
        self.contains = {"Address": address, "Date": date, "Email": email, "User_id": user_id, "Name": name}
        self.test = {}
        self.data = {}

    def generate(self, sample, length, file_name, output_path):
        self.sample = sample.split(" ")
        self.length = length
        self.file_name = file_name
        self.out_path = output_path

        for i in self.sample:
            self.data.update({i: None})

        for i in self.sample:
            self.test.update({i: self.contains[i]})
        for i in range(0, length):
            self.address = [self.test["Address"][random.randint(0, 249)] for _ in
                            range(0, length)] if "Address" in self.data else None
            self.date = [self.test["Date"][random.randint(0, 249)] for _ in
                         range(0, length)] if "Date" in self.data else None
            self.email = [self.test["Email"][random.randint(0, 249)] for _ in
                          range(0, length)] if "Email" in self.data else None
            self.user_id = [self.test["User_id"][random.randint(0, 249)] for _ in
                            range(0, length)] if "User_id" in self.data else None
            self.name = [self.test["Name"][random.randint(0, 249)] for _ in
                         range(0, length)] if "Name" in self.data else None
        for _ in self.data:
            self.data.update({"Address": self.address}) if self.address is not None else None
            self.data.update({"Date": self.date}) if self.date is not None else None
            self.data.update({"Email": self.email}) if self.email is not None else None
            self.data.update({"User_id": self.user_id}) if self.user_id is not None else None
            self.data.update({"Name": self.name}) if self.name is not None else None

        self.df = pd.DataFrame(self.data)

        if "json" in self.file_name:
            self.df.to_json(self.out_path + self.file_name, indent=2)
            return self.file_name
        elif "csv" in self.file_name:
            self.df.to_csv(self.out_path + self.file_name)
            return self.file_name
        elif "xlsx" in self.file_name:
            self.df.to_excel(self.out_path + self.file_name)
            return self.file_name
        elif "png" in self.file_name:
            dfi.export(self.df, self.out_path + self.file_name)
            return self.file_name
        else:
            raise ValueError("Incorrect filetype")