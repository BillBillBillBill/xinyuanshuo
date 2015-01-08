//获取当前时间
function getFormatTime()
{
  function addzero(t){return t<10?'0'+t:t;};
  var time = new Date();
  var y = time.getFullYear();
  var m = time.getMonth()+1;
  var d = time.getDate();
  var h = time.getHours();
  var mm = time.getMinutes();
  var s = time.getSeconds();
  return y+'-'+m+'-'+d+' '+addzero(h)+':'+addzero(mm)+':'+addzero(s);
}

//表单验证
$("#user-intro").bind("change", function() {
    var parent = $("div.am-u-sm-9:nth-child(2)")
    if ($("#user-intro").val()) {
      parent.removeClass("am-form-error");
      parent.addClass("am-form-success");
    }
    else {
      parent.removeClass("am-form-success");
      parent.addClass("am-form-error");
    }
  })

//在页面顶部弹出提示
function alertmsg(msg) {
  $(".am-comments-list").prepend("<div class='am-alert' data-am-alert><button type='button' class='am-close'>&times;</button><p>"+ msg +"</p></div>");
  $('.am-alert').sticky({top: 65});
  setTimeout("$('.am-alert').remove();", 2000);
}

//向服务器post
$(".am-btn.am-btn-primary").bind("click", function () {
  if ($("#user-intro").val().length > 250) {
    alertmsg("留言不能超过250字哦");
  }
  else if ($("#user-intro").val()) {
      var btn = $(this)
      btn.button('loading');
      if (!$("#user-name").val()) {
              names = ["盖伦","易大师","提莫","安妮","阿利斯塔","崔斯特","潘森","古拉加斯","奈德丽","伊泽瑞尔","奥拉夫","伊芙琳","金克丝","卡萨丁","基兰","阿木木","赵信","李青","路人甲","路人已","路人丙","路人丁"];
              var name = names[Math.floor(Math.random() * 22)];
      } else {
        var name = $("#user-name").val();
      }
      $.post("/board", {name:name,content: $("#user-intro").val(),time:getFormatTime()},
          function (data) {
          if (data == "成功提交!!") {
            $(".am-comments-list").prepend("<li class='am-comment'><img src='/static/i/avatar/7.jpg' alt='头像' class='am-comment-avatar' width='50' height='50'><div class='am-comment-main'><header class='am-comment-hd'><div class='am-comment-meta'>" + name +" 评论于 " + getFormatTime() + "</div></header><div class='am-comment-bd'><p>"+$("#user-intro").val()+"</p></div></div></li>");
            $("#user-intro").val("");
          }
          alertmsg(data);
          
          setTimeout(function(){btn.button('reset');},2500);
        });
    } else {
      alertmsg("请输入后再提交..");
    }
  })


$(document).ready(function(){
  //设置随机头像
  for (var i = 0; i < $(".am-comment-avatar").length; i++) {
    $($(".am-comment-avatar")[i]).attr("src","/static/i/avatar/"+String(Math.floor(Math.random() * 17))+".jpg");
  }
  //选中当前页面
  $("#pagination").val("/board/{{ id }}");

  //选中后跳转
  $("#pagination").change(
    function(){
      window.location.href=$(this).children('option:selected').val();
  });

  //隐藏头尾导航
  if ($("#nextpage").attr("href") == "/board/"+{{ len(msglist)/10+2 }}) {
    $("#nextpage").hide();
  }
  if ($("#prvpage").attr("href") == "/board/0") {
    $("#prvpage").hide();
  }

});


