import airflow
from datetime import timedelta
from airflow import DAG
from airflow.operators.postgres_operator import PostgresOperator
from airflow.utils.dates import days_ago

args={'owner': 'airflow'}

default_args = {
    'owner': 'airflow',    
    #'start_date': airflow.utils.dates.days_ago(2),
    # 'end_date': datetime(),
    # 'depends_on_past': False,
    #'email': ['airflow@example.com'],
    #'email_on_failure': False,
    # 'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag_psql = DAG(
    dag_id = "run_insert",
    default_args=args,
    schedule_interval='0 7 * * *',
    schedule_interval='@once',	
    dagrun_timeout=timedelta(minutes=60),
    start_date = airflow.utils.dates.days_ago(1)
)

insert_data_sql_query = """
    insert into fact_order_accumulating 
    select 
    ddorder.id as order_date_id,
    ddinv.id as invoice_date_id,
    ddpayment.id as payment_date_id,
    o.order_number,
    i.invoice_number ,
    c.id as customer_id,
    sum(ol.quantity ) as total_order_quantity,
    sum(ol.usd_amount) as total_order_usd_amount,
    EXTRACT(DAY FROM i."date"::timestamp-o."date"::timestamp) AS order_to_invoice_lag_days,
    EXTRACT(DAY FROM p."date"::timestamp-i."date"::timestamp) AS invoice_to_payment_lag_days
    from orders o
    left join order_lines ol on (o.order_number = ol.order_number)
    left join invoices i on (o.order_number = i.order_number)
    left join payments p on (i.invoice_number = p.invoice_number)
    left join customers c on (o.customer_id = c.id)
    left join dim_date as ddorder on (o."date" = ddorder."date")
    left join dim_date as ddinv on (i."date" = ddinv."date")
    left join dim_date as ddpayment on (p."date" = ddpayment."date")
    group by 1,2,3,4,5,6,10;
    """

insert_data = PostgresOperator(
    sql = insert_data_sql_query,
    task_id = "insert_data_task",
    postgres_conn_id = "postgres_local",
    dag = dag_psql
    )

insert_data 

if __name__ == "__main__":
    dag_psql.cli()