use('slave');

db.createCollection('user');
db.user.drop();

db.getCollection('user').insertOne({
    'role': 'admin', 'email': '77254@qq.com', 'pass_word': '123456'
});
db.getCollection('user').insertOne({
    'role': 'views', 'email': '3818@qq.com', 'pass_word': '123456'
});

