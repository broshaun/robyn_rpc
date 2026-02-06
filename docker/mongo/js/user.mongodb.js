use('slave');

db.createCollection('user');
db.user.drop();

db.getCollection('user').insertOne({
    'uid': 1, 'role': 'admin', 'email': '77254@qq.com', 'pass_word': '123456'
});
db.getCollection('user').insertOne({
    'uid': 2, 'role': 'views', 'email': '3818@qq.com', 'pass_word': '123456'
});

