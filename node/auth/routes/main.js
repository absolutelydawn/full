const express = require('express')
const bodyParser = require('body-parser')
const mysql = require('sync-mysql')
const env = require('dotenv').config({ path: "../../.env" });

const app = express()

app.use(bodyParser.json())
app.use(bodyParser.urlencoded({ extended: false }))
app.use(express.json())
app.use(express.urlencoded({ extended: true }))

var connection = new mysql({
    host: process.env.host,
    user: process.env.user,
    port: process.env.port,
    password: process.env.password,
    database: process.env.database
});

app.get('/Hello', (req,res) => {
    res.send("Hello World")
}) ;

app.get('/select', (req, res) => {
    const result = connection.query("select * from user");
    console.log(result);
    res.send(result);
}) ;

app.get('/selectQuery', (req, res) => {
    const id = req.query.id
    const result = connection.query("select * from user where userid=?", [id]);
    console.log(result);
    res.send(result);
}) ;

app.post('/selectQuery', (req, res) => {
    const id = req.body.id
    const result = connection.query("select * from user where userid=?", [id]);
    console.log(result);
    res.send(result);
}) ;

app.post('/insert', (req, res) => {
    const { id, pw } = req.body;
    const result = connection.query('insert into user values(?, ?)', [id, pw]);
    console.log(result);
    res.redirect('/selectQuery?id=' + req.body.id);
}) ;

app.post('/update', (req, res) => {
    const { id, pw } = req.body;
    const result = connection.query('update user set passwd=? where userid=?', [pw, id]);
    console.log(result);
    res.redirect('/selectQuery?id=' + req.body.id);
}) ;

app.post('/delete', (req, res) => {
    const id = req.body.id;
    const result = connection.query('delete from user where userid=?', [id]);
    console.log(result);
    res.redirect('/select');
}) ;

// login api 제작 
// index.html에서 로그인 성공하면 old_index.html
// 실패시 alert 로그인 실패 메세지
// app.get('/login', (req, res) => {
//     // if문으로 성공 - 실패 분기나누기
//     const { id, pw } = req.query; // id 와 pw가 모두 필요, id && pw 모두 일치
//     if (id=="root" && pw==1234){ // id pw 검색하는 문법 모루겟숨
//         res.redirect('/old_index.html');
//         console.log("Login success");
//         res.send(result);
//     }else {
//         res.redirect('/error.html');
//     }
// }) ;

// login
app.post('/login', (req,res)=>{
    const { id, pw } = req.body;
    const result = connection.query("select * from user where userid=? and passwd=?", [id, pw]);
    if (result.length == 0){
        res.redirect('error.html')
    }
    if (id == 'admin' || id == 'root') {
        console.log(id + " => Administrator Logined")
        res.redirect('member.html')
    } else {
        console.log(id + "=> User Logined")
        res.redirect('main.html')
    }
})

// register
app.post('/register', (req, res) =>{
    const{ id, pw } = req.body;
    const result = connection.query("insert into user values (?,?)", [id,pw]);
    console.log(result);
    res.redirect('/'); 
})

module.exports = app;
