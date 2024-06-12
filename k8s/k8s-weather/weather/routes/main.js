const express = require('express');
const app = express.Router();
const mongoose = require('mongoose');
const request = require('request');
const moment = require('moment');
const datautil = require('data-utils');
const mongoClient = require('mongodb').MongoClient;

let day = new Date().toLocaleDateString('sv').replaceAll('-', '');
day = day - 1;

var keys = 'hgZLcXYGW%2BV162eJNAgEpQfM4QeoW8Hqyjx1B%2FiUXuIORmyrq68teftqf9OBWASMCBSXMhQW7Yuk398mef1K3g%3D%3D';
var url = 'https://apis.data.go.kr/1360000/WthrChartInfoService/getAuxillaryChart';

var queryParams = '?' + encodeURIComponent('ServiceKey') + '=' + keys;
queryParams += '&' + encodeURIComponent('pageNo') + '=' + encodeURIComponent('1');
queryParams += '&' + encodeURIComponent('numOfRows') + '=' + encodeURIComponent('10');
queryParams += '&' + encodeURIComponent('dataType') + '=' + encodeURIComponent('JSON');
queryParams += '&' + encodeURIComponent('code1') + '=' + encodeURIComponent('N500');
queryParams += '&' + encodeURIComponent('code2') + '=' + encodeURIComponent('ANL');
queryParams += '&' + encodeURIComponent('time') + '=' + encodeURIComponent(day);

// define schema
var DataSchema = mongoose.Schema({
  dav_v: String,
  imgSrc1_v: String,
  imgSrc2_v: String,
});

// create model with mongodb collection and schema
var Data = mongoose.model('weathers', DataSchema);

app.get('/getdata', function (req, res, next) {
  request(
    {
      url: url + queryParams,
      method: 'GET',
    },
    function (error, response, body) {
      Data.find({}).remove().exec();
      if (error) console.log(error);
      let data = JSON.parse(body);
      console.log(data);
      let imgSrcArr = data.response.body.items.item[0]['n500-file'].split(',');
      let imgSrc1 = imgSrcArr[0].slice(1);
      let imgSrc2 = imgSrcArr[1].slice(1);
      console.log('imgSrc1 : ' + imgSrc1);
      console.log('imgSrc2 : ' + imgSrc2);

      res.writeHead(200);
      var template = `
        <!DOCTYPE html>
        <html>
        <head>
          <title>Weather</title>
          <meta charset="utf-8">
        </head>
        <body>
          <img src="${imgSrc1}" width="500" height="500"/>
          <img src="${imgSrc2}" width="500" height="500"/>
        </body>
        </html>
        `;
      res.end(template);

      var newData = new Data({ day_v: day, imgSrc1_v: imgSrc1, imgSrc2_v: imgSrc2 });
      newData.save(function (err, result) {
        if (err) return console.error(err);
        console.log(new Date(), result);
      });
    },
  );
});

// list
app.get('/list', function (req, res, next) {
  Data.findOne({}, function (err, docs) {
    if (err) console.log('err');
    console.log(docs);
    res.writeHead(200);
    var template = `
    <!doctype html>
    <html>
    <head>
      <title>Result</title>
      <meta charset="urf-8">
    </head>
    <body>
      <img src="${docs['imgSrc1_v']}" width="500" height="500"/>
      <img src="${docs['imgSrc2_v']}" width="500" height="500"/>
    </body>
    </html>
    `;
    res.end(template);
  }).projection({ _id: 0 });
});

module.exports = app;