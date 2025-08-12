# Pokémon style turn and text based battler

This project requires uv, install uv: curl -LsSf https://astral.sh/uv/install.sh | sh

## Interface

### Optional

- nano ~/.bash_aliases (on linux)
- add alias venv='source ./venv.sh'
- add alias main='./main.sh'
- add alias tester='./test.sh'

### Run the game
- uv venv
- uv sync
- venv (or source ./venv.sh)
- main (or ./main.sh) to start the game

## Roadmap
- color and shiny logic
- status moves
- natures
- maybe abilities

## Implemented
- accurate move sets for all pokemon (just damaging moves for now)
- parties of six for both you and the opponent
- super/not very effective
- STAB
- crits
- physical/special split

## Issues
- Pokemon that don't have at least four moves with power >0 are not being added correctly