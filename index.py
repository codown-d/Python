import akshare as ak
import aktools as at
import pandas as pd
stock_sse_summary = ak.stock_bid_ask_em(
    symbol="000001",  )
df = pd.DataFrame(stock_sse_summary)

# 将DataFrame写入Excel文件
df.to_excel('example_pandas.xlsx', index=False)