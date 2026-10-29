# my-skills

[EchoTint](https://github.com/EchoTint) 的个人 Agent Skills 仓库。每个技能的指令、参考资料和辅助脚本放在同一个目录里，可以单独安装。

[English](README.md) | [简体中文](README.zh-CN.md) | [更新日志](CHANGELOG.zh-CN.md)

## 仓库里的技能

| 技能 | 用途 |
| --- | --- |
| [reading-study-coach](skills/reading-study-coach/) | 书籍与论文陪读、多来源主题阅读、自适应学习路线、实践、掌握检查和间隔复习。 |

## 安装

有 Node.js 环境时，可以通过 [Skills CLI](https://github.com/vercel-labs/skills) 发现和安装技能：

```bash
# 先列出技能，不安装。
npx skills add EchoTint/my-skills --list

# 安装阅读教练到当前项目。
npx skills add EchoTint/my-skills --skill reading-study-coach

# 或安装到用户级目录。
npx skills add EchoTint/my-skills --skill reading-study-coach -g
```

也可以把仓库地址交给 Agent，让它读取 `skills/reading-study-coach/SKILL.md`。手动安装时需要整个技能文件夹，不能只复制主文件。使用 Magpie 时，在 Library 中添加技能的本地文件夹，再选择需要启用的 Agent。安装前先检查是否已有同名技能，避免重复副本。

## 阅读学习教练

学习一本书时，先结合目标、正文中的真实前置依赖和已有能力证据安排路线，不默认从第一章顺序学到最后。做主题阅读时，围绕共同问题跨书选读，而不是把几本摘要拼起来。

系统学习保留追问、独立测试、实践通关和间隔复习。读过、提示后答对、独立掌握和长期保持分别记录，不把助手写出的答案当成用户能力。

可以这样开始：

```text
用 $reading-study-coach 陪我学习这本书。
用 $reading-study-coach 围绕这个主题，结合这几本书建立领域全景。
用 $reading-study-coach 检查我是否理解了这篇论文的证据和结论边界。
```

学习记录默认放在当前工作区的 `book-wiki/`。个人阅读记录、书籍正文和私人项目材料不应提交到这个技能仓库。

核心流程是文本指令。可选 PDF 工具需要 Python 3.10+、`pypdf`，处理内嵌图片还需要 Pillow；文本提取也可使用 PyPDF2。OCR 需要可用的 Windows OCR 环境，或 Poppler、Tesseract 及对应语言包。仓库不捆绑或自动安装这些工具，准备图片也不等于已经完成 OCR。

## 目录结构

```text
my-skills/
  README.md
  README.zh-CN.md
  CHANGELOG.md
  CHANGELOG.zh-CN.md
  .github/workflows/validate.yml
  tools/validate_skills.py
  skills/
    reading-study-coach/
      SKILL.md
      THIRD_PARTY_NOTICES.md
      agents/openai.yaml
      references/
      scripts/
```

以后每个独立技能都放进一个新的 `skills/<技能名>/` 目录。详细规则按需放在 `references/`，仓库维护和测试工具放在外层，不塞进技能的执行入口。

在仓库根目录运行结构检查：

```bash
python tools/validate_skills.py
```

检查覆盖技能标识、本地引用、符号链接和 Python 语法，不代表教学效果或所有 OCR 环境已经通过测试。

## 来源与许可

阅读技能融合了自定义规则和其他技能的部分方法、工具。使用时保留 [第三方来源与许可说明](skills/reading-study-coach/THIRD_PARTY_NOTICES.md)。部分上游许可尚未确认，因此仓库不统一声明 MIT，也不表示所有内容都已获得自由再分发授权。再次分发前请核对来源说明和上游条款。

仓库组织参考 [JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design) 的技能目录、中英文入口、独立技能文件夹和外层维护工具，没有复制其设计技能或编辑器代码。
