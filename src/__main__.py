"""CLI for dhyana."""
import sys, json, argparse
from .core import Dhyana

def main():
    parser = argparse.ArgumentParser(description="Dhyana — AI Meditation Guide. Personalized meditation sessions with biofeedback integration.")
    parser.add_argument("command", nargs="?", default="status", choices=["status", "run", "info"])
    parser.add_argument("--input", "-i", default="")
    args = parser.parse_args()
    instance = Dhyana()
    if args.command == "status":
        print(json.dumps(instance.get_stats(), indent=2))
    elif args.command == "run":
        print(json.dumps(instance.process(input=args.input or "test"), indent=2, default=str))
    elif args.command == "info":
        print(f"dhyana v0.1.0 — Dhyana — AI Meditation Guide. Personalized meditation sessions with biofeedback integration.")

if __name__ == "__main__":
    main()
