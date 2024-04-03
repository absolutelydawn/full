const express = require('express')
const app = express.Router()
const mongoose = require('mongoose')
const async = require('async')

// define schema
var userSchema = mongoose.Schema({
    userid: String,
    name: String,
    city: String,
    sex: String,
    age: Number
},{
    versionKey:false
})

// create model with moongodb collection and schema
var User = mongoose.model('users', userSchema);

app.get("/Hello", function(req, res){
    res.send("Hello World~!!")
})

// list
app.get('/list', function(req, res, next){
    User.find({}, function(err, docs){
        if (err) console.log('err')
        res.send(docs)
    }).projection({ _id: 0 })
})

// get
app.get('/get', function(req, res, next){
    var userid = req.query.input
    User.findOne({ 'userid': userid }, function(err, docs){
        if (err) console.log('err')
        res.send(docs)
    }).projection({ _id: 0 })
})

// insert
app.post('/insert', function(req, res, next){
    var { userid, name, city, sex, age } = req.body
    var user = new User({'userid':userid, 'name':name, 'city':city, 'sex':sex, 'age':age })
    user.save(function(err, slience){
        if (err) {
            console.log('err')
            res.status(500).send('Insert Error')
            return;
        }
    res.status(200).send('Inserted~!!')
    })
})

// update
app.post('/update', function(req, res, next){
    var { userid, name, city, sex, age } = req.body
    User.findOne({'userid':userid}, function(err, user){
        if (err) {
            console.log('err')
            res.status(500).send('Update Error')
        }
        user.name = name
        user.city = city
        user.sex = sex        
        user.age = age

    user.save(function(err, slience){
        if (err) {
            console.log('err')
            res.status(500).send('Update Error')
            return;
        }
    res.status(200).send('Updateted~!!')
    })
})
})

//delete
app.post('/delete', function(req, res, next){
    var userid = req.body.userid
    var user = User.find({'userid':userid})

    // user.remove(function(err){
    //     if (err) {
    //         console.log('err')
    //         res.status(500).send('Delete Error')
    //         return
    //     }
    //     res.status(200).send('Deleted~!!')
    // })
    user.deleteMany({ 'userid':userid }).then(function() {
        res.status(200).send('Deleted~!!')
    }).catch(function(error){
        console.log(error)
    })
})

module.exports = app;

async.series([query1, query2, query3, query4, query5, query6], function (err, result) {
    if (err) {
        console.log('Error' + err)
    } else {
        console.log('Task finish~!!')
    }
})

function query1(callback) {
    // select * from users
    User.find({}, { '_id': 0 })
        .exec(function (err, user) {
            console.log('\nQuery 1')
            console.log(user + "\n")
            callback(null)
        })
}

function query2(callback) {
    // select userid, name, city from users
    User.find({}, { '_id': 0, 'userid': 1, 'name': 1, 'city': 1 })
        .exec(function (err, user) {
            console.log('\nQuery 2')
            console.log(user + "\n")
            callback(null)
        })
}

function query3(callback) {
    // select * from users where city="Seoul" order by userid limit 3
    User.find({ 'city': 'Seoul' }, { '_id': 0 }).sort({ 'userid': 1 })
        .limit(3).exec(function (err, user) {
            console.log('\nQuery 3')
            console.log(user + "\n")
            callback(null)
        })
}

function query4(callback) {
    // select userid, name from users where userid="/02/"
    User.find({ 'userid': { '$regex': '02' } }, { '_id': 0 })
        .select('userid name').exec(function (err, user) {
            console.log('\nQuery 4')
            console.log(user + "\n")
            callback(null)
        })
}

function query5(callback) {
    // using JSON doc query
    // select userid, name, age from users where city="seoul" and age > 15 and age < 23
    User.find({ 'city': 'Seoul', 'age': { $gt: 14, $lt: 23 } }, { '_id': 0 })
        .sort({ 'age': -1 })
        .select('userid name age')
        .exec(function (err, user) {
            console.log('\nQuery 5')
            console.log(user + "\n")
            callback(null)
        })
}

function query6(callback) {
    // using querybuilder
    // select userid, name, age from users city="seoul" and age > 15 and age < 30 order by age 
    User.find({}, { '_id': 0 })
        .where('city').equals('Seoul')
        .where('age').gt(15).lt(30)
        .sort({ 'age': 1 })
        .select('userid name age')
        .exec(function (err, user) {
            console.log('\nQuery 6')
            console.log(user + "\n")
            callback(null)
        })
}
