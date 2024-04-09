const express = require("express");
const bodyParser = require("body-parser");
const mysql = require("sync-mysql");
const env = require("dotenv").config({ path: "../../.env" });

var connection = new mysql({
  host: process.env.host,
  user: process.env.user,
  password: process.env.password,
  database: process.env.database,
});

const app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

function template_nodata() {
  res.writeHead(200);
  var template = `
    <!DOCTYPE html>
    <head>
        <title>Error</title>
        <meta charset="UTF-8">
        <link type="text/css" rel="stylesheet" href="mystyle.css" />
        </head>
        <body>
            <h3>데이터가 존재하지 않습니다.</h3>
        </body>
        </html>
    `;
  res.end(template);
}

function template_result(result, res) {
  res.writeHead(200);
  var template = `
    <!DOCTYPE html>
    <head>
        <title>Error</title>
        <meta charset="UTF-8">
        <link type="text/css" rel="stylesheet" href="mystyle.css" />
    </head>
    <body>
        <table border="1" style="margin:auto;">
        <thead>
            <tr><th>User ID</th><th>Password</th></tr>
        </thead>
        <tbody>
        `;
  for (var i = 0; i < result.length; i++) {
    template += `
            <tr>
                <td>${result[i]["userid"]}</td>
                <td>${result[i]["passwd"]}</td>
            </tr>
            `;
  }
  template += `
            </tbody>
            </table>
        </body>
        </html>
        `;
  res.end(template);
}

app.get("/hello", (req, res) => {
  res.send("Hello World~!!");
});

// login
app.post("/login", (req, res) => {
  const { id, pw } = req.body;
  const result = connection.query(
    "select * from user where userid=? and passwd=?",
    [id, pw]
  );
  if (result.length == 0) {
    res.redirect("error.html");
  }
  if (id == "admin" || id == "root") {
    console.log(id + " => Administrator Logined");
    res.redirect("member.html");
  } else {
    console.log(id + " => User Logined");
    res.redirect("main.html");
  }
});

// register
app.post("/register", (req, res) => {
  const { id, pw } = req.body;
  if (id == "") {
    res.redirect("register.html");
  } else {
    let result = connection.query("select * from user where userid=?", [id]);
    if (result.length > 0) {
      res.writeHead(200);
      var template = `
            <!DOCTYPE html>
            <head>
                <meta charset="UTF-8">
                <meta name="viewpoint content="width=device-width, initial-scale=1>
            </head>
            <body>
                <div>
                <h3 style="margin-left: 30px">Register Failed</h3>
                <h4 style="margin-left: 30px">이미 존재하는 id입니다.<h3>
                <a href="register.html" style="margin-left:30px">다시 시도하기</a>
                </div>
            </body>
            </html>
            `;
      res.end(template);
    } else {
      const result = connection.query("insert into user values(?,?)", [id, pw]);
      console.log(result);
      res.redirect("/");
    }
  }
});

// request O, query X
app.get("/select", (req, res) => {
  const result = connection.query("select * from user");
  console.log(result);
  //res.send(result);
  if (result.length == 0) {
    template_nodata(res);
  } else {
    template_result(result, res);
  }
});

// request O, query X
app.post("/select", (req, res) => {
  const result = connection.query("select * from user");
  console.log(result);
  res.send(result);
});

// request O, query O
app.get("/selectQuery", (req, res) => {
  const id = req.query.id;
  const result = connection.query("select * from user where userid=?", [id]);
  console.log(result);
  // res.send(result);
  if (result.length == 0) {
    template_nodata(res);
  } else {
    template_result(result, res);
  }
});

// request O, query O
app.post("/selectQuery", (req, res) => {
  const id = req.body.id;
  // console.log(req.body);
  const result = connection.query("select * from user where userid=?", [id]);
  console.log(result);
  // res.send(result);
  if (result.length == 0) {
    template_nodata(res);
  } else {
    template_result(result, res);
  }
});

// request O, query O
app.post("/insert", (req, res) => {
  const { id, pw } = req.body;
  const result = connection.query("insert into user values (?, ?)", [id, pw]);
  console.log(result);
  res.redirect("/selectQuery?id=" + req.body.id);
});

// request O, query O
app.post("/update", (req, res) => {
  const { id, pw } = req.body;
  const result = connection.query("update user set passwd=? where userid=?", [
    pw,
    id,
  ]);
  console.log(result);
  res.redirect("/selectQuery?id=" + req.body.id);
});

// request O, query O
app.post("/delete", (req, res) => {
  const id = req.body.id;
  const result = connection.query("delete from user where userid=?", [id]);
  console.log(result);
  res.redirect("/select");
});

module.exports = app;

// 내가 생각한거
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
