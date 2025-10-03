import pydantic as pd

import enum


class ModelType(str, enum.Enum):
	TEXT_GENERATION = 'text_generation'


class TextGenerationRequest(pd.BaseModel):
	prompt: str

