####################################################################################################
# region TinyLog
# simple console log with color coding, indentation, and timestamps

class TinyLog:
    def __init__(self):
        self.reset()

    def reset(self):
        self.muted : int = 0
        self.start_line : bool = True
        self.indentation : int = 0
        self.use_color : bool = True
        self.current_color : int = 0
        self.time_start = time.time()

    class Indenter:
        def __enter__(self):
            tinylog.indent()
            return self
        def __exit__(self, _1, _2, _3):
            tinylog.dedent()

    class Color:
        def __init__(self, color):
            self.old_color = tinylog.current_color
            self.new_color = color
        def __enter__(self):
            tinylog.current_color = self.new_color
            return self
        def __exit__(self, _1, _2, _3):
            tinylog.current_color = self.old_color

    def indent(self):
        self.indentation += 2
    def dedent(self):
        self.indentation -= 2
    def mute(self):
        self.muted += 1
    def unmute(self):
        self.muted -= 1
    def color_off(self):
        self.use_color = False
    def color_on(self):
        self.use_color = True

    def color(self, c : int):
        if self.muted:
            return self
        if not self.use_color:
            return self
        self.current_color = c
        if (c and self.use_color):
            sys.stdout.write(f"\u001b[38;2;{(c >> 0) & 0xFF};{(c >> 8) & 0xFF};{(c >> 16) & 0xFF}m")
        else:
            sys.stdout.write("\u001b[0m")
        return self

    def _put(self, c : str):
        if self.muted:
            return
        if self.start_line and c == '\r':
            return
        if c == '\r':
            c = '\n'

        if self.start_line:
            old_color = self.current_color
            self.color(0)
            sys.stdout.write(f"[{time.time() - self.time_start:08.3f}] ")
            for _ in range(self.indentation):
                sys.stdout.write(' ')
            self.color(old_color)

        self.start_line = (c == '\n')
        sys.stdout.write(str(c))
        sys.stdout.flush()

    def print(self, text):
        self.write(text, len(text))

    def write(self, text : str, size : int):
        for i in range(size):
            self._put(text[i])
        #sys.stdout.write("\u001b[0m")

tinylog = TinyLog()

COL_BLUE    = 0x00EE8888
COL_SKY     = 0x00EEBB88
COL_TEAL    = 0x00EEEE88
COL_AQUA    = 0x00BBEE88
COL_GREEN   = 0x0088EE88
COL_LIME    = 0x0088EEBB
COL_YELLOW  = 0x0088EEEE
COL_ORANGE  = 0x0088BBEE
COL_RED     = 0x008888EE
COL_PINK    = 0x00BB88EE
COL_MAGENTA = 0x00EE88EE
COL_VIOLET  = 0x00EE88BB

COLORS = [
    COL_BLUE, COL_SKY, COL_TEAL, COL_AQUA, COL_GREEN, COL_LIME,
    COL_YELLOW, COL_ORANGE, COL_RED, COL_PINK, COL_MAGENTA, COL_VIOLET
]


def LOG(text)      : tinylog.color(0x00000000) .print(text)
def LOG_C(c, text) : tinylog.color(c         ) .print(text)
def LOG_W(text)    : tinylog.color(0x00FFFFFF) .print(text)
def LOG_B(text)    : tinylog.color(COL_BLUE   ).print(text)
def LOG_S(text)    : tinylog.color(COL_SKY    ).print(text)
def LOG_T(text)    : tinylog.color(COL_TEAL   ).print(text)
def LOG_A(text)    : tinylog.color(COL_AQUA   ).print(text)
def LOG_G(text)    : tinylog.color(COL_GREEN  ).print(text)
def LOG_L(text)    : tinylog.color(COL_LIME   ).print(text)
def LOG_Y(text)    : tinylog.color(COL_YELLOW ).print(text)
def LOG_O(text)    : tinylog.color(COL_ORANGE ).print(text)
def LOG_R(text)    : tinylog.color(COL_RED    ).print(text)
def LOG_P(text)    : tinylog.color(COL_PINK   ).print(text)
def LOG_M(text)    : tinylog.color(COL_MAGENTA).print(text)
def LOG_V(text)    : tinylog.color(COL_VIOLET ).print(text)


#endregion