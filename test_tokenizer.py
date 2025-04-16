from hindi_tokenizer import HindiTokenizer

def test_tokenizer():
    tokenizer = HindiTokenizer()
    test_text = "हिन्दी एक सुंदर भाषा है। क्या आप सहमत हैं?"
    tokens = tokenizer.tokenize(test_text)
    expected = ['हिन्दी', 'एक', 'सुंदर', 'भाषा', 'है', '।', 'क्या', 'आप', 'सहमत', 'हैं', '?']
    assert tokens == expected, f"Expected {expected}, but got {tokens}"
    print("Test passed successfully!")

if __name__ == "__main__":
    test_tokenizer()
