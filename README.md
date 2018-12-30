# Collab

Collab is an implementation of Axelrod's Iterated Prisoner's Dilemma tournament for my own personal use. For official repo, check out [Axelrod-Python/Axelrod](https://github.com/Axelrod-Python/Axelrod)

## Iterated Prisoner's Dilemma

The Prisoner's Dilemma can be summed up as follows.

Two players, P1 & P2, have a chance to collaborate or defect without knowing what the other player will do. Based upon the action taken by both players, scores will be allotted.

The grid shows how the scoring system will work.

|                     | P2 Collaborates  | P2 Defects       |
| ------------------- | ---------------- | ---------------- |
| **P1 Collaborates** | P1 = +3, P2 = +3 | P1 = +0, P2 = +5 |
| **P1 Defects**      | P1 = +5, P2 = +0 | P1 = +1, P2 = +1 |

Iterated Prisoner's Dilemma lasts more than a single round and each player has access to history of interaction with the other player.

Axelrod's Iterated Prisoner's Dilemma had the players play in a round robin format with all other players and a twin/clone of itself.

## System Layout

The system can broadly be split into two entities - Arbiter & Participant

**Arbiter** is the central authority who is responsible for:

- Maintaining history of moves
- Taking input from all participants and updating the status of current round
- Keeping track of scores for all participants
- Keeping track of rounds
- Triggering each participant to return moves for each round

**Player** is the entity who participates in the tournament as follows:

- Accept information from Arbiter such as
  - Round #
  - List of players
  - History of how the other players played against the player in previous round
- Based on the information from Arbiter, return the moves made against each player.

