(function(e){function t(t){for(var r,s,o=t[0],u=t[1],c=t[2],f=0,p=[];f<o.length;f++)s=o[f],Object.prototype.hasOwnProperty.call(a,s)&&a[s]&&p.push(a[s][0]),a[s]=0;for(r in u)Object.prototype.hasOwnProperty.call(u,r)&&(e[r]=u[r]);l&&l(t);while(p.length)p.shift()();return i.push.apply(i,c||[]),n()}function n(){for(var e,t=0;t<i.length;t++){for(var n=i[t],r=!0,o=1;o<n.length;o++){var u=n[o];0!==a[u]&&(r=!1)}r&&(i.splice(t--,1),e=s(s.s=n[0]))}return e}var r={},a={app:0},i=[];function s(t){if(r[t])return r[t].exports;var n=r[t]={i:t,l:!1,exports:{}};return e[t].call(n.exports,n,n.exports,s),n.l=!0,n.exports}s.m=e,s.c=r,s.d=function(e,t,n){s.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:n})},s.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},s.t=function(e,t){if(1&t&&(e=s(e)),8&t)return e;if(4&t&&"object"===typeof e&&e&&e.__esModule)return e;var n=Object.create(null);if(s.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var r in e)s.d(n,r,function(t){return e[t]}.bind(null,r));return n},s.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return s.d(t,"a",t),t},s.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},s.p="/";var o=window["webpackJsonp"]=window["webpackJsonp"]||[],u=o.push.bind(o);o.push=t,o=o.slice();for(var c=0;c<o.length;c++)t(o[c]);var l=u;i.push([0,"chunk-vendors"]),n()})({0:function(e,t,n){e.exports=n("56d7")},"034f":function(e,t,n){"use strict";n("85ec")},"56d7":function(e,t,n){"use strict";n.r(t);n("e260"),n("e6cf"),n("cca6"),n("a79d");var r=n("2b0e"),a=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{attrs:{id:"app"}},[e.news()?n("vs-card-group",e._l(e.newsList,(function(t){return n("Card",{directives:[{name:"show",rawName:"v-show",value:e.checkImage(t.image_url),expression:"checkImage(card.image_url)"}],key:t,attrs:{c:t}})})),1):e._e(),n("Table"),n("vs-button",{on:{click:function(t){return e.news()}}},[e._v("update")])],1)},i=[],s=n("1da1"),o=(n("96cf"),n("d3b7"),n("574d")),u=n.n(o),c=(n("04f2"),function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("vs-card",{on:{click:function(t){return e.url()}},scopedSlots:e._u([{key:"title",fn:function(){return[n("h3",{staticStyle:{"white-space":"nowrap",overflow:"hidden","text-overflow":"ellipsis"}},[e._v(e._s(e.c.title))])]},proxy:!0},{key:"img",fn:function(){return[n("img",{staticStyle:{"aspect-ratio":"16 / 9"},attrs:{src:e.c.image_url,alt:""}})]},proxy:!0},{key:"text",fn:function(){return[n("p",{staticStyle:{"white-space":"nowrap",overflow:"hidden","text-overflow":"ellipsis"}},[e._v(" "+e._s(e.c.description)+" ")])]},proxy:!0},{key:"interactions",fn:function(){return[n("vs-button",{attrs:{danger:"",icon:""}},[n("i",{staticClass:"bx bx-heart"})]),n("vs-button",{staticClass:"btn-chat",attrs:{shadow:"",primary:""}},[n("i",{staticClass:"bx bx-chat"}),n("span",{staticClass:"span"},[e._v(" 54 ")])])]},proxy:!0}])})}),l=[],f=(n("9911"),n("3f08"));r["default"].use(f["b"].Plugin),r["default"].use(f["a"]);var p={name:"Card",props:{card:String,c:Object},methods:{url:function(){window.open(this.c.link)}}},d=p,m=n("2877"),b=Object(m["a"])(d,c,l,!1,null,"6bb939ae",null),h=b.exports,v=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticClass:"center"},[n("vs-table",{scopedSlots:e._u([{key:"thead",fn:function(){return[n("vs-tr",[n("vs-th",[e._v(" Name ")]),n("vs-th",[e._v(" Email ")]),n("vs-th",[e._v(" Id ")])],1)]},proxy:!0},{key:"tbody",fn:function(){return e._l(e.$vs.getPage(e.users,e.page,e.max),(function(t,r){return n("vs-tr",{key:r,attrs:{data:t}},[n("vs-td",[e._v(" "+e._s(t.name)+" ")]),n("vs-td",[e._v(" "+e._s(t.email)+" ")]),n("vs-td",[e._v(" "+e._s(t.id)+" ")])],1)}))},proxy:!0},{key:"footer",fn:function(){return[n("vs-pagination",{attrs:{length:e.$vs.getLength(e.users,e.max)},model:{value:e.page,callback:function(t){e.page=t},expression:"page"}})]},proxy:!0}])})],1)},g=[],w={name:"Table",data:function(){return{page:1,max:3,users:[{id:1,name:"Leanne Graham",username:"Bret",email:"Sincere@april.biz",website:"hildegard.org"},{id:2,name:"Ervin Howell",username:"Antonette",email:"Shanna@melissa.tv",website:"anastasia.net"},{id:3,name:"Clementine Bauch",username:"Samantha",email:"Nathan@yesenia.net",website:"ramiro.info"},{id:4,name:"Patricia Lebsack",username:"Karianne",email:"Julianne.OConner@kory.org",website:"kale.biz"},{id:5,name:"Chelsey Dietrich",username:"Kamren",email:"Lucio_Hettinger@annie.ca",website:"demarco.info"},{id:6,name:"Mrs. Dennis Schulist",username:"Leopoldo_Corkery",email:"Karley_Dach@jasper.info",website:"ola.org"},{id:7,name:"Kurtis Weissnat",username:"Elwyn.Skiles",email:"Telly.Hoeger@billy.biz",website:"elvis.io"},{id:8,name:"Nicholas Runolfsdottir V",username:"Maxime_Nienow",email:"Sherwood@rosamond.me",website:"jacynthe.com"},{id:9,name:"Glenna Reichert",username:"Delphine",email:"Chaim_McDermott@dana.io",website:"conrad.com"},{id:10,name:"Clementina DuBuque",username:"Moriah.Stanton",email:"Rey.Padberg@karina.biz",website:"ambrose.net"}]}}},y=w,_=Object(m["a"])(y,v,g,!1,null,"4d3bbd48",null),x=_.exports;r["default"].use(u.a,{colors:{primary:"#5b3cc4",success:"rgb(23, 201, 100)",danger:"rgb(242, 19, 93)",warning:"rgb(255, 130, 0)",dark:"rgb(36, 33, 69)"}});var k={name:"App",components:{Card:h,Table:x},methods:{checkImage:function(e){var t=new Image;if(t.src=e,t.complete)return!0;t.onload=function(){return!0},t.onerror=function(){return!1}},news:function(){var e=Object(s["a"])(regeneratorRuntime.mark((function e(){var t,n;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.next=2,fetch("http://localhost:5000/news");case 2:if(t=e.sent,!t.ok){e.next=11;break}return e.next=6,t.json();case 6:return n=e.sent,this.newsList=n,e.abrupt("return",!0);case 11:return alert("HTTP-Error: "+t.status),e.abrupt("return",!1);case 13:case"end":return e.stop()}}),e,this)})));function t(){return e.apply(this,arguments)}return t}()},data:function(){return{newsList:[]}}},S=k,j=(n("034f"),Object(m["a"])(S,a,i,!1,null,null,null)),O=j.exports;r["default"].use(u.a),r["default"].config.productionTip=!1,new r["default"]({render:function(e){return e(O)}}).$mount("#app")},"85ec":function(e,t,n){}});
//# sourceMappingURL=app.cca54eb9.js.map