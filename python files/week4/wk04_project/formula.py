"""Formula parsing and molar-mass helpers for the chemistry project."""


class FormulaError(ValueError):
	"""Raised when a chemical formula string is invalid."""


def parse_formula(formula, periodic_table_dict):
	"""Parse a chemical formula into (symbol, quantity) tuples.

	Supports formulas with optional nested parentheses such as:
	H2O, C6H12O6, Ca(OH)2, Al2(SO4)3
	"""

	stack = [dict()]
	i = 0

	while i < len(formula):
		ch = formula[i]

		if ch == "(":
			stack.append(dict())
			i += 1
			continue

		if ch == ")":
			if len(stack) == 1:
				raise FormulaError(f"Unmatched ')' in formula '{formula}'")
			i += 1
			multiplier, i = _parse_number(formula, i)
			group = stack.pop()
			for symbol, qty in group.items():
				stack[-1][symbol] = stack[-1].get(symbol, 0) + qty * multiplier
			continue

		if not ch.isalpha() or not ch.isupper():
			raise FormulaError(f"Invalid character '{ch}' in formula '{formula}'")

		symbol = ch
		i += 1
		if i < len(formula) and formula[i].islower():
			symbol += formula[i]
			i += 1

		if symbol not in periodic_table_dict:
			raise FormulaError(f"Unknown element symbol '{symbol}' in formula '{formula}'")

		quantity, i = _parse_number(formula, i)
		stack[-1][symbol] = stack[-1].get(symbol, 0) + quantity

	if len(stack) != 1:
		raise FormulaError(f"Unmatched '(' in formula '{formula}'")

	return list(stack[0].items())


def _parse_number(text, index):
	"""Parse a positive integer from text[index:], defaulting to 1."""
	start = index
	while index < len(text) and text[index].isdigit():
		index += 1
	if start == index:
		return 1, index
	return int(text[start:index]), index


def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
	"""Compute molar mass in g/mol for the parsed symbol quantities."""
	total_mass = 0.0
	for symbol, quantity in symbol_quantity_list:
		atomic_mass = periodic_table_dict[symbol][1]
		total_mass += atomic_mass * quantity
	return total_mass
