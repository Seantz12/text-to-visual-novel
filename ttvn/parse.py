class Parser:

    STOP_CHARS = set(".?!")
    POST_STOP_CHARS = set(")\"")
    LINEBREAK_CHARS = set("\n\r")
    SPACE_CHARS = set(" ")
    WHITESPACE_CHARS = LINEBREAK_CHARS | SPACE_CHARS

    UPPERCASE_CHARS = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    LOWERCASE_CHARS = set("abcdefghijklmnopqrstuvwxyz")

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
    
    def parse_text(self, text: str):
        """Parse a raw text string into a renpy friendly data structure.

        Args:
            text (str): The text to convert.
        """
        paragraph = []
        sentence = ""
        n = len(text)
        for i, c in enumerate(text):
            self.__raw += c
            # We only consider a sentence possibly done if we hit
            # whitespace or 'post-stop' characters.
            if c in (self.WHITESPACE_CHARS | self.POST_STOP_CHARS):
                if not sentence:
                    sentence += c if c in self.POST_STOP_CHARS else ''
                    continue
                elif sentence[-1] in self.WHITESPACE_CHARS:
                    sentence += c if c in self.POST_STOP_CHARS else ''
                    continue
                elif sentence[-1] in self.STOP_CHARS:
                    sentence += c if c in self.POST_STOP_CHARS else ''
                    # If we are at a stop char, we should look ahead
                    # to confirm a new sentence is ahead. We do this 
                    # naively by checking if first alpha character up
                    # ahead is uppercase.
                    new_sentence_ahead = False
                    look_ahead = i
                    while look_ahead < n:
                        if text[look_ahead] in self.UPPERCASE_CHARS | self.LOWERCASE_CHARS:
                            if text[look_ahead] in self.UPPERCASE_CHARS:
                                new_sentence_ahead = True
                            break
                        look_ahead += 1
                    if new_sentence_ahead:
                        paragraph.append(sentence)
                        sentence = ""
                else:
                    # Always ignore line breaks.
                    sentence += '' if c in self.LINEBREAK_CHARS else c
            else:
                sentence += c
            if len(paragraph) == self.LINES_PER_PARAGRAPH:
                self.__parsed.append(paragraph)
                paragraph = []
        # Cleanup any buffers.
        if sentence:
            paragraph.append(sentence)
        if paragraph:
            self.__parsed.append(paragraph)
                    