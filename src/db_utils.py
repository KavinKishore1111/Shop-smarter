import psycopg2
from config import DB_CONFIG


def get_connection():
    """
    Returns a psycopg2 connection to PostgreSQL
    """
    conn = psycopg2.connect(
        host=DB_CONFIG['host'],
        database=DB_CONFIG['database'],
        user=DB_CONFIG['user'],
        password=DB_CONFIG['password'],
        port=DB_CONFIG['port']
    )
    return conn

def upload_df(df, table_name):
    """
    Uploads a pandas dataframe to PostgreSQL using psycopg2
    """
    import io
    conn = get_connection()
    cursor = conn.cursor()

    # Use StringIO to copy data efficiently
    buffer = io.StringIO()
    df.to_csv(buffer, index=False, header=False)
    buffer.seek(0)

    # Get columns
    columns = ','.join(df.columns)

    try:
        cursor.copy_from(buffer, table_name, sep=",", columns=df.columns)
        conn.commit()
        print(f"Data uploaded to table '{table_name}' successfully using psycopg2!")
    except Exception as e:
        conn.rollback()
        print(f"Error uploading data: {e}")
    finally:
        cursor.close()
        conn.close()
