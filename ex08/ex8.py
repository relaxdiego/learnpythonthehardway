formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)

# The "But it didn't sing" line will be printed with double quotes
# since it has a single quote character (apostrophe, really) inside.
# The other strings are printed with single quotes because they don't.