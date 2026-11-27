import json
from pathlib import Path

from genetic_algorithm import GeneticAlgorithm
from config import Config

def load_config(file_path: str | Path) -> Config:
    with open(file_path, "r", encoding="utf-8") as file:
        config_data = json.load(file)

    return Config(**config_data)


def main():
    config: Config = load_config("config.json")

    ga = GeneticAlgorithm(
        config.crossover_rate,
        config.mutation_rate,
        config.number_of_offspring,
        config.population_size,
        config.crossover_signal,
        config.chromosome_length,
        mutation_step=config.mutation_step,
        seed=config.seed,
        optimum_fitness=config.optimum_fitness,
        target_error=config.target_error,
        lower_bound=config.lower_bound,
        upper_bound=config.upper_bound,
        evaluation_budget=config.evaluation_budget,
        adaptive_mutation=config.adaptive_mutation,
    )

    print(ga.run_evolution(save_report=True))

if __name__ == "__main__":
    main()
