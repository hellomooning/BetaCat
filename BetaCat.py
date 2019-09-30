import tushare as ts
import Movie.movie

print(ts.__version__)
ts.set_token('711951da99614027f5fbbfcfd64a2af751e903a519d12ebdb58422ef')
# pro = ts.pro_api()
# data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
print(Movie.movie.test())
