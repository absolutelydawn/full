const express = require('express')
const bodyParser = require('body-parser')
const pool = require("../../conf/pool" );

const app = express()

app.use(bodyParser.json())
app.use(bodyParser.urlencoded({ extended: false }))
app.use(express.json())
app.use(express.urlencoded({ extended: true }))

app.get('/Hello', (req,res) => {
    res.send("Hello World")
})

// select all rows from st_info table
app.get('/select', async(req, res) => {
    const [rows, fields] = await pool.query("select * from st_info")
    console.log(rows);
    // res.send(result);
    res.writeHead(200);
    var template = `
    <!Doctype html>
    <html>
        <head>
            <meta charset="utf-8">
            <title>Result</title>
        </head>
        <body>
            <table border="1" margin:auto; text-align:center;>
            <tr>
                <th>ST_ID</th>
                <th>NAME</th>
                <th>DEPT</th>
            </tr>
            `;
    for (var i = 0; i < rows.length; i++) {
        template += `
            <tr>
                <th>${rows[i]['ST_ID']}</th>
                <th>${rows[i]['NAME']}</th>
                <th>${rows[i]['DEPT']}</th>
            </tr>
            `
    }
    template += `
            </table>
        </body>
    </html>
    `;
    res.end(template);
})

// insert data into st_info table
app.get('/insert', async(req, res) => {
    const { ST_ID, NAME, DEPT } = req.query
    const [rows, fields] = await pool.query(
        "insert into st_info values (?, ?, ?)", [ST_ID, NAME, DEPT]
    )
    res.redirect('/select');
})

// update row into st_info table
app.get('/update', async(req, res) => {
    const { ST_ID, NAME, DEPT } = req.query
    const [rows, fields] = await pool.query(
        "update st_info set NAME=?, DEPT=? where ST_ID=?", [NAME, DEPT, ST_ID]
    )
    res.redirect('/select');
})


// delete row from st_info table
app.get('/delete', async(req, res) => {
    const ST_ID = req.query.ST_ID
    const [rows, fields] = await pool.query(
        "delete from st_info where ST_ID=?", [ST_ID]
    )
    res.redirect('/select');
})

module.exports = app;