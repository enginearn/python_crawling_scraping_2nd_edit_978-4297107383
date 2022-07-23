### フォント一覧を確認するサンプルコード
import matplotlib.font_manager as fm
import pprint

font_list = [fm.FontProperties(fname=font).get_name() for font in fm.findSystemFonts()]

pprint.pprint(font_list)