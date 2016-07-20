/**
 * Created by andrewsyc on 7/6/16.
 */
var webPage = require('webpage');
var page = webPage.create();

var system = require('system');
var args = system.args;

//console.log(args[1]);
url = String(args[1]);
page.open(url, function (status) {

    var content = page.content;
            //console.log(content);
            //console.log('Content: ' + content);
            console.log(content);
            phantom.exit();
        });






//if (args.length === 1) {
//    console.log('Try to pass some arguments when invoking this script!');
//} else {
//    //args.forEach(function (arg, i) {
//    //    console.log(i + ': ' + arg);
//    //    console.log(args[1]);
//    //    page.open(arg, function (status) {
//    //        var content = page.content;
//    //        console.log('Content: ' + content);
//    //        phantom.exit();
//    //    });
//    //
//    //    phantom.exit();
//    //});
//    //
//    page.open(args[1], function (status) {
//            var content = page.content;
//            console.log(content);
//            console.log('Content: ' + content);
//            phantom.exit();
//        });
//
//        phantom.exit();
//}


