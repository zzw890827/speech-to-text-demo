import re


if __name__ == '__main__':
    temp = r'音声 認識 の 現状 に ついて 教えて いただけ ない でしょう か はい 最近 では 音声 認識 でも ディープ ラーニング が よく つく 使われて ます ねえ それ は どう いった もの なの でしょう か 簡単 に 言えば 脳 の 仕組み を モデル に した 技術 です それ は 難しそう ですね 一部 では 人間 の 能力 を 超える まで に なって います'
    word = r'音声'
    for match in re.finditer(word, temp):
        print("match found from {} to {}".format(match.start(), match.end()))
