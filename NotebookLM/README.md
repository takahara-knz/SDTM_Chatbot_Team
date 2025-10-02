# Notebook LM に関する内容

## 💾 データ
- Notebook LM に読み込ませるファイルは、Data フォルダに入れてください

## 📃 ログ
- Notebook LM のログは、Log フォルダに入れてください

## 🤖 プログラム
- Notebook LM 関連で作成したプログラムは、Code フォルダに入れてください

# Notebook LM で、SDTMチャットボット環境を作る方法
1. Notebook LM をブラウザで立ち上げる　https://notebooklm.google/ → Notebook LM を試す → +新規作成
2. ソース → +追加　で、SDTMIGの読み込みたいバージョン（今のところterminologyのテキストファイルとの兼ね合いで3.3推奨）およびその周辺ドキュメントのPDFをアップロードする
3. 同様に、Data フォルダのテキストファイル2つをアップロードする
4. 以下の文をプロンプト欄に貼り付ける（例示ですので、適宜変更してください）
   - SDTMIG_v3.3_FINAL.pdfは、CDISC/SDTMのルールが記載されています。基本的にはここに書いてあることから回答してください。あと2つの補助的なテキストファイルがあります。TermMerge.txtは、Findings系ドメインにおける、xxTESTCDとxxTESTをペアにしたもので、Findings系ドメインにおけるTEST項目の設計に特化しています。Findings系ドメインは、項目名（例えば白血球数）がSDTMIG内にはなく、LBドメインのLBTESTCDとLBTESTに白血球数のデータを入れることで作成するので、このTermMerge.txtを検索することが必要となります。また、逆に「白血球数のドメインは？」というような問いには、このファイルを検索することで、ドメイン名を引き当てることもできます。TermSel.txtは、xxTESTCDとxxTEST以外のTerminologyについて書かれています。例えば、SDTMIG上に"FRM"というTerminologyから探して入力しなさい、と書かれていれば、このファイル内のFRMから探せばよいわけです。回答の根拠は、まずSDTMIG_v3.3_FINAL.pdfから探してください。補助ファイルは補完的に使用してください。
6. 質問をプロンプト欄に入力する
