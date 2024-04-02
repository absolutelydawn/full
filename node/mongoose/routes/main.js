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
