(function(){function g(a){var b=0;return function(){return b<a.length?{done:!1,value:a[b++]}:{done:!0}}}
function k(a){var b="undefined"!=typeof Symbol&&Symbol.iterator&&a[Symbol.iterator];return b?b.call(a):{next:g(a)}}
function l(a){if(!(a instanceof Array)){a=k(a);for(var b,c=[];!(b=a.next()).done;)c.push(b.value);a=c}return a}
var n="function"==typeof Object.defineProperties?Object.defineProperty:function(a,b,c){a!=Array.prototype&&a!=Object.prototype&&(a[b]=c.value)},p="undefined"!=typeof window&&window===this?this:"undefined"!=typeof global&&null!=global?global:this;
function q(a,b){if(b){for(var c=p,e=a.split("."),d=0;d<e.length-1;d++){var f=e[d];f in c||(c[f]={});c=c[f]}e=e[e.length-1];d=c[e];f=b(d);f!=d&&null!=f&&n(c,e,{configurable:!0,writable:!0,value:f})}}
function r(a,b,c){if(null==a)throw new TypeError("The 'this' value for String.prototype."+c+" must not be null or undefined");if(b instanceof RegExp)throw new TypeError("First argument to String.prototype."+c+" must not be a regular expression");return a+""}
q("String.prototype.endsWith",function(a){return a?a:function(a,c){var b=r(this,a,"endsWith");a+="";void 0===c&&(c=b.length);for(var d=Math.max(0,Math.min(c|0,b.length)),f=a.length;0<f&&0<d;)if(b[--d]!=a[--f])return!1;return 0>=f}});
q("String.prototype.startsWith",function(a){return a?a:function(a,c){var b=r(this,a,"startsWith");a+="";for(var d=b.length,f=a.length,m=Math.max(0,Math.min(c|0,b.length)),h=0;h<f&&m<d;)if(b[m++]!=a[h++])return!1;return h>=f}});
function t(){t=function(){};
p.Symbol||(p.Symbol=u)}
var u=function(){var a=0;return function(b){return"jscomp_symbol_"+(b||"")+a++}}();
function v(){t();var a=p.Symbol.iterator;a||(a=p.Symbol.iterator=p.Symbol("iterator"));"function"!=typeof Array.prototype[a]&&n(Array.prototype,a,{configurable:!0,writable:!0,value:function(){return w(g(this))}});
v=function(){}}
function w(a){v();a={next:a};a[p.Symbol.iterator]=function(){return this};
return a}
function x(a,b){return Object.prototype.hasOwnProperty.call(a,b)}
q("WeakMap",function(a){function b(a){this.a=(m+=Math.random()+1).toString();if(a){a=k(a);for(var b;!(b=a.next()).done;)b=b.value,this.set(b[0],b[1])}}
function c(){}
function e(a){x(a,f)||n(a,f,{value:new c})}
function d(a){var b=Object[a];b&&(Object[a]=function(a){if(a instanceof c)return a;e(a);return b(a)})}
if(function(){if(!a||!Object.seal)return!1;try{var b=Object.seal({}),c=Object.seal({}),d=new a([[b,2],[c,3]]);if(2!=d.get(b)||3!=d.get(c))return!1;d["delete"](b);d.set(c,4);return!d.has(b)&&4==d.get(c)}catch(U){return!1}}())return a;
var f="$jscomp_hidden_"+Math.random();d("freeze");d("preventExtensions");d("seal");var m=0;b.prototype.set=function(a,b){e(a);if(!x(a,f))throw Error("WeakMap key fail: "+a);a[f][this.a]=b;return this};
b.prototype.get=function(a){return x(a,f)?a[f][this.a]:void 0};
b.prototype.has=function(a){return x(a,f)&&x(a[f],this.a)};
b.prototype["delete"]=function(a){return x(a,f)&&x(a[f],this.a)?delete a[f][this.a]:!1};
return b});
q("Map",function(a){function b(){var a={};return a.previous=a.next=a.head=a}
function c(a,b){var c=a.a;return w(function(){if(c){for(;c.head!=a.a;)c=c.previous;for(;c.next!=c.head;)return c=c.next,{done:!1,value:b(c)};c=null}return{done:!0,value:void 0}})}
function e(a,b){var c=b&&typeof b;"object"==c||"function"==c?f.has(b)?c=f.get(b):(c=""+ ++m,f.set(b,c)):c="p_"+b;var d=a.c[c];if(d&&x(a.c,c))for(var e=0;e<d.length;e++){var h=d[e];if(b!==b&&h.key!==h.key||b===h.key)return{id:c,list:d,index:e,b:h}}return{id:c,list:d,index:-1,b:void 0}}
function d(a){this.c={};this.a=b();this.size=0;if(a){a=k(a);for(var c;!(c=a.next()).done;)c=c.value,this.set(c[0],c[1])}}
if(function(){if(!a||"function"!=typeof a||!a.prototype.entries||"function"!=typeof Object.seal)return!1;try{var b=Object.seal({x:4}),c=new a(k([[b,"s"]]));if("s"!=c.get(b)||1!=c.size||c.get({x:4})||c.set({x:4},"t")!=c||2!=c.size)return!1;var d=c.entries(),e=d.next();if(e.done||e.value[0]!=b||"s"!=e.value[1])return!1;e=d.next();return e.done||4!=e.value[0].x||"t"!=e.value[1]||!d.next().done?!1:!0}catch(V){return!1}}())return a;
v();var f=new WeakMap;d.prototype.set=function(a,b){a=0===a?0:a;var c=e(this,a);c.list||(c.list=this.c[c.id]=[]);c.b?c.b.value=b:(c.b={next:this.a,previous:this.a.previous,head:this.a,key:a,value:b},c.list.push(c.b),this.a.previous.next=c.b,this.a.previous=c.b,this.size++);return this};
d.prototype["delete"]=function(a){a=e(this,a);return a.b&&a.list?(a.list.splice(a.index,1),a.list.length||delete this.c[a.id],a.b.previous.next=a.b.next,a.b.next.previous=a.b.previous,a.b.head=null,this.size--,!0):!1};
d.prototype.clear=function(){this.c={};this.a=this.a.previous=b();this.size=0};
d.prototype.has=function(a){return!!e(this,a).b};
d.prototype.get=function(a){return(a=e(this,a).b)&&a.value};
d.prototype.entries=function(){return c(this,function(a){return[a.key,a.value]})};
d.prototype.keys=function(){return c(this,function(a){return a.key})};
d.prototype.values=function(){return c(this,function(a){return a.value})};
d.prototype.forEach=function(a,c){for(var b=this.entries(),d;!(d=b.next()).done;)d=d.value,a.call(c,d[1],d[0],this)};
d.prototype[Symbol.iterator]=d.prototype.entries;var m=0;return d});
q("Set",function(a){function b(a){this.a=new Map;if(a){a=k(a);for(var b;!(b=a.next()).done;)this.add(b.value)}this.size=this.a.size}
if(function(){if(!a||"function"!=typeof a||!a.prototype.entries||"function"!=typeof Object.seal)return!1;try{var b=Object.seal({x:4}),e=new a(k([b]));if(!e.has(b)||1!=e.size||e.add(b)!=e||1!=e.size||e.add({x:4})!=e||2!=e.size)return!1;var d=e.entries(),f=d.next();if(f.done||f.value[0]!=b||f.value[1]!=b)return!1;f=d.next();return f.done||f.value[0]==b||4!=f.value[0].x||f.value[1]!=f.value[0]?!1:d.next().done}catch(m){return!1}}())return a;
v();b.prototype.add=function(a){a=0===a?0:a;this.a.set(a,a);this.size=this.a.size;return this};
b.prototype["delete"]=function(a){a=this.a["delete"](a);this.size=this.a.size;return a};
b.prototype.clear=function(){this.a.clear();this.size=0};
b.prototype.has=function(a){return this.a.has(a)};
b.prototype.entries=function(){return this.a.entries()};
b.prototype.values=function(){return this.a.values()};
b.prototype.keys=b.prototype.values;b.prototype[Symbol.iterator]=b.prototype.values;b.prototype.forEach=function(a,b){var c=this;this.a.forEach(function(d){return a.call(b,d,d,c)})};
return b});
var y=this;function z(a,b){var c=a.split("."),e=y;c[0]in e||"undefined"==typeof e.execScript||e.execScript("var "+c[0]);for(var d;c.length&&(d=c.shift());)c.length||void 0===b?e[d]&&e[d]!==Object.prototype[d]?e=e[d]:e=e[d]={}:e[d]=b}
;var A=/^(?:([^:/?#.]+):)?(?:\/\/(?:([^/?#]*)@)?([^/#?]*?)(?::([0-9]+))?(?=[/#?]|$))?([^?#]+)?(?:\?([^#]*))?(?:#([\s\S]*))?$/;function B(a){return a?decodeURI(a):a}
;var C=window.yt&&window.yt.config_||window.ytcfg&&window.ytcfg.data_||{};z("yt.config_",C);function D(){var a=[];return"CSS_CLASS_WHITELIST"in C?C.CSS_CLASS_WHITELIST:a}
;var E=Object.freeze(["js-httpswwwgoogleanalyticscomanalyticsjs","js-chromeextensionpkedcjkdefgpdelpbcmbmeomcjbeemfm","video-","js-http","css-http"]),F=Object.freeze("document.appendChild document.body.appendChild document.querySelector document.querySelectorAll history.back history.go".split(" ")),G=Object.freeze("fonts.googleapis.com s0.2mdn.net securepubads.g.doubleclick.net ssl.google-analytics.com static.doubleclick.net www.google-analytics.com www.googletagservices.com www.youtube.com youtube.com".split(" ")),
H=Object.freeze(["pkedcjkdefgpdelpbcmbmeomcjbeemfm","fjhoaacokmgbjemoflkofnenfaiekifl","enhhojjnijigcajfphajepfemndkmdlo"]),I=Object.freeze(".corp.google.com .googlevideo.com .ytimg.com .google.com .googlesyndication.com .gstatic.com .prod.google.com .google.ru".split(" ")),J=Object.freeze(["chrome-extension","safari-extension","safari-resource","opera"]);function K(){return F.map(function(a){return L(a)}).filter(function(a){return!!a})}
function L(a){var b=a.split(".");a=b[b.length-1];b=b.reduce(function(a,b){return a&&a[b]},window);
if(!b)return a+" is missing";b=Function.prototype.toString.call(b).replace(/\n/g," ").replace(/  +/g," ");return b!="function "+a+"() { [native code] }"?a+" is not native, prologue: "+b.slice(0,50):null}
function M(a){var b=a.match(A)[1]||null;return J.some(function(a){return b==a})}
function N(a){var b=B(a.match(A)[3]||null);return!b||M(a)?!0:G.some(function(a){return b==a})||I.some(function(a){return b.endsWith(a)})}
function O(a){if(!M(a))return null;var b=B(a.match(A)[3]||null);return b?H.some(function(a){return b==a})?null:b:null}
function P(){var a=new Set;[].concat(l(document.querySelectorAll("script"))).forEach(function(b){b.src&&!N(b.src)&&a.add(b.src)});
[].concat(l(document.querySelectorAll("link[href]"))).forEach(function(b){"alternate"==b.rel||N(b.href)||a.add(b.href)});
return[].concat(l(a)).sort()}
function Q(){var a=new Set;[].concat(l(document.querySelectorAll("script"))).forEach(function(b){b.src&&(b=O(b.src))&&a.add(b)});
return[].concat(l(a)).sort()}
function R(){var a=new Set;[].concat(l(window.document.querySelectorAll("*"))).forEach(function(b){[].concat(l(b.classList)).forEach(function(b){S()||a.add(b)})});
return a}
function S(){return E.some(function(){})}
function T(){var a=new Set(D());if(!a.size)return[];var b=new Set;R().forEach(function(c){a.has(c)||S()||b.add(c)});
var c=[].concat(l(b)).sort();c=c.slice(0,15);var e=b.size-15;0<e&&c.push("...and "+e+" more.");return c}
;z("ytbin.polymer.shared.lib.tampering.info",function(){var a=T(),b=P(),c=K(),e=Q(),d=[];e.length&&d.push("extensions",e);a.length&&d.push("suspiciousClasses",a);b.length&&d.push("suspiciousIncludes",b);c.length&&d.push("suspiciousApis",c);return d.length?d:null});}).call(this);
