/**
 * Created by andrewsyc on 7/6/16.
 */
var webPage = require('webpage');
var page = webPage.create();

page.open('http://phantomjs.org', function (status) {
  var content = page.content;
  //console.log('Content: ' + content);
    return content;
  phantom.exit();
});