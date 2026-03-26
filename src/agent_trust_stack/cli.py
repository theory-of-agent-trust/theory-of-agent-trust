"""
Unified CLI for the Agent Trust Stack.

Commands:
    trust-stack init     — Initialize all protocol stores
    trust-stack status   — Show status of all protocols
    trust-stack verify   — Run full trust verification on an agent
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def cmd_init(args: argparse.Namespace) -> int:
    """Initialize all protocol stores for an agent."""
    from agent_trust_stack.trust_stack import TrustStack

    stack = TrustStack(
        agent_id=args.agent_id,
        storage_root=args.storage,
    )

    # Add genesis entry to CoC chain
    stack.coc.add("boot", f"Trust stack initialized for {args.agent_id}")

    print(f"Initialized Agent Trust Stack for: {args.agent_id}")
    print(f"Storage root: {stack.storage_root}")
    print()
    print(stack.status_summary())
    return 0


def cmd_status(args: argparse.Namespace) -> int:
    """Show status of all protocols."""
    from agent_trust_stack.trust_stack import TrustStack

    storage = args.storage
    if not Path(storage).exists():
        print(f"Error: Storage root '{storage}' does not exist.", file=sys.stderr)
        print("Run 'trust-stack init' first.", file=sys.stderr)
        return 1

    stack = TrustStack(
        agent_id=args.agent_id,
        storage_root=storage,
    )

    if args.json:
        statuses = stack.status()
        output = {k: v.to_dict() for k, v in statuses.items()}
        output["agent_id"] = stack.agent_id
        output["storage_root"] = str(stack.storage_root)
        print(json.dumps(output, indent=2))
    else:
        print(stack.status_summary())

    return 0


def cmd_verify(args: argparse.Namespace) -> int:
    """Run full trust verification on an agent."""
    from agent_trust_stack.trust_stack import TrustStack

    storage = args.storage
    if not Path(storage).exists():
        print(f"Error: Storage root '{storage}' does not exist.", file=sys.stderr)
        print("Run 'trust-stack init' first.", file=sys.stderr)
        return 1

    stack = TrustStack(
        agent_id=args.agent_id,
        storage_root=storage,
    )

    report = stack.bus.run_full_trust_verification(args.target or args.agent_id)

    if args.json:
        print(json.dumps(report, indent=2, default=str))
    else:
        print(f"Trust Verification Report")
        print(f"{'=' * 50}")
        print(f"Agent: {report['agent_id']}")
        print(f"Timestamp: {report['timestamp']}")
        print()
        for proto_name, proto_data in report["protocols"].items():
            print(f"  [{proto_name.upper()}]")
            for k, v in proto_data.items():
                print(f"    {k}: {v}")
        print()
        print(f"  COMPOSITE TRUST SCORE: {report['composite_trust_score']}/100")

    return 0


def main(argv: list[str] | None = None) -> int:
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        prog="trust-stack",
        description="Agent Trust Stack — unified CLI for all seven trust protocols",
    )
    parser.add_argument(
        "--version", action="version",
        version="%(prog)s 0.1.0",
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # --- init ---
    init_parser = subparsers.add_parser("init", help="Initialize all protocol stores")
    init_parser.add_argument(
        "agent_id", help="Agent identifier (DID, URI, or plain string)",
    )
    init_parser.add_argument(
        "--storage", default=".trust-stack",
        help="Storage root directory (default: .trust-stack)",
    )

    # --- status ---
    status_parser = subparsers.add_parser("status", help="Show protocol status")
    status_parser.add_argument(
        "agent_id", help="Agent identifier",
    )
    status_parser.add_argument(
        "--storage", default=".trust-stack",
        help="Storage root directory (default: .trust-stack)",
    )
    status_parser.add_argument(
        "--json", action="store_true",
        help="Output as JSON",
    )

    # --- verify ---
    verify_parser = subparsers.add_parser("verify", help="Run full trust verification")
    verify_parser.add_argument(
        "agent_id", help="Agent identifier (owner of the stack)",
    )
    verify_parser.add_argument(
        "--target", default=None,
        help="Target agent to verify (defaults to agent_id)",
    )
    verify_parser.add_argument(
        "--storage", default=".trust-stack",
        help="Storage root directory (default: .trust-stack)",
    )
    verify_parser.add_argument(
        "--json", action="store_true",
        help="Output as JSON",
    )

    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        return 0

    commands = {
        "init": cmd_init,
        "status": cmd_status,
        "verify": cmd_verify,
    }

    return commands[args.command](args)


if __name__ == "__main__":
    sys.exit(main())
