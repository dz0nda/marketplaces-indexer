# generated by datamodel-codegen:
#   filename:  cancel_sale.json

from __future__ import annotations

from pydantic import BaseModel
from pydantic import Extra


class CancelFloorBidParameter(BaseModel):
    class Config:
        extra = Extra.forbid

    cfb_asset_contract: str
    cfb_bid_type: str
    cfb_bid_asset: str
