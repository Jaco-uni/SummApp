import pandas as pd
import ast
import io
import os
from config import download_to_s3


AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

def pd_dati():
    content = download_to_s3()

    df = pd.read_csv(io.StringIO(content))

    # Crea il dizionario
    diz_email = {}

    for _, row in df.iterrows():
        email = row["Email"]
        name = row["Name"]
        surname = row["Surname"]
        keywords = ast.literal_eval(row["Keywords"])
        subject = ast.literal_eval(row["Subject"])
        classification = row["Classification"]

        diz_email[email] = [name, surname, keywords, subject, classification]
    return diz_email