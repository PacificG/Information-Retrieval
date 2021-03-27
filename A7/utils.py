
def perf_measure(y_actual, y_hat):
  """
  calculates TP, FP, TN, FN for actual and predicted y
  """
  TP = 0
  FP = 0
  TN = 0
  FN = 0

  for i in range(len(y_hat)): 
      if y_actual[i]==y_hat[i]==1:
          TP += 1
      if y_hat[i]==1 and y_actual[i]!=y_hat[i]:
          FP += 1
      if y_actual[i]==y_hat[i]==0:
          TN += 1
      if y_hat[i]==0 and y_actual[i]!=y_hat[i]:
          FN += 1

  return(TP, FP, TN, FN)

def micro_precision(dic):
  """
  returns micro_precision for multilabel classification
  """
  num, denom = 0, 0
  for col in dic:
    num += dic[col][0]
    denom += dic[col][0] + dic[col][1]
  return num/denom

def micro_recall(dic):
  """
  returns micro_recall for multilabel classification
  """
  num, denom = 0, 0
  for col in dic:
    num += dic[col][0]
    denom += dic[col][0] + dic[col][3]
  return num/denom

def micro_f1(micro_p, micro_rec):
  """
  returns micro_f1 for multilabel classification
  """
  return 2*(micro_p*micro_rec)/(micro_p + micro_rec)

def macro_precision(dic):
  """
  returns macro_precision for multilabel classification
  """
  prec = 0
  for col in dic:
    precision = dic[col][0]/ (dic[col][0] + dic[col][1])
    prec += precision
  return prec/len(list(dic.items()))

def macro_recall(dic):
  """
  returns macro_recall for multilabel classification
  """
  recall = 0
  for col in dic:
    recall += dic[col][0] / (dic[col][0] + dic[col][3])
  return recall/len(list(dic.items()))

def macro_f1(macro_p, macro_rec):
  """
  returns macro_f1 for multilabel classification
  """
  return 2*(macro_p*macro_rec)/(macro_p+macro_rec)

def count():
  i = 0
  while True:
    yield i
    i += 1