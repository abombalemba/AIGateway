import pydantic as pd

import typing
import enum


class ModelType(str, enum.Enum):
	TEXT_GENERATION = 'text_generation'


class TextGenerationRequest(pd.BaseModel):
	prompt: str = pd.Field(..., min_length=1, max_length=4096)
	model: str = pd.Field(defualt='deepseek/deepseek-chat-v3.1:free')
	url: str = pd.Field(default='https://openrouter.ai/api/v1')
	token: str = pd.Field(...)

