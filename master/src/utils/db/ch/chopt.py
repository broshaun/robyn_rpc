import  clickhouse_connect


class CHBase:
    def __init__(self,host,port,username,password,database):
        self._client = clickhouse_connect.get_client(
            host= host,
            port = port,
            username = username,
            password = password,
            database = database
        )

    def __del__(self):
        """析构函数：自动关闭连接（防止资源泄露）"""
        if hasattr(self,"_client"):
            self._client.close()

    def bysql_for_polars(self,sql,**kwargs):
        return self._client.query_df_arrow(sql,dataframe_library='polars',parameters=kwargs)
    
