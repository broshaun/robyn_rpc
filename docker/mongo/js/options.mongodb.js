use('slave');


db.getCollection('options').drop();

// 1. 性别选项
db.getCollection('options').insertOne({
    label: '性别: ', organize: 'SEX',
    option: [{ value: 'boy', text: '男' }, { value: 'girl', text: '女' }]
});

// 2. 婚姻状态选项
db.getCollection('options').insertOne({
    label: '婚姻状态: ', organize: 'MARITAL',
    option: [{ value: 'married', text: '已婚' }, { value: 'unmarried', text: '未婚' }, { value: 'divorced', text: '离异' }]
});