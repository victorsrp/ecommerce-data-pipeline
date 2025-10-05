# generate_csv.py
from faker import Faker
import pandas as pd
import uuid
from datetime import datetime
from pathlib import Path

fake = Faker('pt_BR')
raw_path = Path("data/raw") #criando objeto path

#garantindo pasta data/raw
raw_path.mkdir(parents=True, exist_ok=True)


def gen_rows(n=1000):
    rows = []
    for _ in range(n):
        rows.append({
            "user_id": str(uuid.uuid4()),
            "nome": fake.name(),
            "idade": fake.random_int(min=18, max=75),
            "cidade": fake.city(),
            "produto": fake.word(),
            "valor_compra": round(fake.pyfloat(left_digits=3, right_digits=2, positive=True),2),
            "data_compra": fake.date_time_between(start_date='-60d', end_date='now').isoformat()
        })
    return pd.DataFrame(rows)

if __name__ == "__main__":
    df = gen_rows(5000)  # gera 5000 linhas
    filename = f"sales_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    file_path = raw_path / filename #diretorio data/raw/filename.csv
    df.to_csv(file_path, index=False)
    print("CSV gerado:", file_path)
