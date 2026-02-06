use('slave');

db.createCollection('roles');
db.roles.drop();

db.getCollection('roles').insertMany([
  { 'role': 'views', permission: { "views": "观察者" } },
  { 'role': 'admin', permission: { "admin": "管理员", 'views': "观察者" } },
]);