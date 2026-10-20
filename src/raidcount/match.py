"""Match state: two teams, their points, and the raid log."""
import json
from dataclasses import dataclass, field, asdict
from pathlib import Path

STATE = Path(".raidcount.json")


@dataclass
class Match:
    team_a: str
    team_b: str
    points: dict = field(default_factory=lambda: {"A": 0, "B": 0})
    raids: list = field(default_factory=list)

    def raid(self, team: str, touch: int = 0, bonus: bool = False, tackled: bool = False) -> int:
        """Score one raid. A touch point per defender touched, one bonus point,
        and one point to the defending side when the raider is tackled."""
        gained = touch + (1 if bonus else 0)
        self.points[team] += gained
        if tackled:
            self.points["B" if team == "A" else "A"] += 1
        self.raids.append({"team": team, "touch": touch, "bonus": bonus, "tackled": tackled})
        return gained

    def undo(self) -> bool:
        """Take back the last raid: remove its points from both sides.
        Returns False when no raid has been scored yet."""
        if not self.raids:
            return False
        r = self.raids.pop()
        self.points[r["team"]] -= r["touch"] + (1 if r["bonus"] else 0)
        if r["tackled"]:
            self.points["B" if r["team"] == "A" else "A"] -= 1
        return True

    def save(self) -> None:
        STATE.write_text(json.dumps(asdict(self), indent=2))

    @classmethod
    def load(cls) -> "Match":
        return cls(**json.loads(STATE.read_text()))
