from sqlalchemy import create_engine

def init(data, username='root', password='tttn0711', host='localhost:3306/data'):
    engine = create_engine(
        f"mysql+mysqlconnector://{username}:{password}@{host}"
    )

    data.to_sql(
        'SPACEXTBL', # Table name
        con = engine,
        if_exists = 'replace',
        index = False,
        method = 'multi'
    )