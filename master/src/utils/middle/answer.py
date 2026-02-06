from asyncio import CancelledError
import wrapt
from typing import Awaitable
from json import dumps
from datetime import datetime
from utils.suger import logs



class Rsp(CancelledError):
    """
    1**	信息,服务器收到请求,需要请求者继续执行操作
    2**	成功,操作被成功接收并处理
    3**	重定向,需要进一步的操作以完成请求
    4**	客户端错误,请求包含语法错误或无法完成请求
    5**	服务器错误,服务器在处理请求的过程中发生了错误
    """
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def to_json_string(self)->str:
        head, *args = self.args
        if head == 'dict':
            return  dumps(self.kwargs)
        elif head == 'json':
            return args[0]
        
    @classmethod
    def from_raw_json(cls,json:str):
        this = cls("json",json)
        raise this

    @classmethod
    def next(cls,msg='',data=None):
        '继续。客户端应继续其请求。'
        result = {"code": 100, "message": "继续。", "data": data}
        if msg:
            result["message"] = msg
        this = cls("dict",**result)
        raise this

    @classmethod
    def exchange(cls,msg='',data=None):
        '切换协议。服务器根据客户端的请求切换协议。只能切换到更高级的协议,例如,切换到HTTP的新版本协议。'
        result = {"code": 101, "message": "切换协议。", "data": data}
        if msg:
            result["message"] = msg
        this = cls('dict',**result)
        raise this
    
    @classmethod
    def customize(cls,code,message,data):
        '自定义返回'
        result = {"code": code, "message": message, "data": data}
        this = cls('dict',**result)
        raise this
    
    @classmethod
    def ok(cls,data=None,msg=""):
        '请求成功,正常返回。'
        result = {"code": 200,"message": msg,"data":data}
        this = cls('dict',**result)
        raise this

    @classmethod
    def login_fail(cls,msg='',data=None):
        '登录失败'
        result = {"code": 203, "message": "密码或账号错误", "data": data}
        if msg:
            result["message"] = msg
        this = cls('dict',**result)
        
        raise this

    @classmethod
    def no_content(cls,msg='',data=None):
        '无内容。服务器成功处理,但未返回内容。在未更新网页的情况下,可确保浏览器继续显示当前文档'
        result = {"code": 204, "message": "无内容。服务器成功处理,但未返回内容。", "data": data}
        if msg:
            result["message"] = msg
        this = cls('dict',**result)
        raise this
    
    @classmethod
    def no_method(cls,msg="",data=None):
        '不存在方法！'
        result = {"code": 331,"message": "Method does not exist !","data":data}
        if msg:
            result["message"] = msg
        this = cls('dict',**result)
        raise this
    
    @classmethod
    def auth_fail(cls,msg='',data=None):
        '认证失败'
        result = {"code": 332,  "message": "请输入 Headers Authorization: {token}", "data": data}
        if msg:
            result["message"] = msg
        this = cls('dict',**result)
        raise this

    @classmethod
    def sign_fail(cls,msg='',data=None):
        '验签失效'
        result = {"code": 333, "message": "验签失效, 请重新登录!", "data": data}
        if msg:
            result["message"] = msg
        this = cls('dict',**result)
        raise this
    
    @classmethod
    def invalid_token(cls,msg='',data=None):
        '无效Token'
        result = {"code": 334, "message": "无效Token,请验证Token!", "data": data}
        if msg:
            result["message"] = msg
        this = cls('dict',**result)
        raise this

    @classmethod
    def no_power(cls,msg='',data=None):
        '没有权限'
        result = {"code": 335, "message": "没有权限!", "data": data}
        if msg:
            result["message"] = msg
        this = cls('dict',**result)
        raise this

    @classmethod
    def repeat(cls,msg='',data=None):
        '数据重复'
        result = {"code": 336, "message": "数据已存在!", "data": data}
        if msg:
            result["message"] = msg
        this = cls('dict',**result)
        raise this
    
    @classmethod
    def keynull(cls,msg='',data=None):
        '缺少字段'
        result = {"code": 337, "message": "缺少字段和值!", "data": data}
        if msg:
            result["message"] = msg
        this = cls('dict',**result)
        raise this

    @classmethod
    def operate(cls,msg='',data=None):
        '操作不成功'
        result = {"code": 338, "message": "操作失败!", "data": data}
        if msg:
            result["message"] = msg
        this = cls('dict',**result)
        raise this

    @classmethod
    def weixin(cls,msg="",data=None):
        '微信错误'
        result = {"code": 350, "message": "微信认证错误!", "data": data}
        if msg:
            result["message"] = msg
        this = cls('dict',**result)
        raise this
    
    @classmethod
    def not_found(cls,msg="",data=None):
        '找不到端口'
        result = {"code": 404, "message": "Api url not found!", "data": data}
        if msg:
            result["message"] = msg
        this = cls('dict',**result)
        raise this
    
    @classmethod
    def rpc(cls,msg='',data=None):
        'rpc服务端错误'
        result = {"code": 502, "message": "RPCServer错误", "data": data}
        if msg:
            result["message"] = msg
        this = cls('dict',**result)
        raise this

    
    @classmethod
    @wrapt.decorator
    async def response(wrapped, instance, args, kwargs):
        try:
            future = wrapped(*args, **kwargs)
            if isinstance(future, Awaitable):
                await future
        except Rsp as s:
            return s.to_json_string()
        except CancelledError:
            return dict(code=499, message='RPClient Closed Request', data=datetime.now())
        except Exception as e:
            logs.error(e,wrapped)
            return dict(code=502, message="Robyn 错误", data=datetime.now())
        else:
            return dict(code=204, message="无内容", data=None)