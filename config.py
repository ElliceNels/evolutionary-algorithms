from pydantic import BaseModel, Field, model_validator


class Config(BaseModel):
    """Configuration for the genetic algorithm.

    Args:
        BaseModel (Pydantic BaseModel): The base class for the configuration model.
    """
    crossover_rate: float = Field(ge=0.0, le=1.0)
    mutation_rate: float = Field(ge=0.0, le=1.0)
    mutation_step: float = Field(ge=0.0, allow_inf_nan=False)
    population_size: int = Field(gt=0)
    number_of_offspring: int = Field(gt=0)
    chromosome_length: int = Field(gt=0)
    crossover_signal: int = Field(gt=0)
    iterations: int = Field(gt=0)

    @model_validator(mode="after")
    def validate_ga_settings(self) -> "Config":
        if self.number_of_offspring > self.population_size:
            raise ValueError("number_of_offspring must not exceed population_size")
        if self.crossover_signal >= self.chromosome_length:
            raise ValueError("crossover_signal must be less than chromosome_length")
        return self
