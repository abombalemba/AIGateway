import pydantic as pd

import datetime as dt
import typing as tp


class BaseResponse(pd.BaseModel):
	success: bool
	message: str
	timestamp: dt.datetime


class TextGenerationResponse(BaseResponse):
	generated_text: str
	tokens_used: int
	processing_time: float

