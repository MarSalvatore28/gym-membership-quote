"""Command-line interface for the Gym Membership Quote (R8)."""
from gym_quote import INVALID, GymQuote


def parse_extras(text):
    """Turn 'spa, group_classes' into ['SPA', 'GROUP_CLASSES']."""
    return [item.strip().upper() for item in text.split(",") if item.strip()]


def run(read=input, write=print):
    """Ask for the selection, show each step and return the total, or -1."""
    plan = read("Plan (BASIC, STANDARD, PREMIUM): ").strip().upper()
    extras = parse_extras(read("Extras separated by commas (empty for none): "))
    try:
        members = int(read("Number of members: "))
    except ValueError:
        write("Invalid selection")
        return INVALID
    steps = GymQuote(plan, extras, members).breakdown()
    if steps is None:
        write("Invalid selection")
        return INVALID
    write(f"Subtotal:           {steps['subtotal']:.2f}")
    write(f"Group discount:    -{steps['group_discount']:.2f}")
    write(f"Special offer:     -{steps['special_offer']:.2f}")
    write(f"Premium surcharge: +{steps['premium_surcharge']:.2f}")
    write(f"Total:              {steps['total']}")
    if read("Confirm (y/n): ").strip().lower() != "y":
        write("Cancelled")
        return INVALID
    return steps["total"]


if __name__ == "__main__":
    print(f"Result: {run()}")
