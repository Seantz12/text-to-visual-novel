from textwrap import dedent

INPUT = dedent("""
And Theoden stared at the doom that lay before him, and it inflamed a 
blood red rage within him. He spurred his horse onward, holding his 
blade aloft as he dragged it along the spear shafts of his Rohirrim. 
The sound of steel clashing against wood awoke the fire that burns in men when  
they see death before them.

"Arise, arise, riders of Theoden!" the king roared. "Fell deeds awake: fire and slaughter!" 
The horselords echoed in response. "Spear shall be shaken; shield shall be splintered. 
A sword day - a red day! - ere the sun rises."
""")

EXPECTED = [
    [
        "And Theoden stared at the doom that lay before him, and it inflamed a blood red rage within him.",
        "He spurred his horse onward, holding his blade aloft as he dragged it along the spear shafts of his Rohirrim.",
        "The sound of steel clashing against wood awoke the fire that burns in men when they see death before them.",
    ],
    [
        "\"Arise, arise, riders of Theoden!\" the king roared.",
        "\"Fell deeds awake: fire and slaughter!\"",
        "The horselords echoed in response.",
        "\"Spear shall be shaken; shield shall be splintered.",
        "A sword day - a red day! - ere the sun rises.\""
    ],
]