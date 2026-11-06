from pydantic import BaseModel, Field


class Config(BaseModel):
    crossover_rate: float = Field(ge=0.0, le=1.0)
    mutation_rate: float = Field(ge=0.0, le=1.0)
    population_size: int = Field(gt=0)
    number_of_offspring: int = Field(gt=0, le=population_size)
    chromosome_length: int = Field(gt=0)
    crossover_signal: int = Field(gt=0, lt=chromosome_length)
    iterations: int = Field(gt=0)
