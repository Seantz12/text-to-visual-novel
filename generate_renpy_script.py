import re

# some notes to keep in mind for configs:
# gui.rpy takes care of all the graphics settings
# change nvl_height to none
# nvl_spacing to 15
# maybe make it more customisable?
# 6 lines before clear at all times? fuck it we ball and keep it like that


# we know a monologue block is surrounded by """test... """
# the question is, how do we break up the spacing?

config = {
    "max_lines": 6
}

def insert_script(script):
   with open('base_script.rpy', 'r') as file:
      file_contents = file.read()

      updated_contents = file_contents.replace('script', script)

   with open('script.rpy', 'w') as file:
      file.write(updated_contents)


# lets start nice and easy, put a .txt with our desired script and go from there

def parse_line(line):
    # split up sentences (.) and remove footmarks?
    # first get rid of any footnote markings
    # we will have to deal with quotes and sentences later ugh
    line = re.sub(r'(\[[0-9]*\])*?', '', line)
    return [x for x in re.split('([\.\?\!])', line) if x != '\n'] # ignore empty lines

def convert_line_to_renpy_line(line):
    pass

# this gonna have triple clears but whatever we ball

def read_file():
    script = ""
    with open("sample.txt", "r", encoding='utf-8') as file:
        paragraphs = file.readlines()
        for paragraph in paragraphs:
            line_count = 0
            lines = parse_line(paragraph)
            for line in lines:
                script += line.strip()
                if line in ['.', '!', '?']:
                    script += "\n\n"
                    line_count += 1
                    if line_count % config['max_lines'] == 0:
                        script += "\n\n{clear}"
            script += "\n\n" 
            if line_count % config['max_lines'] != 0:
                script += "{clear}\n\n"
    return script



if __name__ == '__main__':
    print("hello!")
    script = read_file()
    insert_script(script)
