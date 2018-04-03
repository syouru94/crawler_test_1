import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# 專案中下載的私密金鑰，必須改成你自己的




# 產生授權物件
cred = credentials.Certificate("/Users/Lewis/Desktop/vscode/.vscode/project/serviceAccount.json")

# 如果firebase_admin 是 None 就初始化，僅會初始化一次

try:
  firebase_admin.delete_app(firebase_admin.get_app())
except:
  print('尚未初始化過 firebase_admin')
else:
  print('初始化 firebase_admin')
firebase_admin.initialize_app(cred)

# 初始化 資料庫物件
db = firestore.client()

def save_data(collection_name, doc_name, data_set):
  
  # 回傳 firebase 儲存後的訊息
  return db.collection(collection_name).document(doc_name).set(data_set)

def select(date, ccy, type):
  
  # 建立 doc 的參考
  doc_ref = db.collection('exchange_rates').document(date)
  
  try:
    
    # 試著讀取數據
    doc = doc_ref.get()
    
    # 將數據轉換為字典
    data = doc.to_dict()
    
    # 回傳抓到結果
    return data[ccy][type]
  
  # 出現例外狀況呢？
  except:
    
    # 列印出提示訊息
    print('有東西出錯囉')
