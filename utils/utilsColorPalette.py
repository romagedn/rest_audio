

import colorsys
import math

class UtilsColorPalette:
    rgb_colors = None

    @staticmethod
    def get_hls_colors():
        hls_colors = []

        hs = [x / 360 for x in [0, 20, 40, 70, 120, 180, 210, 240, 280, 300, 330, ]]
        ss = [x / 100 for x in [55, 100]]
        ls = [x / 100 for x in [50, 20, 80]]

        for l in ls:
            for s in ss:
                for h in hs:
                    hls_colors.append([h, l, s])

        return hls_colors

    @staticmethod
    def get_rgb_colors():
        if UtilsColorPalette.rgb_colors is None:
            rgb_colors = []
            hls_colors = UtilsColorPalette.get_hls_colors()
            for hlsc in hls_colors:
                _r, _g, _b = colorsys.hls_to_rgb(hlsc[0], hlsc[1], hlsc[2])
                r, g, b = [int(x * 255.0) for x in (_r, _g, _b)]
                code = '#' +\
                       hex(r).replace('0x', '').rjust(2, '0') +\
                       hex(g).replace('0x', '').rjust(2, '0') +\
                       hex(b).replace('0x', '').rjust(2, '0')
                code = code.replace('0x', '')
                rgb_colors.append(code)

            UtilsColorPalette.rgb_colors = rgb_colors

        return UtilsColorPalette.rgb_colors
