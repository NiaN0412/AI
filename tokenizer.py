import urllib.request
import re
url = ("https://raw.githubusercontent.com/rasbt/"
       "LLMs-from-scratch/main/ch02/01_main-chapter-code/"
       "the-verdict.txt")

file_path = "the-verdict.txt"
urllib.request.urlretrieve(url, file_path)
with open(file_path, "r", encoding="utf-8") as f:
    raw_text = f.read()
preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)',raw_text)
preprocessed = [item for item in preprocessed if item.strip()]# 斷詞網址裡的文本
all_words = sorted(set(preprocessed))# 變成詞彙表
vocab_size = len(all_words)# 詞彙表長度

class SimpltexteTokenizerV1:
  def __init__(self,vocab):
    self.str_to_int = vocab
    self.int_to_str = {i:s for s,i in vocab.items()}

  def encode(self,text):
    preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)',raw_text)
    preprocessed = [item.strip()for item in preprocessed if item.strip()]
    ids = [self.str_to_int[s]for s in preprocessed]
    return ids

  def decode(self,ids):
    text = " ".join([self.int_to_str[i]for i in ids])

    text = re.sub(r'\s+([,."()\'])',r'\1',text)
    return text

all_token = sorted(list(set(preprocessed)))
all_token.extend(["<|endoftext|>","<|unk|>"])
vocab = {token:integer for integer,token in enumerate(all_token)}

class SimpleTokenizerV2:
  def __init__(self, vocab):
    self.str_to_int = vocab
    self.int_to_str = {i:s for s,i in vocab.items()}

  def encode(self,text):
    preprocessed = re.split(r'([,.?_!"()\']|--|\s)',text)
    preprocessed = [item.strip() for item in preprocessed if item.strip()]
    preprocessed = [item if item in self.str_to_int
             else "<|unk|>" for item in preprocessed] # Changed proprocessed to preprocessed

    ids = [self.str_to_int[s] for s in preprocessed] # Changed processed to preprocessed
    return ids

  def decode(self,ids):
    text = " ".join([self.int_to_str[i] for i in ids])

    text = re.sub(r'\s+([,.?!"()\'])',r'\1',text)
    return text
    
text1 = "hello,do you like tea?"
text2 = "in the sunlit teerraces of the palace."
text = "<|endoftext|>".join([text1,text2])
tokenizer = SimpleTokenizerV2(vocab)
print(tokenizer.encode(text))
