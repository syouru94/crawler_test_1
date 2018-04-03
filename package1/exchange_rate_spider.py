from pyquery import PyQuery as pq

def crawler(url, selector):

  # 抓取台銀的匯率頁面，存入html物件
  html = pq(url) 
  html_elements = html(selector)
  return html_elements

def clean_up(html_elements):
  
  # 將傳入的html_elements轉為文字
  html_elements_text = html_elements.text()
  
  # 建立幣別清單
  currency_list = ["USD", "HKD", "GBP", "AUD", "CAD", "SGD", "CHF", "JPY", "ZAR", "SEK", "NZD", "THB", "PHP", "IDR", "EUR", "KRW", "VND", "MYR", "CNY"]
  
  # 分割轉好的文字，產生匯率的清單
  rates_list = html_elements_text.split(' ')
  
  # 建立空的字典檔，當成資料集
  data_set = {}
  
  # 對於每一個在 幣別清單中的 index
  for index in range(len(currency_list)):
    
    # 取得 幣別的名稱
    currency_name = currency_list[index]
    
    # 根據幣別清單的index 計算 匯率清單的位置 並將相關數據存在變數中備用
    cash_buy   = rates_list[index * 4]
    cash_sell  = rates_list[index * 4 + 1]
    sight_buy  = rates_list[index * 4 + 2]
    sight_sell = rates_list[index * 4 + 3]
    
    # 在字典中，新增一個 key， 內容為 另一個字典 負責放四種匯率值
    data_set[currency_name] = {
        'CASH_BUY': cash_buy,
        'CASH_SELL': cash_sell,
        'SIGHT_BUY': sight_buy,
        'SIGHT_SELL': sight_sell
    }

  # 回傳 建立好的資料集
  return data_set
