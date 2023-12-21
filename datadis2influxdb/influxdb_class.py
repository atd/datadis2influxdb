import os
from functools import cached_property
from influxdb_client import InfluxDBClient

class InfluxDbClass:
  @cached_property
  def client(self):
    return InfluxDBClient(
      url=os.environ["INFLUXDB_URL"],
      token=os.environ["INFLUXDB_TOKEN"],
      org=os.environ["INFLUXDB_ORG"])

  @cached_property
  def write_api(self):
    return self.client.write_api()

  def write(self, data):
    return self.write_api.write(
      os.environ["INFLUXDB_BUCKET"],
      os.environ["INFLUXDB_ORG"],
      data
    )
