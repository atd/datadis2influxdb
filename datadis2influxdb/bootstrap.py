from datetime import datetime, timedelta
from datadis_class import Datadis
from influxdb_class import InfluxDbClass

influxdb = InfluxDbClass()

def month_strings(start_month):
  start_date = datetime.strptime('2021/03', '%Y/%m')
  current_date = datetime.now()

  unique_month_set = {(start_date + timedelta(i)).strftime('%Y/%m') for i in range((current_date - start_date).days + 1)}

  return sorted(list(unique_month_set))

def store(data):
  influxdb.write(data)

def bootstrap():
  datadis = Datadis()

  year, month, day = datadis.contract_start_date.split('/')
  start_month = f"{year}/{month}"

  months = (month_strings(start_month))

  for month in months:
    try:
      datadis_data = datadis.data(month)
      influxdb_data = transform(datadis_data)
      store(influxdb_data)
      print(f"{month} stored")
    except Exception as error:
      print(f"error in month {month}: {error}")


if __name__ == "__main__":
    print(f"Fetching first data")

    bootstrap()
