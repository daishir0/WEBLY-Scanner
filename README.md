# WCAG Checker

## Overview
WCAG Checker is a Python tool designed to check web pages for compliance with Web Content Accessibility Guidelines (WCAG) 2.1 criteria. It aims to support various WCAG success criteria and can be expanded to include more checks in the future.

## Installation
To install WCAG Checker, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/daishir0/wcag_checker
   ```
2. Change to the project directory:
   ```
   cd wcag_checker
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
To use WCAG Checker, run the main.py script with a URL as an argument:

```
python main.py <url>
```

Replace `<url>` with the web page URL you want to check.

The tool will perform checks for the implemented WCAG criteria and display the results in the console.

## Notes
- This tool performs automated checks for the implemented WCAG criteria. It may not cover all accessibility issues, and manual review is still necessary for comprehensive accessibility testing.
- Some checks may require further development for more accurate results.
- The tool is designed to be extensible, allowing for the addition of more WCAG criteria checks in the future.
- Ensure you have permission to test the websites you're checking.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

---

# WCAG Checker

## 概要
WCAG Checkerは、Web Content Accessibility Guidelines (WCAG) 2.1基準に対するウェブページの準拠性をチェックするために設計されたPythonツールです。様々なWCAG達成基準をサポートすることを目指しており、将来的にはさらに多くのチェック項目を追加できるように設計されています。

## インストール方法
WCAG Checkerをインストールするには、以下の手順に従ってください：

1. リポジトリをクローンします：
   ```
   git clone https://github.com/daishir0/wcag_checker
   ```
2. プロジェクトディレクトリに移動します：
   ```
   cd wcag_checker
   ```
3. 必要な依存関係をインストールします：
   ```
   pip install -r requirements.txt
   ```

## 使い方
WCAG Checkerを使用するには、main.pyスクリプトをURLを引数として実行します：

```
python main.py <url>
```

`<url>`をチェックしたいウェブページのURLに置き換えてください。

ツールは実装されているWCAG基準に対するチェックを実行し、結果をコンソールに表示します。

## 注意点
- このツールは実装されているWCAG基準に対する自動チェックを実行します。すべてのアクセシビリティの問題を検出できるわけではなく、包括的なアクセシビリティテストには手動でのレビューが依然として必要です。
- 一部のチェックはより正確な結果を得るためにさらなる開発が必要な場合があります。
- このツールは拡張可能に設計されており、将来的に更多くのWCAG基準チェックを追加することができます。
- チェックするウェブサイトのテスト許可を得ていることを確認してください。

## ライセンス
このプロジェクトはMITライセンスの下でライセンスされています。詳細はLICENSEファイルを参照してください。