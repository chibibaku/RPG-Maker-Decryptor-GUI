# RPG-Maker-Decryptor-GUI
このスクリプトは、RPGツクールMV用のリソース復号化ツールです。
<br/>Tkinter(tk,filedialog,messagebox)でGUI wrappingしています。
<br/>Pyinstallerでexe化して使用する事を想定しています。

# Usage / 使用方法
## Build / ビルド
> git clone https://github.com/chibibaku/RPG-Maker-Decryptor-GUI
> 
> cd RPG-Maker-Decryptor-GUI
> 
> pyinstaller ./GUI.py --onefile [optional: --noconsole]

## Run / 実行
- 任意の場所にexeを配置し、実行します。
  - 推奨：復号化したいゲームのルートフォルダと同じ位置
- 必要な項目を埋めていきます。
  - Game Directory
    - ゲームのルートフォルダーです。
  - Target File
    - 復号化したいファイルを選択します。(複数可)
    - ``.rpgmvo, .rpgmvm, .rpgmvp, .png_, .ogg_``に対応しています。
  - Output Directory
    - ファイルの出力先です。
  - Key
    - 復号化キーです。
    - Game Directoryが正しく選択された状態で"Get Key"を押すと内部JSONから自動で読み取られます。
- [Decrypt]を押して復号化します。
- 復号化されたファイルはOutput Directoryの位置に保存されます。


# License / ライセンス
- MIT License

# Copyright / 著作権表記
- 複合化部分：[netherpills/RPG-Maker-MV-File-Decryptor.py](https://github.com/netherpills/RPG-Maker-MV-File-Decryptor.py)
