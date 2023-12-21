import os
import asyncio
from functools import cached_property
from datadis import get_token, get_supplies, get_contract_detail, get_consumption_data

class Datadis:
  @cached_property
  def token(self):
    return asyncio.run(get_token(os.environ["DATADIS_USER"], os.environ["DATADIS_PASSWORD"]))

  @cached_property
  def supplies(self):
    return asyncio.run(get_supplies(self.token))

  @cached_property
  def supply(self):
    return self.supplies[0]

  @cached_property
  def cups(self):
    return self.supply["cups"]

  @cached_property
  def point_type(self):
    return self.supply["pointType"]

  @cached_property
  def distributor_code(self):
    return self.supply["distributorCode"]

  @cached_property
  def contract_details(self):
    return asyncio.run(get_contract_detail(self.token, self.cups, self.distributor_code))

  @cached_property
  def contract_detail(self):
    for detail in self.contract_details:
      if detail["cups"] == self.cups:
        return detail

    raise "Cannot find contract detail"

  @cached_property
  def contract_start_date(self):
    return self.contract_detail["startDate"]

  def data(self, month):
    return asyncio.run(
      get_consumption_data(
        self.token, self.cups, self.distributor_code, month, month, '0', self.point_type
      )
    )









