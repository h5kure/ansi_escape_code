#!/usr/bin/env python3

# ANSI escape code wikipedia: https://en.wikipedia.org/wiki/ANSI_escape_code

import sys


class ansi_escape_code:
    NORMAL = '\033[0m'  # Reset / Normal
    BOLD = '\033[1m'  # Bold or increased intensity
    FAINT = '\033[2m'  # decreased intensity. Not widely supported
    ITALIC = '\033[3m'  # Not widely supported. Sometimes treated as inverse.
    UNDERLINE = '\033[4m'  # underline
    SLOW_BLINK = '\033[5m'  # less than 150 per minute
    RAPID_BLINK = '\033[6m'  # MS-DOS ANSI.SYS; 150+ per minute; not widely supported.
    REVERSE_VIDEO = '\033[7m'  #swap foreground and background colors
    CONCEAL = '\033[8m'  # not widely supported
    CROSSED_OUT = '\033[9m'  # Characters legible, but marked for deletion. Not widely supported.
    PRIMARY_FONT = '\033[10m'
    FRAKTUR = '\033[20m'  # hardly ever supported
    BOLD_OFF = '\033[21m'  # not widely supported
    DOUBLE_UNDERLINE = '\033[21m'  # hardly ever supported
    NORMAL_COLOR = '\033[22m'  # neither bold nor faint
    NORMAL_INTENSITY = '\033[22m'  # neither bold nor faint
    NOT_ITALIC = '\033[23m'
    NOT_FRAKTUR = '\033[23m'
    UNDERLINE_OFF = '\033[24m'  # not singly or doubly underlined
    BLINK_OFF = '\033[25m'
    INVERSE_OFF = '\033[27m'
    REVEAL = '\033[28m'  # conceal off
    NOT_CROSSED_OUT = '\033[29m'
    FG_BLACK = '\033[30m'
    FG_RED = '\033[31m'
    FG_GREEN = '\033[32m'
    FG_YELLOW = '\033[33m'
    FG_BLUE = '\033[34m'
    FG_MAGENTA = '\033[35m'
    FG_CYAN = '\033[36m'
    FG_WHITE = '\033[37m'
    FG_BRIGHT_BLACK = '\033[90m'
    FG_BRIGHT_RED = '\033[91m'
    FG_BRIGHT_GREEN = '\033[92m'
    FG_BRIGHT_YELLOW = '\033[93m'
    FG_BRIGHT_BLUE = '\033[94m'
    FG_BRIGHT_MAGENTA = '\033[95m'
    FG_BRIGHT_CYAN = '\033[96m'
    FG_BRIGHT_WHITE = '\033[97m'
    FG_DEFAULT_COLOR = '\033[39m'
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'
    BG_BRIGHT_BLACK = '\033[100m'
    BG_BRIGHT_RED = '\033[101m'
    BG_BRIGHT_GREEN = '\033[102m'
    BG_BRIGHT_YELLOW = '\033[103m'
    BG_BRIGHT_BLUE = '\033[104m'
    BG_BRIGHT_MAGENTA = '\033[105m'
    BG_BRIGHT_CYAN = '\033[106m'
    BG_BRIGHT_WHITE = '\033[107m'
    BG_DEFAULT_COLOR = '\033[49m'
    FRAMED = '\033[51m'
    ENCIRCLED = '\033[52m'
    OVERLINED = '\033[53m'
    NOT_FRAMED = '\033[54m'
    NOT_OVERLINED = '\033[55m'

    codes = {
        'NORMAL': '\033[0m',  # Reset / Normal
        'BOLD': '\033[1m',  # Bold or increased intensity
        'FAINT': '\033[2m',  # decreased intensity. Not widely supported
        'ITALIC': '\033[3m',  # Not widely supported. Sometimes treated as inverse.
        'UNDERLINE': '\033[4m',  # underline
        'SLOW_BLINK': '\033[5m',  # less than 150 per minute
        'RAPID_BLINK': '\033[6m',  # MS-DOS ANSI.SYS; 150+ per minute; not widely supported.
        'REVERSE_VIDEO': '\033[7m',  #swap foreground and background colors
        'CONCEAL': '\033[8m',  # not widely supported
        'CROSSED_OUT': '\033[9m',  # Characters legible, but marked for deletion. Not widely supported.
        'PRIMARY_FONT': '\033[10m',
        'FRAKTUR': '\033[20m',  # hardly ever supported
        'BOLD_OFF': '\033[21m',  # not widely supported
        'DOUBLE_UNDERLINE': '\033[21m',  # hardly ever supported
        'NORMAL_COLOR': '\033[22m',  # neither bold nor faint
        'NORMAL_INTENSITY': '\033[22m',  # neither bold nor faint
        'NOT_ITALIC': '\033[23m',
        'NOT_FRAKTUR': '\033[23m',
        'UNDERLINE_OFF': '\033[24m',  # not singly or doubly underlined
        'BLINK_OFF': '\033[25m',
        'INVERSE_OFF': '\033[27m',
        'REVEAL': '\033[28m',  # conceal off
        'NOT_CROSSED_OUT': '\033[29m',
        'FG_BLACK': '\033[30m',
        'FG_RED': '\033[31m',
        'FG_GREEN': '\033[32m',
        'FG_YELLOW': '\033[33m',
        'FG_BLUE': '\033[34m',
        'FG_MAGENTA': '\033[35m',
        'FG_CYAN': '\033[36m',
        'FG_WHITE': '\033[37m',
        'FG_BRIGHT_BLACK': '\033[90m',
        'FG_BRIGHT_RED': '\033[91m',
        'FG_BRIGHT_GREEN': '\033[92m',
        'FG_BRIGHT_YELLOW': '\033[93m',
        'FG_BRIGHT_BLUE': '\033[94m',
        'FG_BRIGHT_MAGENTA': '\033[95m',
        'FG_BRIGHT_CYAN': '\033[96m',
        'FG_BRIGHT_WHITE': '\033[97m',
        'FG_DEFAULT_COLOR': '\033[39m',
        'BG_BLACK': '\033[40m',
        'BG_RED': '\033[41m',
        'BG_GREEN': '\033[42m',
        'BG_YELLOW': '\033[43m',
        'BG_BLUE': '\033[44m',
        'BG_MAGENTA': '\033[45m',
        'BG_CYAN': '\033[46m',
        'BG_WHITE': '\033[47m',
        'BG_BRIGHT_BLACK': '\033[100m',
        'BG_BRIGHT_RED': '\033[101m',
        'BG_BRIGHT_GREEN': '\033[102m',
        'BG_BRIGHT_YELLOW': '\033[103m',
        'BG_BRIGHT_BLUE': '\033[104m',
        'BG_BRIGHT_MAGENTA': '\033[105m',
        'BG_BRIGHT_CYAN': '\033[106m',
        'BG_BRIGHT_WHITE': '\033[107m',
        'BG_DEFAULT_COLOR': '\033[49m',
        'FRAMED': '\033[51m',
        'ENCIRCLED': '\033[52m',
        'OVERLINED': '\033[53m',
        'NOT_FRAMED': '\033[54m',
        'NOT_OVERLINED': '\033[55m',
    }

    def __init__(self):
        if not self.supports_color():
            self.disable()

    def supports_color(self):
        """
        Returns True if the running system's terminal supports color, and False
        otherwise.
        """
        plat = sys.platform
        supported_platform = plat != 'Pocket PC' and (plat != 'win32' or
                                                      'ANSICON' in os.environ)
        # isatty is not always implemented, #6223.
        is_a_tty = hasattr(sys.stdout, 'isatty') and sys.stdout.isatty()
        if not supported_platform or not is_a_tty:
            return False
        return True

    def get(self, code):
        return self.codes.get(code.upper(), '')

    def disable(self):
        for key, value in self.codes.items():
            self.codes[key] = ''

class ansi_wrapped_string(ansi_escape_code):
    def __init__(self, code, string):
        ansi_escape_code.__init__(self)
        code_start = ''
        code_end = self.get('normal')
        if isinstance(code, list):
            for c in code:
                code_start += self.get(c)
        else:
            code_start = self.get(code)
        self.value = '{start}{string}{end}'.format(
            string=string, start=code_start, end=code_end)

    def __str__(self):
        return self.value

if __name__ == '__main__':
    print(ansi_wrapped_string('bold', 'bold'))
    print(ansi_wrapped_string('faint', 'faint'))
    print(ansi_wrapped_string('italic', 'italic'))
    print(ansi_wrapped_string('underline', 'underline'))
    print(ansi_wrapped_string('slow_blink', 'slow_blink'))
    print(ansi_wrapped_string('rapid_blink', 'rapid_blink'))
    print(ansi_wrapped_string('reverse_video', 'reverse_video'))
    print(ansi_wrapped_string('conceal', 'conceal'))
    print(ansi_wrapped_string('crossed_out', 'crossed_out'))
    print(ansi_wrapped_string('primary_font', 'primary_font'))
    print(ansi_wrapped_string('fraktur', 'fraktur'))
    print(ansi_wrapped_string(['bold', 'bold_off'], 'bold_off'))
    print(ansi_wrapped_string('double_underline', 'double_underline'))
    print(ansi_wrapped_string('framed', 'framed'))
    print(ansi_wrapped_string('encircled', 'encircled'))
    print(ansi_wrapped_string('overlined', 'overlined'))
    print(ansi_wrapped_string('fg_black', 'fg_black'))
    print(ansi_wrapped_string('fg_red', 'fg_red'))
    print(ansi_wrapped_string('fg_green', 'fg_green'))
    print(ansi_wrapped_string('fg_yellow', 'fg_yellow'))
    print(ansi_wrapped_string('fg_blue', 'fg_blue'))
    print(ansi_wrapped_string('fg_magenta', 'fg_magenta'))
    print(ansi_wrapped_string('fg_cyan', 'fg_cyan'))
    print(ansi_wrapped_string('fg_white', 'fg_white'))
    print(ansi_wrapped_string('fg_bright_black', 'fg_bright_black'))
    print(ansi_wrapped_string('fg_bright_red', 'fg_bright_red'))
    print(ansi_wrapped_string('fg_bright_green', 'fg_bright_green'))
    print(ansi_wrapped_string('fg_bright_yellow', 'fg_bright_yellow'))
    print(ansi_wrapped_string('fg_bright_blue', 'fg_bright_blue'))
    print(ansi_wrapped_string('fg_bright_magenta', 'fg_bright_magenta'))
    print(ansi_wrapped_string('fg_bright_cyan', 'fg_bright_cyan'))
    print(ansi_wrapped_string('fg_bright_white', 'fg_bright_white'))
    print(ansi_wrapped_string('fg_default_color', 'fg_default_color'))
    print(ansi_wrapped_string('bg_black', 'bg_black'))
    print(ansi_wrapped_string('bg_red', 'bg_red'))
    print(ansi_wrapped_string('bg_green', 'bg_green'))
    print(ansi_wrapped_string('bg_yellow', 'bg_yellow'))
    print(ansi_wrapped_string('bg_blue', 'bg_blue'))
    print(ansi_wrapped_string('bg_magenta', 'bg_magenta'))
    print(ansi_wrapped_string('bg_cyan', 'bg_cyan'))
    print(ansi_wrapped_string('bg_white', 'bg_white'))
    print(ansi_wrapped_string('bg_bright_black', 'bg_bright_black'))
    print(ansi_wrapped_string('bg_bright_red', 'bg_bright_red'))
    print(ansi_wrapped_string('bg_bright_green', 'bg_bright_green'))
    print(ansi_wrapped_string('bg_bright_yellow', 'bg_bright_yellow'))
    print(ansi_wrapped_string('bg_bright_blue', 'bg_bright_blue'))
    print(ansi_wrapped_string('bg_bright_magenta', 'bg_bright_magenta'))
    print(ansi_wrapped_string('bg_bright_cyan', 'bg_bright_cyan'))
    print(ansi_wrapped_string('bg_bright_white', 'bg_bright_white'))

    print(ansi_wrapped_string(['fg_red', 'bg_white', 'underline'], 'fg_red & bg_white & underline'))
