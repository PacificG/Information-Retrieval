
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from gensim.test.utils import datapath
from gensim import utils
from gensim.parsing.preprocessing import preprocess_string, preprocess_documents

class document:
  """
  custom class to represent comments
  """
  def __init__(self, id, text, *ls):
    """
    initialization of comments
    """
    self.id = id
    self.text = text
    r = iter(range(6))
    self.level = {threat:ls[next(r)] for threat in ['toxic', 'severe_toxic', 'obscene', 'threat', 
                                  'insult', 'identity_hate']}
  
  def read(self):
    """
    returns comment's text
    """
    return self.text

class vectorize:
  """
  custom class for tfidf and word2vec
  """
  def __init__(self, documents, testdocs):
    self.documents = documents
    self.testdocs = testdocs

  def iter(self):
    
    from gensim.parsing.preprocessing import preprocess_string, preprocess_documents
    for doc in self.documents:
      yield doc.read()
    for testd in self.testdocs:
      yield testd.read()


  def tfidfvec(self):
    """
    tfidf representation for training and testing comments
    """
    from sklearn.feature_extraction.text import TfidfVectorizer
    itr = self.iter()
    termdocMat = TfidfVectorizer(self.documents, token_pattern='[a-zA-Z]+', stop_words={'english'}).fit_transform(itr)
    self.tfidfdoc = termdocMat[:len(self.documents), :]
    c= count()
    self.tfidftestdoc = termdocMat[len(self.documents):,:]
    del termdocMat

  def word2vec(self, sentences):
    """
    word2vec representation for training and testing comments
    """
    from gensim.test.utils import datapath
    from gensim import utils
    from gensim.parsing.preprocessing import preprocess_string, preprocess_documents 

    import gensim.models

    skipmodel = gensim.models.Word2Vec(sentences=sentences, sg=1, min_count = 1, size=300, window=5, workers=2)

    
    docs = {file.id:file.read().lower().split() for file in self.documents}

    queries = {file.id:file.read().lower().split() for file in self.testdocs}

    for i in range(len(self.documents)):
      self.documents[i].w2vec = sum([skipmodel.wv[word] for word in docs[self.documents[i].id] if  word in skipmodel.wv])
    
    for i in range(len(self.testdocs)):
      self.testdocs[i].w2vec = sum([skipmodel.wv[word] for word in queries[self.testdocs[i].id] if word in skipmodel.wv])

      
from gensim.parsing.preprocessing import preprocess_string, preprocess_documents 
class MyCorpus:
      """An iterator that yields sentences (lists of str)."""

      def __iter__(self):
        for file in vec.documents:
          yield file.read().lower().split()
        for file in vec.testdocs:
          yield file.read().lower().split()      
