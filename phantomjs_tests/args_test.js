/**
 * Created by andrewsyc on 7/6/16.
 */
var system = require('system');
var args = system.args;

if (args.length === 1) {
  console.log('Try to pass some arguments when invoking this script!');
} else {
  args.forEach(function(arg, i) {
    console.log(i + ': ' + arg);
  });
}