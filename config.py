from pydantic import BaseModel, Field


class Config(BaseModel):
    """Configuration for the genetic algorithm.

    Args:
        BaseModel (Pydantic BaseModel): The base class for the configuration model.
    """
    crossover_rate: float = Field(ge=0.0, le=1.0)
    mutation_rate: float = Field(ge=0.0, le=1.0)
    population_size: int = Field(gt=0)
    iterations: int = Field(gt=0)
    max_depth: int = Field(gt=0)
    target_lookup: dict[float, float]
    seed: int | None = None