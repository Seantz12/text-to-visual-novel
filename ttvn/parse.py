class Parser:

    STOP_CHARS = set(".?!")
    POST_STOP_CHARS = set(")\"")
    LINEBREAK_CHARS = set("\n\r")
    SPACE_CHARS = set(" ")
    WHITESPACE_CHARS = LINEBREAK_CHARS | SPACE_CHARS

    UPPERCASE_CHARS = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    LOWERCASE_CHARS = set("abcdefghijklmnopqrstuvwxyz")

    ALPHA_CHARS = UPPERCASE_CHARS | LOWERCASE_CHARS
    DIGIT_CHARS = set("0123456789")

    ALPHANUMERIC_CHARS = ALPHA_CHARS | DIGIT_CHARS

    LINES_PER_PARAGRAPH = 6

    def __init__(self):
        self.__raw = ""
        self.__parsed = []

    @property
    def raw(self):
        return self.__raw

    @property
    def parsed(self):
        return self.__parsed
    
    def __reset(self):
        self.__raw = ""
        self.__parsed = []
    
    def parse_text(self, text: str):
        """Parse a raw text string into a renpy friendly data structure.

        Args:
            text (str): The text to convert.
        """
        self.__reset()

        paragraph = []
        sentence = ""
        n = len(text)
        prev_c = None
        i = 0
        while i < n:
            c = text[i]
            prev_c = text[i - 1] if i > 0 else ''
            next_c = text[i + 1] if i < n - 1 else ''
            self.__raw += c

            # We only consider a sentence possibly done if we hit
            # whitespace or 'post-stop' characters.
            if c in (self.WHITESPACE_CHARS | self.POST_STOP_CHARS):
                if prev_c in self.WHITESPACE_CHARS:
                    if c in self.POST_STOP_CHARS:
                        sentence += c
                    elif (
                        c in self.LINEBREAK_CHARS 
                        and prev_c in self.LINEBREAK_CHARS
                    ):
                        # We consider a paragraph break as two consecutive linebreaks
                        if sentence:
                            paragraph.append(sentence.strip())
                            sentence = ""
                        if paragraph:
                            self.__parsed.append(paragraph)
                            paragraph = []
                elif prev_c in self.STOP_CHARS:
                    # If we are at a stop char, we should look ahead
                    # to confirm a new sentence is ahead. We do this 
                    # naively by checking if first alpha character up
                    # ahead is uppercase.
                    new_sentence_ahead = False
                    look_ahead = i
                    while look_ahead < n:
                        next_c = text[look_ahead]
                        if next_c in self.ALPHANUMERIC_CHARS:
                            if next_c in self.UPPERCASE_CHARS | self.DIGIT_CHARS:
                                new_sentence_ahead = True
                            break
                        look_ahead += 1
                    if new_sentence_ahead:
                        if sentence:
                            sentence += c if c in self.POST_STOP_CHARS else ''
                            paragraph.append(sentence.strip())
                            sentence = ""
                    else:
                        sentence += c
                    if len(paragraph) == self.LINES_PER_PARAGRAPH:
                        self.__parsed.append(paragraph)
                        paragraph = []
                else:
                    # Ignore linebreaks
                    sentence += '' if c in self.LINEBREAK_CHARS else c
            else:
                sentence += c
            i += 1
        # Cleanup any buffers.
        if sentence:
            paragraph.append(sentence)
        if paragraph:
            self.__parsed.append(paragraph)
                    