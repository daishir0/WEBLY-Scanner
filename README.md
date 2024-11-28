# WEBLY-Scanner

## Overview
WEBLY-Scanner is a Python tool designed to check web pages for compliance with Web Content Accessibility Guidelines (WCAG) 2.1 criteria. It aims to support various WCAG success criteria and can be expanded to include more checks in the future.

## Installation
To install WEBLY-Scanner, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/daishir0/webly-scanner
   ```
2. Change to the project directory:
   ```
   cd webly-scanner
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
WEBLY-Scanner can be used in two ways:

### 1. Check all implemented WCAG criteria
```
python main.py <url>
```

### 2. Check a specific WCAG criterion
```
python main.py <url> <criterion>
```

Examples:
```
# Check all criteria
python main.py https://example.com

# Check only WCAG 1.1.1
python main.py https://example.com 1.1.1
```

The tool will perform the specified checks and display detailed results in the console, including:
- Overall pass/fail status
- Individual check results for each criterion
- Specific details about any failures found

## Features
- Modular design allowing easy addition of new WCAG criteria checks
- Ability to test specific WCAG criteria individually
- Detailed reporting of test results
- Automatic detection and loading of implemented checkers

## Notes
- This tool performs automated checks for the implemented WCAG criteria. It may not cover all accessibility issues, and manual review is still necessary for comprehensive accessibility testing.
- Some checks may require further development for more accurate results.
- The tool is designed to be extensible, allowing for the addition of more WCAG criteria checks in the future.
- Ensure you have permission to test the websites you're checking.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

---

# WEBLY-Scanner

## 概要
WEBLY-ScannerはWeb Content Accessibility Guidelines (WCAG) 2.1基準に対するウェブページの準拠性をチェックするために設計されたPythonツールです。様々なWCAG達成基準をサポートすることを目指しており、将来的にはさらに多くのチェック項目を追加できるように設計されています。

## インストール方法
WEBLY-Scannerをインストールするには、以下の手順に従ってください：

1. リポジトリをクローンします：
   ```
   git clone https://github.com/daishir0/webly-scanner
   ```
2. プロジェクトディレクトリに移動します：
   ```
   cd webly-scanner
   ```
3. 必要な依存関係をインストールします：
   ```
   pip install -r requirements.txt
   ```

## 使い方
WEBLY-Scannerは2つの方法で使用できます：

### 1. 実装されているすべてのWCAG基準をチェック
```
python main.py <url>
```

### 2. 特定のWCAG達成基準のみをチェック
```
python main.py <url> <criterion>
```

使用例：
```
# すべての基準をチェック
python main.py https://example.com

# WCAG 1.1.1のみをチェック
python main.py https://example.com 1.1.1
```

ツールは指定されたチェックを実行し、以下を含む詳細な結果をコンソールに表示します：
- 全体的な合否状態
- 各基準における個別のチェック結果
- 不合格項目の詳細情報

## 特徴
- 新しいWCAG基準チェックを容易に追加できるモジュラー設計
- 特定のWCAG基準を個別にテスト可能
- テスト結果の詳細なレポート
- 実装されているチェッカーの自動検出と読み込み

## 注意点
- このツールは実装されているWCAG基準に対する自動チェックを実行します。すべてのアクセシビリティの問題を検出できるわけではなく、包括的なアクセシビリティテストには手動でのレビューが依然として必要です。
- 一部のチェックはより正確な結果を得るためにさらなる開発が必要な場合があります。
- このツールは拡張可能に設計されており、将来的に更多くのWCAG基準チェックを追加することができます。
- チェックするウェブサイトのテスト許可を得ていることを確認してください。

## ライセンス
このプロジェクトはMITライセンスの下でライセンスされています。詳細はLICENSEファイルを参照してください。
