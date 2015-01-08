
var duoshuoQuery = {short_name:"xinyuanshuo"};
  (function() {
    var ds = document.createElement('script');
    ds.type = 'text/javascript';ds.async = true;
    ds.src = (document.location.protocol == 'https:' ? 'https:' : 'http:') + '//static.duoshuo.com/embed.js';
    ds.charset = 'UTF-8';
    (document.getElementsByTagName('head')[0] 
     || document.getElementsByTagName('body')[0]).appendChild(ds);
  })();

<!-- 多说公共JS代码 end -->

//向服务器post
  $("#complete,#delete,#join").bind("click", function () {
      $(this).button('loading');
      $.post("/wish", {optype:this.id,wishid:parseInt($(".am-text-primary.am-text-lg").text().slice(1))},
        function (data) {
          alert(data);
          if (data != "成功删除") {
            location.reload();
          } else {
            location.href = "/pool";
          }
        });
      $(this).button('reset');
    })
//修复bug
$(".am-g.am-u-sm-centered").css("padding","0");
