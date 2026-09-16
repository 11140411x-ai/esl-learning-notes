import json
import os

VOCAB_FILE = "vocabulary.json"

def load_vocab():
    """加载单词库"""
    if os.path.exists(VOCAB_FILE):
        with open(VOCAB_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_vocab(vocab):
    """保存单词库"""
    with open(VOCAB_FILE, "w", encoding="utf-8") as f:
        json.dump(vocab, f, ensure_ascii=False, indent=2)

def add_word(vocab):
    """添加新单词"""
    word = input("请输入英文单词：").strip().lower()
    if word in vocab:
        print(f"单词 {word} 已存在！")
        return
    meaning = input("输入中文释义：").strip()
    example = input("输入例句：").strip()
    vocab[word] = {"meaning": meaning, "example": example}
    print(f"✅ 单词 {word} 添加成功！")

def search_word(vocab):
    """查询单词"""
    word = input("请输入要查询的单词：").strip().lower()
    if word in vocab:
        info = vocab[word]
        print(f"\n单词：{word}")
        print(f"释义：{info['meaning']}")
        print(f"例句：{info['example']}\n")
    else:
        print("❌ 未找到该单词")

def export_words(vocab):
    """导出全部单词到txt"""
    with open("word_list.txt", "w", encoding="utf-8") as f:
        for word, info in vocab.items():
            f.write(f"{word} | {info['meaning']} | {info['example']}\n")
    print("✅ 单词表已导出到 word_list.txt")

def main():
    vocab = load_vocab()
    while True:
        print("\n==== ESL单词助手 ====")
        print("1. 添加单词")
        print("2. 查询单词")
        print("3. 导出单词表")
        print("4. 退出")
        choice = input("\n请选择功能：").strip()
        if choice == "1":
            add_word(vocab)
        elif choice == "2":
            search_word(vocab)
        elif choice == "3":
            export_words(vocab)
        elif choice == "4":
            save_vocab(vocab)
            print("已保存单词库，程序退出")
            break
        else:
            print("输入无效，请重新选择")

if __name__ == "__main__":
    main()
