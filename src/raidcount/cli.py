"""raidcount command line."""
import argparse

from .match import Match


def main() -> None:
    p = argparse.ArgumentParser(prog="raidcount")
    sub = p.add_subparsers(dest="cmd", required=True)
    new = sub.add_parser("new", help="start a match")
    new.add_argument("team_a")
    new.add_argument("team_b")
    raid = sub.add_parser("raid", help="score one raid")
    raid.add_argument("--team", choices=["A", "B"], required=True)
    raid.add_argument("--touch", type=int, default=0, help="defenders touched")
    raid.add_argument("--bonus", action="store_true", help="raider crossed the bonus line")
    raid.add_argument("--tackled", action="store_true", help="raider was tackled")
    sub.add_parser("undo", help="take back the last raid")
    sub.add_parser("score", help="show the score")
    args = p.parse_args()

    if args.cmd == "new":
        Match(args.team_a, args.team_b).save()
        return
    m = Match.load()
    if args.cmd == "raid":
        m.raid(args.team, args.touch, args.bonus, args.tackled)
        m.save()
    elif args.cmd == "undo":
        if not m.undo():
            print("nothing to undo")
        m.save()
    print(f"{m.team_a} {m.points['A']} : {m.points['B']} {m.team_b}")


if __name__ == "__main__":
    main()
