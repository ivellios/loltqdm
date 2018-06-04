from tqdm import tqdm
from localolcat import LolCat


class Options:
    os = 0
    animate = False
    force = False
    charset_py2 = 'utf-8'
    spread = 3.0
    freq = 0.1
    duration = 12
    speed = 20.0
    mode = 16


class loltqdm(tqdm):
    options = Options()

    @classmethod
    def status_printer(cls, file):
        fp = file
        fp_flush = getattr(fp, 'flush', lambda: None)  # pragma: no cover


        def fp_write(s):
            # fp.write(_unicode(s))
            lolcat = LolCat()
            lolcat.cat([s], cls.options)

            fp_flush()

        last_len = [0]

        def print_status(s):
            len_s = len(s)
            fp_write('\r' + s + (' ' * max(last_len[0] - len_s, 0)))
            last_len[0] = len_s

        return print_status

    def moveto(self, n):
        self.options.os -= n
        super(loltqdm, self).moveto(n)



# ORIGINAL
# @staticmethod
# def status_printer(file):
#     """
#     Manage the printing and in-place updating of a line of characters.
#     Note that if the string is longer than a line, then in-place
#     updating may not work (it will print a new line at each refresh).
#     """
#     fp = file
#     fp_flush = getattr(fp, 'flush', lambda: None)  # pragma: no cover
#
#     def fp_write(s):
#
#         fp_flush()
#
#     last_len = [0]
#
#     def print_status(s):
#         len_s = len(s)
#         fp_write('\r' + s + (' ' * max(last_len[0] - len_s, 0)))
#         last_len[0] = len_s
#
#     return print_status
