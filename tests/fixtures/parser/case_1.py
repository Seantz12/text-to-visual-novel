from textwrap import dedent

INPUT = dedent("""
It was the best of times;  it was the worst of times. "Stop, fiend!" he yelled. 
The knave replied: "Catch me if you dare..."
"With pleasure," shot back the hunter, brandishing her blade.
(No one moved.) (No one moved.) (No one moved.) (No one moved.) (No one moved.)
(No one moved.) (No one moved.) (No one moved.) (No one moved.) (No one moved.)

""")

EXPECTED = [
    [
        "It was the best of times; it was the worst of times.",
        "\"Stop, fiend!\" he yelled.",
        "The knave replied: \"Catch me if you dare...\"",
        "\"With pleasure,\" shot back the hunter, brandishing her blade.",
        "(No one moved.)",
        "(No one moved.)",
    ],
    [
        "(No one moved.)",
        "(No one moved.)",
        "(No one moved.)",
        "(No one moved.)",
        "(No one moved.)",
        "(No one moved.)",
    ],
    [
        "(No one moved.)",
        "(No one moved.)",
    ]
]